from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente
from .forms import ClienteForm


@login_required
def lista_clientes(request):
    clientes = Cliente.objects.all().order_by("nome")
    return render(
        request,
        "clientes/lista.html",
        {"clientes": clientes},
    )


@login_required
def criar_cliente(request):
    form = ClienteForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("lista_clientes")

    return render(
        request,
        "clientes/formulario.html",
        {"form": form, "titulo": "Cadastrar cliente"},
    )


@login_required
def editar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    form = ClienteForm(request.POST or None, instance=cliente)

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("lista_clientes")

    return render(
        request,
        "clientes/formulario.html",
        {"form": form, "titulo": "Editar cliente"},
    )


@login_required
def excluir_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)

    if request.method == "POST":
        cliente.delete()
        return redirect("lista_clientes")

    return render(
        request,
        "clientes/confirmar_exclusao.html",
        {"cliente": cliente},
    ) 