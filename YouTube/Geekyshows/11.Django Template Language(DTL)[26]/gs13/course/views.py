from django.shortcuts import render
# from datetime import datetime

# Create your views here.

# Filter Examples
# def learn_django(request):
#     # return render(request,'course/courseone.html',{'nm':'Django is Awosome'})

#     # d=datetime.now()
#     # return render(request,'course/courseone.html',{'dt':d})
    
#     # return render(request,'course/courseone.html',{'p1':563.21321,'p2':56.00000,'p3':56.37000})

# # if Tag Examples
# def learn_django(request):
#     # return render(request,'course/courseone.html',{'nm':'Django'})

#     return render(request,'course/courseone.html',{'nm':'Django','st':5})

# for loop Examples
def learn_django(request):
    # student={'names':['Rahul','Sonam','Raj','Anu']}
    # return render(request,'course/courseone.html',student)

    # stu={
    #     'stu1':{'name':'Rahul','roll':101},
    #     'stu2':{'name':'Sonam','roll':102},
    #     'stu3':{'name':'Raj','roll':103},
    #     'stu4':{'name':'Anu','roll':104}
    # }
    # students={'student':stu}
    # return render(request,'course\courseone.html',students)
    
    # data={'name':'Rahul','roll':101}
    # return render(request,'course\courseone.html',{'data':data})
    
    data={
        'stu1':{'name':'Rahul','roll':101},
        'stu2':{'name':'Sonam','roll':102},
        'stu3':{'name':'Raj','roll':103},
        'stu4':{'name':'Anu','roll':104}
    }
    return render(request,'course\courseone.html',{'data':data})