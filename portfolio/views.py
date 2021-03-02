from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.http import FileResponse, Http404
from . import github
from .forms import VisitorContactForm

def home(request):
    repos = github.get_repos()
    git_data = []

    for repo in repos:
        if repo['stargazers_count'] > 1:
            git_data.append(github.filter_repo(repo))

        if len(git_data) == 8:
            break
    
    git_data = github.add_image(git_data)

    if request.method == 'POST':
        form = VisitorContactForm(request.POST)
        if form.is_valid():
            form.save()
            form.send_email()
            messages.success(request, f'Thanks for Reaching out I will be contacting back soon!')
            return redirect('home')
        else:
            messages.warning(request, f'Information entered is incorrect! Please try again.')
    else:
        form = VisitorContactForm()
    
    context ={
        'git_repos' : git_data,
        'form': form,
    }

    return render(request, 'portfolio/index.html', context=context)

def resume_view(request):
    try:
        return FileResponse(open('resume.pdf', 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        raise Http404()

def projetcs(request):
    repos = github.get_repos()
    git_data = []

    for repo in repos:
        git_data.append(github.filter_repo(repo))
    
    print(len(git_data))

    context={
        'projects': git_data,
    }

    return render(request, 'portfolio/projects.html', context=context)

def blog(request):
    return render(request, 'portfolio/blog.html')

def contact(request):

    if request.method == 'POST':
        form = VisitorContactForm(request.POST)
        if form.is_valid():
            form.save()
            form.send_email()
            messages.success(request, f'Thanks for Reaching out I will be contacting back soon!')
            return redirect('contact')
        else:
            messages.warning(request, f'Information entered is incorrect! Please try again.')
    else:
        form = VisitorContactForm()

    return render(request, 'portfolio/contact.html', context={'form': form})

def error404(request, exception):
    return render(request, 'portfolio/error_404.html')