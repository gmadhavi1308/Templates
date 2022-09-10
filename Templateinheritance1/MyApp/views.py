from django.shortcuts import render
import datetime
# Create your views here.
def index(request):
    return render(request,'home.html')

def examples(request):
    return render(request,'examples.html')

def projects(request):
    d=datetime.datetime(2022,11,1)
    info={'fname':'teja','lname':'Reddy','sub':562,'lab':266,'Section':'',
    'project_tittle':'Student INFORMATION System','sub_date':d,'email':'tejareddy@gmail.com'}
    lis=['Languages',['C','C++','python'],'package',['Ms Office','Tally']]
    data=[{'name':'sam','age':20},{'name':'Raj'}]
    marks=[78,23,72,30,66,39]
    return render(request,'projects.html',{'info':info,'lis':lis,'data':data,'marks':marks})

def documents(request):
    return render(request,'documents.html')

def contact(request):
    return render(request,'contact.html')

# Create your views here.
