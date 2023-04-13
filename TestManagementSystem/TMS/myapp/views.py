from django.shortcuts import render
from .models import *
from django.contrib import messages


def home(request):
    questions = QuesModel.objects.all().order_by('?')[0:10]

    if request.method == 'POST':
        keys = list(request.POST.keys())[1:-1]
        values = list(request.POST.values())[1:-1]
        dic = dict(zip(keys, values))
        wrong = 0
        correct = 0
        total_attempt = 0
        for k, v in dic.items():
            total_attempt += 1
            ansobj = AnswerModel.objects.get(question_id=k)
            if ansobj.ans == v:
                correct += 1
                continue
            wrong += 1
        score = correct
        context = {
            'score': score,
            'wrong': wrong,
            'correct': correct,
            'total_attempt': total_attempt
        }
        messages.success(request, 'Your test is submitted successfully')
        if score > 5:
            messages.warning(request, 'Congrats.. You Pass This Quiz')
        else:
            messages.error(request, 'Oops... You Fail This Quiz')
        return render(request, 'result.html', context)
    context = {
        'questions': questions
    }
    return render(request, 'home.html', context)


def add_question(request):
    if request.method == 'POST':
        question = request.POST.getlist('question')
        op1 = request.POST.getlist('op1')
        op2 = request.POST.getlist('op2')
        op3 = request.POST.getlist('op3')
        op4 = request.POST.getlist('op4')
        ans = request.POST.getlist('ans')
        list1 = []
        list2 = []
        for que in range(len(question)):
            obj = QuesModel(question=question[que], op1=op1[que], op2=op2[que], op3=op3[que], op4=op4[que])
            list1.append(obj)
            list2.append(AnswerModel(question=obj, ans=ans[que]))
        QuesModel.objects.bulk_create(list1)
        AnswerModel.objects.bulk_create(list2)
    return render(request, 'addQuestion.html')
