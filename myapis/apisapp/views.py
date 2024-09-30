from django.shortcuts import render, redirect
from django.http import HttpResponse,JsonResponse
import psutil
from .models import person_collection, Messages, User, Message, Store, Bus, Forest, Coins
from apisapp.form import Login, Register, Message1, add_std, Deregister,Boot1,buyCoin, sendCoin, coinLogin, Quiz
from django.contrib import messages
import json
from django.core import serializers
from apisapp.serializers import StoreSerializer, ForestSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from scipy import stats
# Create your views here.
def api(request):
    records = {
        "first_name":"Gideon",
        "last_name":"Smith",
    }
    person_collection.insert_one(records)
    return HttpResponse("New person is added")

#for the login part
def login(request):
    form = Login(request.POST)
    if form.is_valid():
        if request.method == 'POST':
            email = request.POST.get('email')
            password = request.POST.get('password')
            if User.objects.filter(email=email, password=password).exists():
                user_details = User.objects.get(email=email)
                user_name = user_details.name
                user_email = user_details.email
                classteacher = user_details.classteacher
                user_phone_number = user_details.phone_number
                user_admission_no = user_details.admission_no
                user_form = user_details.form
                billed = user_details.billed 
                paid = user_details.paid
                request.session['user_name'] = user_name
                request.session['user_email'] = user_email
                request.session['user_phone_number'] = user_phone_number
                request.session['user_admission_no'] = user_admission_no
                request.session['user_form'] = user_form
                request.session['billed'] = billed
                request.session['paid'] = paid
                request.session['classteacher'] = classteacher
                return redirect('school')
            else:
                return render(request, 'login.html',{'form':form})
            
    else:
        return render(request, 'login.html',{'form':form})
    
#for the school home page
def school(request):
    user_name = request.session.get('user_name',None)
    user_email = request.session.get('user_email',None)
    return render(request, 'school.html', {'user_name':user_name,'user_email':user_email})

#for the register part
def register(request):
    reg_form = Register(request.POST)
    if reg_form.is_valid():
        if request.method == 'POST':
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone_number = request.POST.get('phone_number')
            password = request.POST.get('password')
            password2 = request.POST.get('password2')

            if User.objects.filter(email=email).exists():
                messages.info(request, "The email already exists")
            elif password == password2:
                user_data = User(name=name, email=email, phone_number=phone_number, password=password)
                user_data.save()
                return redirect('login')
        

    return render(request, 'register.html',{'reg_form':reg_form})

#for the messages part from the school home page
def message(request):
    if request.method == 'POST':
        name = request.POST.get('Name')
        email = request.POST.get('Email')
        message = request.POST.get('Message')
        if Messages.objects.filter(email=email, message=message).exists():
            return render(request, 'school.html',{'success':'Message was already submitted!'})
        
        else:
           msg = Messages(name=name,email=email,message=message)
           msg.save()
           return render(request, 'school.html',{'success':"Thank you for your message!"})
    else:
        return HttpResponse("Error occurred when sending the message")
    
#for the student portal part
def portal(request):
    user_name = request.session.get('user_name',None)
    user_email = request.session.get('user_email',None)
    user_phone_number = request.session.get('user_phone_number', None)
    user_admission_no = request.session.get('user_admission_no',None)
    classteacher = request.session.get('classteacher',None)
    user_form = request.session.get('user_form',None)
    billed = request.session.get('billed',None)
    paid = request.session.get('paid',None)
    balance = billed - paid
    return render(request, 'portal.html',{'user_name':user_name,
                                          'user_email':user_email, 
                                          'user_phone_number':user_phone_number,
                                          'user_admission_no':user_admission_no,
                                          'user_form':user_form,
                                          'billed':billed,
                                          'paid':paid,
                                          'classteacher':classteacher,
                                          'balance':balance,
                                          })


#for viewing messages that have been sent by admin
def messages_view(request):
    msg = Message.objects.values('message', 'time')
    context = { 
        'msg':msg,
    }
    return render(request, 'messages.html',context)


#for the admin part
def admin1(request):
    add_std_form = add_std(request.POST)
    if add_std_form.is_valid():
        if request.method == 'POST':
            name = request.POST.get('name')
            admission_no = request.POST.get('admission_no')
            form = request.POST.get('form')
            classteacher = request.POST.get('classteacher')
            billed = request.POST.get('billed')
            paid = request.POST.get('paid')
            email = request.POST.get('email')
            password = request.POST.get('password')
            phone_number = request.POST.get('phone_number')
            if User.objects.filter(admission_no=admission_no).exists():
                messages.info(request, "Student is already admitted")
                return render(request, 'admin1.html',{'add_std_form':add_std_form})
            else:
                user_data = User(name=name,email=email,form=form,classteacher=classteacher, password=password,admission_no=admission_no, phone_number=phone_number,billed=billed,paid=paid)
                user_data.save()
                messages.info(request, 'Student admitted')
                return render(request, 'admin1.html', {'add_std_form':add_std_form})
    return render(request, 'admin1.html', {'add_std_form':add_std_form})

