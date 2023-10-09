from django.shortcuts import render,  get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Project
from .forms import QuantityForm



def paginat(request, list_objects, per_page=20):  
    p = Paginator(list_objects, per_page)
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)
    except PageNotAnInteger:
        page_obj = p.page(1)
    except EmptyPage:
        page_obj = p.page(p.num_pages)
    return page_obj



def home_page(request):
    projects = Project.objects.all()
    context = {'projects': paginat(request, projects)}
    return render(request, 'home_page.html', context)


def project_detail(request, slug):
    form = QuantityForm()
    project = get_object_or_404(Project, slug=slug)
    first_category = project.category.first()
    related_projects = Project.objects.filter(category=first_category).exclude(slug=slug)[:5]

    context = {
        'title': project.title,
        'project': project,
        'form': form,
        'related_projects': related_projects
    }

    return render(request, 'project_detail.html', context)

def search(request):
    query = request.GET.get('q')
    if query:
        projects = Project.objects.filter(title__icontains=query).all()
    else:
        projects = []  
    context = {'projects': paginat(request, projects)}
    return render(request, 'home_page.html', context)

