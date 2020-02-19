from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.shortcuts import render_to_response
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import os
import requests
# Create your views here.

def home_page_view(request):
    print(request.headers)
    return render(request, "home.html", {})

@csrf_exempt
def submit_position(request):
    Company = request.POST.get('Company')
    Position = request.POST.get('position')

    url = 'http://localhost:8080/InternshipHUAInternal/api/addposition'
    params = {'compName': Company, 'category': Position}
    response = requests.post(url, data = params)
    if response.status_code == 200:
        print("Code 200")
    else:
        print("Code not 200")

    return render(request, "success_submit.html", {})    


@csrf_exempt
def view_positions(request):
    username = request.user.username
    url = 'http://localhost:8080/InternshipHUAInternal/api/positions'
    param = {'compName': username}

    response = requests.get(url, params = param)
    if response.status_code == 200:
        print("Code 200")
    else:
        print("Code not 200")

    data = response.json()
    print(data)
    print(type(data))

# render_to_response
    return render_to_response("view_positions.html", {"data": data, 'user': request.user})



@csrf_exempt
def view_students(request):
    username = request.user.username   
    posid = request.POST.get('PosId')
    url = 'http://localhost:8080/InternshipHUAInternal/api/studentsForposition'
    param = {'compName': username, 'posID': posid}

    response = requests.get(url, params = param)
    if response.status_code == 200:
        print("Code 200")
    else:
        print("Code not 200")

    data = response.json()
    print(data)
    print(type(data))

# render_to_response
    return render_to_response("view_students.html", {"data": data, "PosId": posid, 'user': request.user})


@csrf_exempt
def choose_student(request):
    posid = request.POST.get('PosId')
    stid = request.POST.get('StudentId')

    url = 'http://localhost:8080/InternshipHUAInternal/api/saveStudentForposition'
    param = {'posID': posid, 'studentID': stid}

    response = requests.post(url, params = param)
    if response.status_code == 200:
        print("Code 200")
    else:
        print("Code not 200")

# render_to_response
    return render_to_response("student_chosen.html", {'user': request.user})