#for the admin part to send messages to the users
def messages_send(request):
    msg_form = Message1(request.POST)
    if msg_form.is_valid():
        if request.method == 'POST':
            message = request.POST.get('message')
            if Message.objects.filter(message=message).exists():
                messages.info(request, 'Message already sent')
                return render(request, 'admin1.html', {'msg_form':msg_form})
            else:
                msg = Message(message=message)
                msg.save()
                messages.info(request, 'Message sent')
                return render(request, 'admin1.html', {'msg_form':msg_form})
    return render(request, 'admin1.html', {'msg_form':msg_form})

#for the deregister part 
def deregister(request):
    deregister_form = Deregister(request.POST)
    if deregister_form.is_valid():
        if request.method == 'POST':
            id_number = request.POST.get('id_number')
            if User.objects.filter(admission_no = id_number).exists():
                user_to_delete = User.objects.get(admission_no = id_number)
                user_to_delete.delete()
                messages.info(request, 'Successful deleted')
                return render(request, 'admin1.html', {'deregister_form':deregister_form})
            else:
                messages.info(request, 'The id does not exists!!')
                return render(request, 'admin1.html', {'deregister_form':deregister_form})

    return render(request, 'admin1.html',{'deregister_form':deregister_form})


#for the form1 details part 
def form1(request):
    return render(request, 'form1.html')

#for the teacher to add marks
def addMarks(request):
    return render(request, 'addMarks.html')

#for the store api
def store(request, name=None):
    stores_list = Store.objects.all()

    if name:
        stores_list = stores_list.filter(name=name)
    if 'type' in request.GET and request.GET['type'] == 'xml':
        serialized_stores = serializers.serialize('xml', stores_list)
        return HttpResponse(serialized_stores, content_type='application/xml')
    else:
        serialized_stores = serializers.serialize('json', stores_list)
        return HttpResponse(serialized_stores, content_type='application/json')
    #store_names = [{"name":store.name} for store in stores_list]
    #return HttpResponse(json.dumps(store_names), content_type='application/json')
@api_view(['GET','POST','DELETE'])
def rest_store(request):
    if request.method == 'GET':
        stores = Store.objects.all()
        serializers = StoreSerializer(stores, many=True)
        return Response(serializers.data)
    
    elif request.method == 'POST':
        pass 
    elif request.method == 'DELETE':
        pass

@api_view(['GET', 'POST', 'DELETE'])
def forest(request):
    if request.method == 'GET':
        forests = Forest.objects.all()
        f_serializer = ForestSerializer(forests, many=True)
        return Response(f_serializer.data)

def bus(request):
    buses = Bus.objects.all()
    serialized_bus = serializers.serialize('json', buses)
    return HttpResponse(serialized_bus, content_type='application/json')

#for the music page 
def music(request):

    return render(request, 'music.html')

def boot(request):
    form = Boot1(request.POST)
    if form.is_valid():
        if request.method == 'POST':
            return render(request, 'boot.html', {'form':form})
    return render(request, 'boot.html', {'form':form})


def coins(request):
    send = sendCoin(request.POST)
    login = coinLogin(request.POST)
    buy = buyCoin(request.POST)
    email2 = request.session.get('email2',None)
    if send.is_valid():
        if request.method == 'POST':
            personID = request.POST.get("personID")
            amount = request.POST.get("Amount")
            password = request.POST.get("Password")
            sender = Coins.objects.get(personID=2000)
            if Coins.objects.filter(personID=personID).exists():
                if int(sender.coins) > int(amount) and password == sender.password:
                    
                    messages.info(request, "You can send")
                    return render(request, 'coins.html', {"send":send, "email2":email2})
                else:
                    messages.info(request, "Insufficient balance")
                    return render(request, 'coins.html', {"send":send, "email2":email2})
            else:
                messages.info(request, 'Wrong password')
                return render(request, 'coins.html', {"send":send, "email2":email2})

    return render(request, 'coins.html', {"send":send, "buy":buy, "login":login, "email2":email2})
def coinLogin1(request):
    login = coinLogin(request.POST)
    send = sendCoin(request.POST)
    if login.is_valid():
        if request.method == 'POST':
            email = request.POST.get("Email")
            password = request.POST.get("Password")
            if Coins.object.filter(email=email, password=password).exists():
                email2 = email
                request.session['email2'] = email2
                return redirect('coins');
            else:
                messages.warning(request, "Invalid inputs")
                return render(request, "coins.html", {"login":login})

            

    return render(request, 'coins.html', {"login":login})

#for the mobile app api

def speed(request, age):
    #speed1 = 0
    x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
    y = [99,86,87,88,111,86,103,87,94,78,77,85,86]
    slope, intercept, r, p, std_err = stats.linregress(x, y)
    def myfunc(x):
        return slope * x + intercept
    speed = myfunc(age)
    return HttpResponse(json.dumps(speed), content_type='application/json')

def near_shop(request, shop):
    shop = shop
    
    return HttpResponse(json.dumps(shop), content_type='application/json')
    