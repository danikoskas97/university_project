from django.shortcuts import render
from student_app.models import Student

def index(request):
	students = Student.objects.all()
	return render(request , 'students/index.html', context={ 'students': students })



def details(request , student_id):
	student = Student.objects.get(id=student_id)

	return render(request, student_id=student_id)
		