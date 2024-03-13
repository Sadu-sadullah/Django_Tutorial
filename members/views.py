from django.shortcuts import render, HttpResponse
from .models import Member

def members(request):
    mymembers = Member.objects.all().values()
    context = {
        'mymembers': mymembers,
    }
    return render(request, 'all_members.html', context)

def details(request, id):
    mymember = Member.objects.get(id=id)
    context = {
        'mymember': mymember,
    }
    return render(request, 'details.html', context)

def main(request):
    return render(request, 'main.html')

def testing(request):
    mymembers = Member.objects.all().values()
    context = {
        'mymembers': mymembers,
        'name': 'check'
    }
    return render(request, 'template.html', context)