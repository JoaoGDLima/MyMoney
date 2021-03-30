from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .models import Lancamento
from .models import Categoria
from .forms import categoryForm
from .forms import accountForm

@login_required
def accountList(request):
    search = request.GET.get('search')

    if search:
        lancamentos = Lancamento.objects.filter(nome__icontains=search, usuario=request.user)
    else:
        lancamentos_list = Lancamento.objects.all().order_by('datahora').filter(usuario=request.user)
        paginator = Paginator(lancamentos_list, 50)

        page = request.GET.get('page')
        lancamentos = paginator.get_page(page)
    
    return render(request, 'account/list.html', {'lancamentos': lancamentos})

@login_required
def newAccount(request):
    if request.method == 'POST' : 
        form =  accountForm(request.POST)

        if form.is_valid():
            lancamento = form.save(commit=False)
            lancamento.usuario = request.user
            lancamento.save()
            return redirect('/lancamentos/')
    else:
        form =  accountForm
        return render(request, 'account/addAccount.html', {'form': form})

@login_required
def editAccount(request, id):
    lancamento = get_object_or_404(Lancamento, pk=id)
    form = accountForm(instance=lancamento)

    if request.method == 'POST' : 
        form = accountForm(request.POST, instance=lancamento)

        if form.is_valid():
            lancamento.save()
            return redirect('/lancamentos/')
        else:
            return render(request, 'account/editAccount.html', {'form': form, 'lancamento': lancamento})  
    else:
        return render(request, 'account/editAccount.html', {'form': form, 'lancamento': lancamento})  

@login_required
def deleteAccount(request, id):
    lancamento = get_object_or_404(Lancamento, pk=id)
    lancamento.delete()
    
    messages.info(request, 'Lançamento deletado com sucesso.')

    return redirect('/lancamentos/')

@login_required
def accountView(request, id):
    lancamento = get_object_or_404(Lancamento, pk=id)
    return render(request, 'account/account.html', {'lancamento': lancamento})

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

