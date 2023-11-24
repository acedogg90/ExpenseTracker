from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from .models import Book
import plotly.express as px

# Create your views here.
def index(request):
    books = Book.objects.all



    # Check to see if logging in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in!")
            return redirect('index')
        else:
            messages.success(request, "There was an error logging in, please try again...")
            return redirect('index')
    else:
        return render(request, 'index.html', {'books':books})



def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out!")
    return redirect('index')
    

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and login
            username = form.cleaned_data['username']
            password =  form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You have successfully registered!! Welcome!!")
            return redirect('index')
    
    else:
            form = SignUpForm()
            return render(request, 'register.html', {'form':form})
    
    return render(request, 'register.html', {'form':form})

def login(request):
    return render(request, "login.html", {})

def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out!")
    return redirect('index')

def chart(request):
    expenses = Book.objects.all()
    
    fig = px.bar(
        #  chart,
         x='published_date', 
         y='distribution_expense', 
         color='category', 
         title='Book Distribution Expenses',
         )

    chart = fig.to_html(full_html=False, default_height=500, default_width=700)

    context = {'chart': chart}
    return render(request, 'chart.html', context)

def book_list(request, id):
    if request.user.is_authenticated:
        # look up records
        books = Book.objects.all.get(pk=id)
        return render(request, 'book_list.html', {'books':books})
    else:
        messages.success(request, "You must be logged in to view that page...")
        return redirect('index')

def add_book(request, id):
    if request.user.is_authenticated:
        # look up records
        customer_record = Book.objects.get(pk=id)
        return render(request, 'book_list.html', {'customer_record':customer_record})
    else:
        messages.success(request, "You must be logged in to view that page...")
        return redirect('index')
    
def delete_book(request, id):
    if request.user.is_authenticated:
        # look up records
        customer_record = Book.objects.get(pk=id)
        customer_record.delete()
        return redirect('book_list')
    else:
        messages.success(request, "You must be logged in to view that page...")
        return redirect('index')
    
def update_book(request, id):
    if request.user.is_authenticated:
        # look up records
        customer_record = Book.objects.get(pk=id)
        return render(request, 'book_list.html', {'customer_record':customer_record})
    else:
        messages.success(request, "You must be logged in to view that page...")
        return redirect('index')