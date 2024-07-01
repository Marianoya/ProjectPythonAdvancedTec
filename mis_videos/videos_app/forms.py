from django import forms
from .models import user_data, videos_data, videos_users, video_number

class UserForm(forms.ModelForm):
    class Meta:
        model = user_data
        fields = ('id_user', 'nombre')

class VideoDataForm(forms.ModelForm):
    class Meta:
        model = videos_data
        fields = ('id_video', 'video_name', 'video_extension', 'video_size', 'video_url')

class VideoUsersForm(forms.ModelForm):
    class Meta:
        model = videos_users
        fields = ('id_video', 'id_user')

class VideoNumberForm(forms.ModelForm):
    class Meta:
        model = video_number
        fields = ('id_user','nombre','numero_de_video')


from django.forms import formset_factory

VideoFormSet = formset_factory(VideoDataForm, extra=1)
