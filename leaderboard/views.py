from django.shortcuts import render, get_object_or_404,redirect,HttpResponse
from .models import Scorecard
from .forms import Enter_Score
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,authenticate,logout 
import requests
import random
from django.http import JsonResponse


# Create your views here.

API_URL = "https://matrix.org:8448/_matrix/client/r0/"
room_id = ""


def landingpage(request):
    return render(request , 'leaderboard/nonlogin.html')


def create(request):
    if "create" in request.POST: 
        roomname = request.POST.get('roomname', None)
        createroom_url =  API_URL + "createRoom?access_token=MDAxOGxvY2F0aW9uIG1hdHJpeC5vcmcKMDAxM2lkZW50aWZpZXIga2V5CjAwMTBjaWQgZ2VuID0gMQowMDJlY2lkIHVzZXJfaWQgPSBAaGFyaXNoZ2FuYXBhdGhpOm1hdHJpeC5vcmcKMDAxNmNpZCB0eXBlID0gYWNjZXNzCjAwMjFjaWQgbm9uY2UgPSA3PTU1WWxtT1AjZXp-MjYrCjAwMmZzaWduYXR1cmUgF6QjpTKDnCISNpfUzbdcir-kIve4J78N336tGQtTrgsK"
        room_detail_json = {
            "room_alias_name": roomname}
        response_obj = requests.post(createroom_url ,json=room_detail_json)
        response_obj_json = response_obj.json()
        global room_id 
        try:
            room_id = response_obj_json['room_id']
            return redirect('sendmessage')
        except:
            return HttpResponse('Sorry,Please enter a different Room Name ')
    else:
        return render(request, 'leaderboard/landingpage.html')

'''
def joined(request):
    if "create" in request.POST:
        roomname = request.POST.get('roomname', None)
        createroom_url = API_URL + "createRoom?access_token=MDAxOGxvY2F0aW9uIG1hdHJpeC5vcmcKMDAxM2lkZW50aWZpZXIga2V5CjAwMTBjaWQgZ2VuID0gMQowMDJlY2lkIHVzZXJfaWQgPSBAaGFyaXNoZ2FuYXBhdGhpOm1hdHJpeC5vcmcKMDAxNmNpZCB0eXBlID0gYWNjZXNzCjAwMjFjaWQgbm9uY2UgPSA3PTU1WWxtT1AjZXp-MjYrCjAwMmZzaWduYXR1cmUgF6QjpTKDnCISNpfUzbdcir-kIve4J78N336tGQtTrgsK"
        room_detail_json = {
            "room_alias_name": roomname}
        response_obj = requests.post(createroom_url, json=room_detail_json)
        response_obj_json = response_obj.json()
        global room_id
        room_id += response_obj_json['room_id']
        return redirect('sendmessage')
    else:
        return render(request, 'leaderboard/landingpage.html')
'''
def join(request):
    if request.method == "POST":
        global room_id
        room_id = request.POST.get('roomname', None)
        joinroom_url = API_URL +"rooms/"+room_id + "/join?access_token=MDAxOGxvY2F0aW9uIG1hdHJpeC5vcmcKMDAxM2lkZW50aWZpZXIga2V5CjAwMTBjaWQgZ2VuID0gMQowMDJlY2lkIHVzZXJfaWQgPSBAaGFyaXNoZ2FuYXBhdGhpOm1hdHJpeC5vcmcKMDAxNmNpZCB0eXBlID0gYWNjZXNzCjAwMjFjaWQgbm9uY2UgPSA3PTU1WWxtT1AjZXp-MjYrCjAwMmZzaWduYXR1cmUgF6QjpTKDnCISNpfUzbdcir-kIve4J78N336tGQtTrgsK"
        print(joinroom_url)
        response_obj = requests.post(joinroom_url)
        return redirect('sendmessage')
    else:
        return render(request, 'leaderboard/landingpage.html')


