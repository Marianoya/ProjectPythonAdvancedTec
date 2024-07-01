from django.shortcuts import render, redirect, get_object_or_404
from .models import user_data
from .models import videos_users
from .models import videos_data
from .forms import VideoUsersForm
from .forms import UserForm
from .forms import VideoDataForm
from .forms import VideoNumberForm


def video_list(request):    
    videos = videos_data.objects.all()
    users = user_data.objects.all()
    context = {
        'videos': videos,
        'users': users,
    }
    return render(request, 'videos/video_list.html', context)


def video_view(request, pk):
    video = get_object_or_404(videos_data, pk=pk)
    return render(request, 'videos/video_detail.html', {'video': video})

def video_add(request):
    if request.method == "POST":
        form = VideoDataForm(request.POST)
        if form.is_valid():
            video = form.save(commit=False)
            video.save()
            return redirect('video_list')
    else:
        form = VideoDataForm()
    return render(request, 'videos/video_add.html', {'form': form})

def user_registration(request):
    if request.method == "POST":
        form = VideoNumberForm(request.POST)
        if form.is_valid():
            request.session['id_user'] = form.cleaned_data['id_user']
            request.session['nombre'] = form.cleaned_data['nombre']
            request.session['numero_de_video'] = form.cleaned_data['numero_de_video']
            return redirect('confirmacion')  # Redirige a la vista de confirmación
    else:
        form = VideoNumberForm()
    return render(request, 'videos/new_user.html', {'form': form})

def confirmacion(request):
    id_user = request.session.get('id_user')
    nombre = request.session.get('nombre')
    numero_de_video = request.session.get('numero_de_video')
    if 'confirmacion' in request.POST:
            respuesta = request.POST['confirmacion']
            if respuesta == 'si':
                 return redirect('confirmacion_exitosa')
            elif respuesta == 'no':
                 return redirect('video_list')
    return render(request, 'videos/confirmacion.html', {'id_user': id_user, 'nombre': nombre, 'numero_de_video': numero_de_video})

def confirmacion_exitosa(request):
    if request.method == "POST":
        form = VideoDataForm(request.POST)
        if form.is_valid():
            video = form.save(commit=False)
            video.save()
            return redirect('video_list')
    else:
        form = VideoDataForm()
    return render(request, 'videos/confirmacion_exitosa.html', {'form': form})

def video_edit(request, pk):
    video = get_object_or_404(videos_data, pk=pk)
    if request.method == "POST":
        form = VideoDataForm(request.POST, instance=video)
        if form.is_valid():
            video = form.save(commit=False)
            video.save()
            return redirect('video_list')
    else:
        form = VideoDataForm(instance=video)
    return render(request, 'videos/video_edit.html', {'form': form})

def video_delete(request, pk):
    video = get_object_or_404(videos_data, pk=pk)
    video.delete()
    return redirect('video_list')


def user_view(request, pk):
    user = get_object_or_404(user_data, pk=pk)
    return render(request, 'videos/user_detail.html', {'user': user})

def user_add(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect('video_list')
    else:
        form = UserForm()
    return render(request, 'videos/user_add.html', {'form': form})

def user_edit(request, pk):
    user= get_object_or_404(user_data, pk=pk)
    if request.method == "POST":
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect('video_list')
    else:
        form = UserForm(instance=user)
    return render(request, 'videos/user_edit.html', {'form': form})

def user_delete(request, pk):
    user = get_object_or_404(user_data, pk=pk)
    user.delete()
    return redirect('video_list')


