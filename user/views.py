from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

def custom_login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('search:index')  # Replace 'search:index' with the URL name of the search homepage
        else:
            # Handle invalid credentials here, e.g., show an error message or redirect back to the login page with a message
            pass

    return render(request, 'login.html')  
# Create a login.html template for the login form
def logout_view(request):
    logout(request)
    return redirect('login')