def sendmessage(request):
    if request.method == 'POST':
        event_num = str(random.randint(0, 137863))
        message_body = request.POST['message_body']
        message_body_json = {'body': message_body}
        send_message_url = API_URL + "rooms/" + room_id + "/send/m.text/" + event_num + \
            "?access_token=MDAxOGxvY2F0aW9uIG1hdHJpeC5vcmcKMDAxM2lkZW50aWZpZXIga2V5CjAwMTBjaWQgZ2VuID0gMQowMDJlY2lkIHVzZXJfaWQgPSBAaGFyaXNoZ2FuYXBhdGhpOm1hdHJpeC5vcmcKMDAxNmNpZCB0eXBlID0gYWNjZXNzCjAwMjFjaWQgbm9uY2UgPSA3PTU1WWxtT1AjZXp-MjYrCjAwMmZzaWduYXR1cmUgF6QjpTKDnCISNpfUzbdcir-kIve4J78N336tGQtTrgsK"
        reponse_message = requests.put(
            send_message_url, json=message_body_json)
        if reponse_message.status_code == 200:
            reponse_message = reponse_message.json()
            eventid = reponse_message['event_id']
            #return render(request, 'leaderboard/createroom.html', {'response_message': reponse_message.json(),'room_id':room_id})
            messages = []
            
            if eventid != "":
            # sample = "https://matrix.org:8448/_matrix/client/r0/rooms/!GVqILJOxQBndsDJXxs:matrix.org/initialSync?access_token=MDAxOGxvY2F0aW9uIG1hdHJpeC5vcmcKMDAxM2lkZW50aWZpZXIga2V5CjAwMTBjaWQgZ2VuID0gMQowMDJlY2lkIHVzZXJfaWQgPSBAaGFyaXNoZ2FuYXBhdGhpOm1hdHJpeC5vcmcKMDAxNmNpZCB0eXBlID0gYWNjZXNzCjAwMjFjaWQgbm9uY2UgPSA3PTU1WWxtT1AjZXp-MjYrCjAwMmZzaWduYXR1cmUgF6QjpTKDnCISNpfUzbdcir-kIve4J78N336tGQtTrgsK"
                message_url = API_URL + "rooms/" + room_id + "/initialSync?access_token=MDAxOGxvY2F0aW9uIG1hdHJpeC5vcmcKMDAxM2lkZW50aWZpZXIga2V5CjAwMTBjaWQgZ2VuID0gMQowMDJlY2lkIHVzZXJfaWQgPSBAaGFyaXNoZ2FuYXBhdGhpOm1hdHJpeC5vcmcKMDAxNmNpZCB0eXBlID0gYWNjZXNzCjAwMjFjaWQgbm9uY2UgPSA3PTU1WWxtT1AjZXp-MjYrCjAwMmZzaWduYXR1cmUgF6QjpTKDnCISNpfUzbdcir-kIve4J78N336tGQtTrgsK"
                response_message_url = requests.get(message_url)
                response_message_url_json = response_message_url.json() 
                for every in response_message_url_json["messages"]["chunk"]:
                    if "content" in every:
                        if "body" in every["content"]:
                            username = every["sender"]
                            messages.append(every["content"]["body"]) 
                            
            #username = str(request.user)       
            return JsonResponse({'messages': messages,'username':username})
        else:
            messages = "Error"
            return JsonResponse({'messages': messages})
    else:
        return render(request, 'leaderboard/createroom.html',{'room_id':room_id})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            obj = form.save(commit = False)
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            email = form.cleaned_data.get('email')
            obj = form.save()
            user = authenticate(username = username , password = password)
            login(request,user)
            return redirect('landingpage')
    else:
        form = UserCreationForm()
    return render(request , 'leaderboard/signup.html' , { 'form':form })


def signin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username= username ,password = password)
        if user is not None:
            login(request, user)
            return redirect('score_list')
    else:
        form = AuthenticationForm()
    return render(request , 'leaderboard/signin.html' , {'form': form})

def signout(request):
    logout(request)
    return render(request,'leaderboard/signout.html')

def broadcast(request):
    if request.method == "POST":
        print(request.POST)
        rooms = []
        room1 = rooms.append(request.POST['room1'])
        room2 = rooms.append(request.POST['room2'])
        room3 = rooms.append(request.POST['room3'])
        broadcast_body = request.POST['message_body']
        broadcast_body_json = {'body': broadcast_body}
        for room in rooms:
            broadcast_url = API_URL + "rooms/" + room + "/send/m.text/" + str(random.randint(0, 137863)) + "?access_token=MDAxOGxvY2F0aW9uIG1hdHJpeC5vcmcKMDAxM2lkZW50aWZpZXIga2V5CjAwMTBjaWQgZ2VuID0gMQowMDJlY2lkIHVzZXJfaWQgPSBAaGFyaXNoZ2FuYXBhdGhpOm1hdHJpeC5vcmcKMDAxNmNpZCB0eXBlID0gYWNjZXNzCjAwMjFjaWQgbm9uY2UgPSA3PTU1WWxtT1AjZXp-MjYrCjAwMmZzaWduYXR1cmUgF6QjpTKDnCISNpfUzbdcir-kIve4J78N336tGQtTrgsK" 
            reponse_message = requests.put(broadcast_url, json=broadcast_body_json)
        return HttpResponse('Broadcast Successfull')
    else:
        return render(request,'leaderboard/broadcast.html',{})


