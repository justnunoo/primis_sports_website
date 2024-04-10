from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import coaches
from .forms import TraineeForm

# Create your views here.
def index(request):
    coaches_list = coaches.objects.all()


    context = { 'coaches_list': coaches_list,
                }
    return render(request, 'index.html', context)


def register_trainee(request):
    if request.method == 'POST':
        form = TraineeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration Successful")
            return redirect('index')  # Redirect to success page
    else:
        form = TraineeForm()
    return render(request, 'register.html', {'form': form})

