from django.contrib.auth.models import AbstractUser
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .forms import CreateUserForm
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError
from .forms import FormContactForm




# Create your views here.

#The home view page 

@login_required(login_url='login')
def home_view(request):
    context = {}
    
    return render(request,'home.html', context)

#end of home view page




#The Login in view page
def loginpage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('home')

            else:
                messages.info(request,'Username or Password is correct Incorrect')
                
        
        my_context = {}
        return render(request,'accounts/login.html', my_context)
  
#End of the Login view page



#Start of the logout page

def logoutUser(request):
    logout(request)
    return redirect('login')

#Ther Registration view page

def registrationform(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    else:
        form = CreateUserForm()
        
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()

                messages.success(request , "Account Successfully created  Please login" )
                
                return redirect('login')
            
        return render(request, 'accounts/register.html', {'form':form})




#Contact Form
def contact(request):
	if request.method == 'POST':
		form = FormContactForm(request.POST)
		if form.is_valid():
			subject = "Website Inquiry" 
			body = {
			'first_name': form.cleaned_data['first_name'], 
			'last_name': form.cleaned_data['last_name'], 
			'email': form.cleaned_data['email'], 
			'phone': form.cleaned_data['phone'], 
			'address': form.cleaned_data['address'], 
			'message':form.cleaned_data['message'], 
			}
        
			message = "\n".join(body.values())
    
			try:
				send_mail(subject, message, 'bbjulius@gmail.com', ['bbjulius4@gmail.com ']) 
			except BadHeaderError:
				return HttpResponse('Invalid header found.')
			return redirect ("thankyou")
      
	form = FormContactForm()
	return render(request, "contact.html", {'form':form})


def Thankyoupage(request):
    thankyou_context = {}
    return render(request, "thankyou.html", thankyou_context)


        
# def showform(request):
#     form = FormContactForm(request.POST or None)
#     if form.is_valid():
#         form.save()
        
#     form_context = {'form':form}
    
#     return render(request,'secondcontactform.html', form_context)



