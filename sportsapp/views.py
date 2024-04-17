from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Coaches
from .forms import TraineeForm
import os
from django.conf import settings 
from PIL import Image

# Create your views here.
def index(request):
    coaches_list = Coaches.objects.all()


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

def gallery_view(request):
    static_dir = os.path.join(settings.BASE_DIR, 'static')
    image_folder = os.path.join(static_dir, 'sample')  # Change 'images' to the name of your image folder
    image_filenames = [filename for filename in os.listdir(image_folder) if filename.endswith(('.jpg', '.png', '.jpeg'))]
    return render(request, 'gallery.html', {'image_filenames': image_filenames})


def coaches_view(request):
    coaches = Coaches.objects.all()
    context = {'coaches' : coaches}
    return render(request, 'coaches.html', context)