# import re
from django.shortcuts import render, redirect
from django.conf import settings
import yagmail
from .models import *
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib import messages
from .forms import *
from django.core.mail import send_mail
from .tasks import send

# Create your views here.

sender_email = settings.SENDER_EMAIL
sender_password = settings.SENDER_PASSWORD
User=get_user_model()

    
def estate_details(request, slug):
    try:
        estate = Estate.objects.get(slug=slug)
        # images = Image.objects.filter(mission = mission).order_by('-date_created')
    except:
        print('error')
    context = {'estate':estate}
    return render(request, 'pageListing.html', context)

def signup (request):
    profile_id = request.session.get('ref_profile')
    print('profile_id', profile_id)
    form = UserCreationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user_name = form.cleaned_data['user_name']
            email = form.cleaned_data['email']
            pass1 = form.cleaned_data['pass1']
            pass2 = form.cleaned_data['pass2']
                
            if User.objects.filter(user_name=user_name):
                messages.error(request, 'Username already exists! Please try some other username')
                return redirect('signup')
            
            if User.objects.filter(email=email):
                messages.error(request, "Email already registered")
                return redirect('signup')
            
            if len(user_name) < 1:
                messages.error(request, 'Username must not be under 3 characters')
                return redirect('signup')
                
            if pass1 != pass2:
                messages.error(request, 'Passwords did not match')
                return redirect('signup')
                
            if not user_name.isalnum():
                messages.error(request, 'Username must be Alpha-Numeric')
                return redirect('signup')          

            if profile_id is not None:
                try:
                    recommended_by_profile = Profile.objects.get(id=profile_id)           
                    user = form.save(commit=False)
                    user.set_password(pass2)
                    user.is_active = True
                    user.save()
                    registered_user = User.objects.get(id=user.id)
                    print(registered_user)
                    registered_profile = Profile.objects.get(user=registered_user)
                    registered_profile.recommended_by = recommended_by_profile.user
                    print(recommended_by_profile.user)
                    print(registered_profile.recommended_by)
                    registered_profile.save()
                    print(registered_profile)
                except User.DoesNotExist:
                    print('no user found')
            else:
                print('not working')
                user = form.save(commit=False)
                user.set_password(pass2)
                user.is_active = True
                user.save()
            
            messages.success(request, "Your account have been successfully created")
            return redirect("signin")
    context = {'form':form}
    return render(request, "realtor.html", context)

def signin(request):
    
    if request.method == "POST":
        user_name = request.POST['username']
        pass1 = request.POST['pass1']
        # print(user_name, pass1)
        
        user = authenticate(user_name=user_name, password=pass1)
        print(user)
        if user is not None:
            login(request, user)
            return redirect("dashboard")
        else:
            messages.error(request, "Bad Credentials")
            return redirect('signin')
    return render(request, 'realtor-login.html')

def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully")
    return redirect('home')

# @csrf_protect
def dashboard(request):
    
    user = request.user
    print (user.email)
    profile = Profile.objects.get(user=request.user)
    print (profile)
    my_refs = profile.get_recommended_profiles()
    print(my_refs)
    profile_form = ProfileForm(request.POST or None)
    if request.method == 'POST':
        if profile_form.is_valid():
            update  = profile_form.save()
            update.save()
            print ('saved successfully')
            return redirect('dashboard')
        user_name = request.POST['username']
        full_name = request.POST['full_name']
        email = request.POST['email']
        residential_address = request.POST['address']
        state = request.POST['state_origin']
        account_name = request.POST['account_merchant']
        account_number = request.POST['account_number']
        date_of_birth = request.POST['date_of_birth']
        phone_number = request.POST['phone']
        image = request.POST['image']
        print(image)
        
        create_profile = Profile.objects.create(user_name=user_name, full_name=full_name, email=email, phone_number=phone_number, image=image,
                                                residential_address = residential_address, state=state, account_name=account_name, 
                                                account_number=account_number, date_of_birth=date_of_birth)
        create_profile.save()
        print('saved successfully')
        return redirect("dashboard")
  
    template = "realtor-dashboard.html"
    context = { 'my_refs': my_refs, 'user':user, 'profile':profile, 'profile_form':profile_form }
    # csrfContext = RequestContext(request, context)
    return render(request, template, context)

