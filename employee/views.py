from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth import login,logout,authenticate
# Create your views here.


def index(request):
    return render(request,'index.html')

def registration(request):
    error = ""
    if request.method == "POST":
        fn = request.POST['firstname']
        ln = request.POST['lastname']
        ec = request.POST['empcode']
        email = request.POST['email']
        pwd = request.POST['pwd']

        try:
     
            user = User.objects.create_user(first_name=fn, last_name=ln, username=email, password=pwd)
            EmployeeDetail.objects.create(user=user, empcode=ec)
            EmployeeExperience.objects.create(user=user)
            EmployeeEducation.objects.create(user=user)

            error = "no"

        except:
            error = "yes"

    return render(request,'registration.html',locals())


def emp_login(request):
    error = ""
    if request.method == "POST":
        u = request.POST['emailid']
        p = request.POST['password']

        user = authenticate(username=u, password=p)
        if user:
            login(request,user)
            error = "no"

        else:
            error = "yes"

    return render(request,'emp_login.html',locals())


def emp_home(request):
    if not request.user.is_authenticated:
        return redirect('emplogin')
    return render(request, 'emp_home.html')

def Logout(request):
    logout(request)
    return redirect('index')

def profile(request):
    if not request.user.is_authenticated:
        return redirect('emplogin')

    error = ""
    user = request.user
    employee = EmployeeDetail.objects.get(user=user)
    
    if request.method == "POST":
        fn = request.POST['firstname']
        ln = request.POST['lastname']
        ec = request.POST['empcode']
        dept = request.POST['department']
        designation = request.POST['designation']
        contact = request.POST['contact']
        jdate = request.POST['jdate']
        gender = request.POST['gender']
        

        employee.user.first_name = fn
        employee.user.first_name = ln
        employee.empcode = ec
        employee.empdept = dept
        employee.designation = designation
        employee.contact = contact
        employee.joiningdate = jdate
        employee.gender = gender

        if jdate:
            employee.joiningdate = jdate

        try:
            employee.save()
            employee.user.save()

            error = "no"
        except:
            error = "yes"

    return render(request, 'profile.html', locals())


def admin_login(request):

    error = ""
    if request.method == "POST":
        u = request.POST['username']
        p = request.POST['pwd']

        user = authenticate(username=u, password=p)

        try:

            if user.is_staff:
                login(request,user)
                error = "no"
            else:
                error = "yes"

        except:
                error = "yes"        

    return render(request, 'admin_login.html',locals())

