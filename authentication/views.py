
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def home(request):
    return render(request, "authentication/index.html")

def signup(request):
    if request.method == "POST":

        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if User.objects.filter(username=username):
            messages.error(request, "Käyttäjänimi on jo olemassa! Kokeile jotain toista käyttäjänimeä")
            return redirect('home')
        
        if User.objects.filter(email=email):
            messages.error(request, "Sähköpostiosoite on jo rekisteröity")
            return redirect('home')
        
        if len(username)>10:
            messages.error(request, "Käyttäjänimen tulee olla lyhyempi kuin 10 merkkiä")

        if pass1 != pass2:
            messages.error(request, "Salasanat eivät täsmänneet!")
        
        if not username.isalnum():
            messages.error(request, "Käyttäjänimen tulee sisältää vain kirjaimia ja numeroita")
            return redirect('home')

            
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname

        myuser.save()

        messages.success(request, "Käyttäjätunnus on luotu onnistuneesti.")

        return redirect('signin')


    return render(request, "authentication/signup.html")

def signin(request):

    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            fname = user.first_name
            return render(request, "authentication/index.html", {'fname': fname})

        else:
            messages.error(request, "Tunnukset eivät toimineet!")
            return redirect('home')

    return render(request, "authentication/signin.html")

def signout(request):
    logout(request)
    messages.success(request, "Kirjauduttu ulos onnistuneesti!")
    return redirect('home')