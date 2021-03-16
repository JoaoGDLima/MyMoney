from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .models import Lancamento
from .models import Categoria
from .forms import categoryForm

@login_required
def accountList(request):
    lancamentos = Lancamento.objects.all()
    return render(request, 'account/list.html', {'lancamentos': lancamentos})

@login_required
def categoryList(request):
    search = request.GET.get('search')

    if search:
        categorias = Categoria.objects.filter(nome__icontains=search, usuario=request.user)
    else:
        categorias_list = Categoria.objects.all().order_by('nome').filter(usuario=request.user)
        paginator = Paginator(categorias_list, 50)

        page = request.GET.get('page')
        categorias =paginator.get_page(page)
        
    return render(request, 'category/list.html', {'categorias': categorias})

@login_required
def newCategory(request):
    if request.method == 'POST' : 
        form =  categoryForm(request.POST)

        if form.is_valid():
            categoria = form.save(commit=False)
            categoria.usuario = request.user
            categoria.save()
            return redirect('/categorias/')
    else:
        form =  categoryForm
        return render(request, 'category/addCategory.html', {'form': form})

@login_required
def editCategory(request, id):
    categoria = get_object_or_404(Categoria, pk=id)
    form = categoryForm(instance=categoria)

    if request.method == 'POST' : 
        form = categoryForm(request.POST, instance=categoria)

        if form.is_valid():
            categoria.save()
            return redirect('/categorias/')
        else:
            return render(request, 'category/editCategory.html', {'form': form, 'categoria': categoria})  
    else:
        return render(request, 'category/editCategory.html', {'form': form, 'categoria': categoria})  

@login_required
def deleteCategory(request, id):
    categoria = get_object_or_404(Categoria, pk=id)
    categoria.delete()
    
    messages.info(request, 'Categoria deletada com sucesso.')

    return redirect('/categorias/')

@login_required
def categoryView(request, id):
    categoria = get_object_or_404(Categoria, pk=id)
    return render(request, 'category/category.html', {'categoria': categoria})

def helloWorld(request):
    return HttpResponse('Hello World!')