def admin_home(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    return render(request, 'admin_home.html')




def my_experience(request):
    if not request.user.is_authenticated:
        return redirect('emplogin')
    
    user = request.user
    experience = EmployeeExperience.objects.get(user=user)
    

    return render(request,'my_experience.html',locals())


def edit_experience(request):
    if not request.user.is_authenticated:
        return redirect('emplogin')

    error = ""
    user = request.user
    experience = EmployeeExperience.objects.get(user=user)
    
    if request.method == "POST":
        cn1 = request.POST['company1name']
        jd1 = request.POST['company1deg']
        js1 = request.POST['company1salary']
        jduration1 = request.POST['company1duration']
        cn2 = request.POST['company2name']
        jd2 = request.POST['company2deg']
        js2 = request.POST['company2salary']
        jduration2 = request.POST['company2duration']
        cn3 = request.POST['company3name']
        jd3 = request.POST['company3deg']
        js3 = request.POST['company3salary']
        jduration3 = request.POST['company3duration']
        
        
        experience.company1name = cn1
        experience.company1deg = jd1
        experience.company1salary = js1
        experience.company1duration = jduration1
        experience.company2name = cn2
        experience.company2deg = jd2
        experience.company2salary = js2
        experience.company2duration = jduration2
        experience.company3name = cn3
        experience.company3deg = jd3
        experience.company3salary = js3
        experience.company3duration = jduration3

        try:
            experience.save()

            error = "no"
        except:
            error = "yes"

    return render(request, 'edit_experience.html', locals())

def my_education(request):
    if not request.user.is_authenticated:
        return redirect('emplogin')
    
    user = request.user
    education = EmployeeEducation.objects.get(user=user)
    

    return render(request,'my_education.html',locals())


def edit_education(request):
    if not request.user.is_authenticated:
        return redirect('emplogin')

    error = ""
    user = request.user
    education = EmployeeEducation.objects.get(user=user)
    
    if request.method == "POST":
        pgcourse = request.POST['pgcourse']
        pgclg = request.POST['pgclg']
        pgpassingyear = request.POST['pgpassingyear']
        pgpercentage = request.POST['pgpercentage']

        gradcourse = request.POST['gradcourse']
        gradclg = request.POST['gradclg']
        gradpassingyear = request.POST['gradpassingyear']
        gradpercentage = request.POST['gradpercentage']

        ssccourse = request.POST['ssccourse']
        sscclg = request.POST['sscclg']
        sscpassingyear = request.POST['sscpassingyear']
        sscpercentage = request.POST['sscpercentage']

        hsccourse = request.POST['hsccourse']
        hscclg = request.POST['hscclg']
        hscpassingyear = request.POST['hscpassingyear']
        hscpercentage = request.POST['hscpercentage']
        
        
        education.coursepg = pgcourse
        education.schoolclgpg = pgclg
        education.yearofpassingpg = pgpassingyear
        education.percentagepg = pgpercentage
        education.coursegra = gradcourse
        education.schoolclggra = gradclg
        education.yearofpassinggra = gradpassingyear
        education.percentagegra = gradpercentage
        education.coursessc = ssccourse
        education.schoolclgssc = sscclg
        education.yearofpassingssc = sscpassingyear
        education.percentagessc = sscpercentage
        education.coursehsc = hsccourse
        education.schoolclghsc = hscclg
        education.yearofpassinghsc = hscpassingyear
        education.percentagehsc = hscpercentage

        if pgpassingyear:
            education.yearofpassingpg = pgpassingyear

        if gradpassingyear:
            education.yearofpassinggra = gradpassingyear

        if sscpassingyear:
            education.yearofpassingssc = sscpassingyear

        if hscpassingyear:
            education.yearofpassinghsc = hscpassingyear
       

        try:
            education.save()

            error = "no"
        except:
            error = "yes"

    return render(request, 'edit_education.html', locals())



def change_password(request):
    if not request.user.is_authenticated:
        return redirect('emplogin')

    error = ""
    user = request.user

    if request.method == "POST":
        cur = request.POST['currentpassword']
        new = request.POST['newpassword']


        try:
            if user.check_password(cur): 
                user.set_password(new)
                user.save()
                error = "no"
            else:
                error = "not"
        except:
            error = "yes"

    return render(request, 'change_password.html', locals())


def change_adminpassword(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')

    error = ""
    user = request.user

    if request.method == "POST":
        cur = request.POST['currentpassword']
        new = request.POST['newpassword']


        try:
            if user.check_password(cur): 
                user.set_password(new)
                user.save()
                error = "no"
            else:
                error = "not"
        except:
            error = "yes"

    return render(request, 'change_adminpassword.html', locals())

def all_employee(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    
    employee = EmployeeDetail.objects.all()
    return render(request, 'all_employee.html',locals())

def edit_profile(request,pid):
    if not request.user.is_authenticated:
        return redirect('emplogin')

    error = ""
    user = User.objects.get(id=pid)
    employee = EmployeeDetail.objects.get(user=user)
    
    if request.method == "POST":
        fn = request.POST['firstname']
        ln = request.POST['lastname']
        ec = request.POST['empcode']
        dept = request.POST['department']
        designation = request.POST['designation']
        contact = request.POST['contact']
        jdate = request.POST['jdate']
        gender = request.POST['gender']
        

        employee.user.first_name = fn
        employee.user.first_name = ln
        employee.empcode = ec
        employee.empdept = dept
        employee.designation = designation
        employee.contact = contact
        employee.joiningdate = jdate
        employee.gender = gender

        if jdate:
            employee.joiningdate = jdate

        try:
            employee.save()
            employee.user.save()

            error = "no"
        except:
            error = "yes"
    return render(request,'edit_profile.html',locals())

def delete_employee(request,pid):
    if not request.user.is_authenticated:
        return redirect('emplogin')

    error = ""
    
    if request.method == "POST":
        
        try:
            user = User.objects.get(id=pid)
            employee = EmployeeDetail.objects.get(user=user)
            
            # Delete related objects if necessary
            # For example:
            # education = EmployeeEducation.objects.get(user=user)
            # education.delete()
            
            user.delete()
            employee.delete()
            
            error = "no"
        except:
            error = "yes"
    return render(request,'delete_employee.html',locals())

def adminedit_education(request,pid):
    if not request.user.is_authenticated:
        return redirect('emplogin')

    error = ""
    user = User.objects.get(id=pid)
    education = EmployeeEducation.objects.get(user=user)
    
    if request.method == "POST":
        pgcourse = request.POST['pgcourse']
        pgclg = request.POST['pgclg']
        pgpassingyear = request.POST['pgpassingyear']
        pgpercentage = request.POST['pgpercentage']

        gradcourse = request.POST['gradcourse']
        gradclg = request.POST['gradclg']
        gradpassingyear = request.POST['gradpassingyear']
        gradpercentage = request.POST['gradpercentage']

        ssccourse = request.POST['ssccourse']
        sscclg = request.POST['sscclg']
        sscpassingyear = request.POST['sscpassingyear']
        sscpercentage = request.POST['sscpercentage']

        hsccourse = request.POST['hsccourse']
        hscclg = request.POST['hscclg']
        hscpassingyear = request.POST['hscpassingyear']
        hscpercentage = request.POST['hscpercentage']
        
        
        education.coursepg = pgcourse
        education.schoolclgpg = pgclg
        education.yearofpassingpg = pgpassingyear
        education.percentagepg = pgpercentage
        education.coursegra = gradcourse
        education.schoolclggra = gradclg
        education.yearofpassinggra = gradpassingyear
        education.percentagegra = gradpercentage
        education.coursessc = ssccourse
        education.schoolclgssc = sscclg
        education.yearofpassingssc = sscpassingyear
        education.percentagessc = sscpercentage
        education.coursehsc = hsccourse
        education.schoolclghsc = hscclg
        education.yearofpassinghsc = hscpassingyear
        education.percentagehsc = hscpercentage

        if pgpassingyear:
            education.yearofpassingpg = pgpassingyear

        if gradpassingyear:
            education.yearofpassinggra = gradpassingyear

        if sscpassingyear:
            education.yearofpassingssc = sscpassingyear

        if hscpassingyear:
            education.yearofpassinghsc = hscpassingyear
       

        try:
            education.save()

            error = "no"
        except:
            error = "yes"
    return render(request,'adminedit_education.html',locals())


def adminedit_experience(request,pid):
    if not request.user.is_authenticated:
        return redirect('emplogin')

    error = ""
    user = User.objects.get(id=pid)
    experience = EmployeeExperience.objects.get(user=user)
    
    if request.method == "POST":
        cn1 = request.POST['company1name']
        jd1 = request.POST['company1deg']
        js1 = request.POST['company1salary']
        jduration1 = request.POST['company1duration']
        cn2 = request.POST['company2name']
        jd2 = request.POST['company2deg']
        js2 = request.POST['company2salary']
        jduration2 = request.POST['company2duration']
        cn3 = request.POST['company3name']
        jd3 = request.POST['company3deg']
        js3 = request.POST['company3salary']
        jduration3 = request.POST['company3duration']
        
        
        experience.company1name = cn1
        experience.company1deg = jd1
        experience.company1salary = js1
        experience.company1duration = jduration1
        experience.company2name = cn2
        experience.company2deg = jd2
        experience.company2salary = js2
        experience.company2duration = jduration2
        experience.company3name = cn3
        experience.company3deg = jd3
        experience.company3salary = js3
        experience.company3duration = jduration3

        try:
            experience.save()

            error = "no"
        except:
            error = "yes"

    return render(request, 'adminedit_experience.html', locals())







 