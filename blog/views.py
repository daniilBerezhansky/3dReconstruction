from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView

from blog.forms import PhotoForm
# from django_project import settings
from .models import Post, Photo


def home(request):
    context = {

    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


class Reconstruction(View):
    def get(self, request):
        photos_list = Photo.objects.all()
        return render(self.request, 'blog/reconstruction.html', {'photos': photos_list})

    def post(self, request):
        form = PhotoForm(self.request.POST, self.request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.author = request.user
            photo.save()
            data = {'is_valid': True, 'name': photo.file.name, 'url': photo.file.url}
        else:
            data = {'is_valid': False}
        return JsonResponse(data)