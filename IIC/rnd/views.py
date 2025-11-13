from django.shortcuts import render , redirect
from .models import dept , facult , suff , patent , copyright , conference , book , bookChapter , journal , basicDetails
from .forms import basicDetailsForm

# Create your views here.

def rnd(req):
    dep = dept.objects.all()
    context = {"dept" : dep}
    return render(req,'rd.html', context)

def depart(req , pk):
    dep = dept.objects.get(id = pk)
    faculty = facult.objects.filter(dept = dep)
    suf = suff.objects.all()
    context = {"faculty" : faculty , "suf" : suf}
    return render(req , 'depart.html' , context)

def facul(req , pk):
    faculty = facult.objects.get(id = pk)
    pat = patent.objects.filter(faculty = faculty)
    copyr = copyright.objects.filter(faculty = faculty)
    books = book.objects.filter(faculty = faculty)
    bookchapters = bookChapter.objects.filter(faculty = faculty)
    journals = journal.objects.filter(faculty = faculty)
    conferences = conference.objects.filter(faculty = faculty)
    context = {"faculty" : faculty , "patent" : pat , "books" : books , "journals" : journals , "bookchapters" : bookchapters , "copyrights" : copyr , "conferences" : conferences}
    return render(req , 'faculty.html' , context)

def basicCreate(req):
    basicsf = basicDetailsForm()
    if(req.method == "POST"):
        basicsf = basicDetails(req.POST)
        if(basicsf.is_valid()):
            basicsf.save()
        return redirect("admin-site")
    context = {'basicsf' : basicsf}
    return render(req , "form.html" , context)

def basicEdit(req , pk):
    basic = basicDetails.objects.get(id = pk)
    basicf = basicDetailsForm(instance = basic)
    if(req.method == "POST"):
        basicf = basicDetailsForm(req.POST , instance = basic)

        if basicf.is_valid():
            basicf.save()
            return redirect('admin-site')
    context = {'basicf' : basicf}
    return render(req,"form.html",context)

def basicDeletion(req , pk):
    basic = basicDetails.objects.get(id = pk)
    basic.delete()
    return redirect('admin-site')