def update_profile(request, *args, **kwargs):
    pk = str(kwargs.get('pk'))
    profile_form = ProfileForm(request.POST or None)
    profile = Profile.objects.get(user=pk)
    if request.method == 'POST':
        if profile_form.is_valid():
            profile_form.save()
        # user_name = request.POST['username']
        # full_name = request.POST['full_name']
        # email = request.POST['email']
        # residential_address = request.POST['address']
        # state = request.POST['state_origin']
        # account_name = request.POST['account_merchant']
        # account_number = request.POST['account_number']
        # date_of_birth = request.POST['date_of_birth']
        # phone_number = request.POST['phone']
        # image = request.POST['image']
        # print(image)
        
        # create_profile = Profile.objects.create(user_name=user_name, full_name=full_name, email=email, phone_number=phone_number, image=image,
        #                                         residential_address = residential_address, state=state, account_name=account_name, 
        #                                         account_number=account_number, date_of_birth=date_of_birth)
        # create_profile.save()
        print('saved successfully')
        return redirect("dashboard")
    
    context = {'profile_form':profile_form, 'profile':profile}
    template = "profile.html"
    return render(request, template, context)

def home(request, *args, **kwargs):
    code = str(kwargs.get('ref_code'))
    print(code)
    try:
        profile = Profile.objects.get(code=code)
        print(profile)
        request.session['ref_profile'] = profile.id
        print('id', profile.id)
    except:
        pass
    print(request.session.get_expiry_age())
    estates = Estate.objects.all()
    template = 'index.html'
    
    if request.method == "POST":
        message_name = request.POST['name']
        message_email = request.POST['email']
        message_phone_number = request.POST['phone']
        message = request.POST['message']
        subject = f'testing my contact page {message_phone_number}'
        from_email = "okekefrancis112@gmail.com"
        to = [message_email]
        
        # yag = yagmail.SMTP(user=sender_email, password=sender_password)
        
        # yag.send(
        #     #  message_name,
        #     contents = message,
        #     subject = subject,
        #     to = message_email,
        #     #  to = ['okeke98@gmail.com']
            
        # )
        # send_mail( subject, message, "okekefrancis112@gmail.com", [message_email])
        res = send(subject, message, from_email, to)
        # print("mail sent >>> ",send_mail)
        print("mail sent >>> ", res)
        
        context = {'estates':estates, 'message_name':message_name}
        return render(request, template, context)
    else:
        context = {'estates':estates}
        return render(request, template, context) 

# def edit_profile(request):
    
#     if request.method == 'POST':
#         user_name = request.POST['username']
#         full_name = request.POST['full_name']
#         email = request.POST['email']
#         residential_address = request.POST['address']
#         state = request.POST['state_origin']
#         account_name = request.POST['account_merchant']
#         account_number = request.POST['account_number']
#         date_of_birth = request.POST['date_of_birth']
#         phone_number = request.POST['phone']
#         image = request.POST['image']
#         pass1 = request.POST['pass1']
#         pass2 = request.POST['pass2']
        
        
#         if pass1 != pass2:
#             messages.error(request, 'Passwords did not match')
#             return redirect('signup')
        
#     return render(request, '')

# def my_recommendations_view(request):
#     profile = Profile.objects.get(user=request.user)
#     # print (profile)
#     my_recs = profile.get_recommended_profiles()
#     # print(my_recs)
#     context = { 'my_recs': my_recs }
#     return render(request, 'estate/realtor-dashboard.html', context)