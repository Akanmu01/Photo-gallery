from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import *
from django.contrib.auth.models import User
from .forms import *
from django.template.defaultfilters import slugify
from taggit.models import Tag


def home(request):
    uploads = Upload.objects.all()
    common_tags = Upload.tags.most_common()[:4]
    context = {
        'uploads':uploads,
        'common_tags':common_tags,
    }
    return render(request, 'index.html', context)


def contact(request):
    return render(request, 'contact.html')



@login_required
def upload(request):
    form = UploadForm(request.POST,request.FILES)
    if request.method == "POST":
        if form.is_valid():
            upload = form.save(commit=False)
            upload.slug = slugify(upload.title)
            upload.author = request.user
            upload.save()
            form.save_m2m()
            return redirect('/')
    else:
        form = UploadForm()
    return render(request, 'upload.html', {'form': form})



def detail(request, slug):
    upload = get_object_or_404(Upload, slug=slug)
    common_tags = Upload.tags.most_common()[:4]
    context = {
        'upload':upload,
        'common_tags':common_tags,
    }
    return render(request, 'detail.html', context)



def tagged(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    common_tags = Upload.tags.most_common()[:4]
    uploads = Upload.objects.filter(tags=tag)
    context = {
        'tag':tag,
        'common_tags':common_tags,
        'uploads':uploads,
    }
    return render(request, 'tag.html', context)
