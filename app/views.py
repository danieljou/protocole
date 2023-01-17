from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.

def index(request):

    return render(request, 'index.html')

def etudiant(request):
    context = {}
    context['etudiants'] = Etudiant.objects.all()

    return render(request, 'etudiants.html', context)

def etudiant_add(request):
    context = {}
    form = EtudiantForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('etudiants')
    context['form'] = form

    return render(request, 'form_etudiant.html', context)

def etudiant_edit(request, id):
    context = {}
    etudiant = Etudiant.objects.get(pk = id)
    form = EtudiantForm(request.POST or None, instance = etudiant)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('etudiants')
    context['form'] = form

    return render(request, 'form_etudiant.html', context)


def etudiant_delete(request, id):
  
    etudiant = Etudiant.objects.get(pk = id)
    etudiant.delete()
    return redirect('etudiants')

def etudaint_noter(request, id):
    context = {}
    etudiant = Etudiant.objects.get(pk = id)
    form = NotationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            note = form.save(commit = False)
            note.etudiant = etudiant
            note.utilisateur = request.user
            note.save()
            return redirect('etudiants')

    context['etudiant'] = etudiant
    context['form'] = form

    return render(request, 'noter_single.html', context)



def etudiant_notes(request, id):
    context = {}
    etudiant = Etudiant.objects.get(pk = id)
    context['etudiant'] = etudiant
    
    return render(request,'students_notes.html', context)

def notes(request):
    context = {}    
    context['criteres'] = Critere.objects.all()
    students = Etudiant.objects.all()
    context["students"] = students
    listes = []

    def get_total(listes):
        return listes.get('total')

    for item in students:
        listes.append({'student':item, 'total': item.get_tautaux()})
        # print(item.get_tautaux())
    student_list = sorted(listes, key = lambda  x: x.get('total')) 
    i = 0
    for item in student_list:
        item['rank'] = len(student_list) - i
        i = i + 1
    context['student_list'] = student_list
    return render(request, 'notes.html', context)


def noter(request):
    context = {}
    criteres = Critere.objects.all()
    students = Etudiant.objects.all()
    form_criteres = []
    group_student = []


    for student  in students :
        notes_forms = []
        for critere in criteres:
            form = NoteForm(request.POST or None)
            try:
                form2 = form.save(commit = False)
                form2.Critere = critere
                form2.etudiant = student
                form2.utilisateur = request.user
                form3 = NoteForm(request.POST or None, instance = form2)
            except:
                # form2 = form.save(commit = False)
                # form2.Critere = critere
                # form2.etudiant = student
                # form2.utilisateur = request.user
                # form2 = note.objects.filter(etudiant = student, Critere = critere)
                # print(form2)
                form3 = NoteForm(request.POST or None)
            
            
            group = {'Critere': critere, 'form':form3, 'Etudiant':student}
            notes_forms.append(form3)
            # print(form2.utilisateur)
            # print(form2.Critere)
        group_student.append(
            {
                'student':student,
                'form': notes_forms
            }
        )
            

    if request.method == 'POST':
        Validate = True
        for stud in group_student:
            # print(stud['student'])
            # print("\n\n")
            for form in stud['form']:
                if  form.is_valid():
                    # print(form)
                    pass
                else:
                    # print(form)
                    Validate = False
                    break
        
        if Validate:
            for student in group_student: 
                for form in student['form']:
                    # print(form)
                    form.save()
            return redirect('notes')
                    
    context['form_criteres'] = form_criteres
    context['criteres'] = criteres
    context['students'] = students
    context['group_student'] = group_student
    return render(request, 'noter.html', context)