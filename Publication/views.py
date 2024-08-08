from django.shortcuts import render
from django.shortcuts import render, redirect,  get_object_or_404
from .models import Publication
from .forms import PublicationForm

def create_publication(request):
    if request.method == 'POST':
        form = PublicationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PublicationForm()
    return render(request, 'create_publication.html', {'form': form})

def post_detail(request, pk):
    publication = get_object_or_404(Publication, pk=pk)
    return render(request, 'post_detail.html', {'publication': publication})


def index(request):
    return render(request, 'index.html')



def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def post(request):
    return render(request, 'post.html')