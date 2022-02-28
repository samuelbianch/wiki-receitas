from unicodedata import name
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth, messages
from django.contrib.auth import authenticate, login
from receitasapp.models import Receita

def login(request):
    """Realiza o Login do usuário na aplicação"""
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']
        if email == "" or senha == "":
            messages.error(request, 'O email ou a senha não possuem nenhum valor')
            print("O email ou a senha não possuem nenhum valor")
            return redirect('login')
        print(email, senha)
        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list('username', flat=True).get()
            user = auth.authenticate(request, username=nome, password=senha)
            if user is not None:
                auth.login(request, user)
                messages.success(request, 'Login realizado com sucesso')
                print("Login realizado com sucesso")
                return redirect('dashboard')

    return render(request, 'usuarios/login.html')

def cadastro(request):
    """Cadastra o usuário no banco de dados"""
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['password']
        senha2 = request.POST['password2']
        print(nome, email, senha, senha2)

        if not nome.strip():
            messages.error(request, 'O campo nome não pode estar vazio')
            print("O campo nome não pode estar vazio")
            return redirect('cadastro')
        if not email.strip():
            messages.error(request, 'O campo email não pode estar vazio')
            print("O campo email não pode estar vazio")
            return redirect('cadastro')
        if senha != senha2:
            messages.error(request, 'As senhas não são iguais')
            print("As senhas não são iguais")
            return redirect('cadastro')
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Usuário já existe')
            print("Usuário já existe")
            return redirect('cadastro')
        if User.objects.filter(username=nome).exists():
            messages.error(request, 'O nome de usuário já existe')
            return redirect('cadastro')

        user = User.objects.create_user(username=nome, email=email, password=senha)
        user.save()
        messages.success(request, 'Usuário cadastrado com sucesso')
        return redirect('login')
    else:
        return render(request, 'usuarios/cadastro.html')

def logout(request):
    """Apaga o token e redireciona para a raiz do sistema"""
    auth.logout(request)
    return redirect('index')

def dashboard(request):
    """Exibe as receitas criadas pelo usuário que está logado"""
    if request.user.is_authenticated:
        id = request.user.id
        receita = Receita.objects.order_by('-data_receita').filter(pessoa=id)

        dados = {
            'receitas' : receita
        }
        return render(request, 'usuarios/dashboard.html', dados)
    else:
        return redirect('index')
