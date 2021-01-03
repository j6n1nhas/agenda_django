from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import FormContacto
from checknome_mail import checkmail


# Create your views here.
def login(request):
    """
    View responsável pela apresentação da página de login/autenticação no sistema
    :param request: HTTP request
    :return: HTTPResponse
    """
    if request.method != 'POST':  # se o método utilizado no request for diferente de 'POST'...
        return render(request, 'contas/login.html')  # renderiza o documento login.html passando o request
    # caso contrário, ou seja, se o request for um 'POST':
    utilizador = request.POST.get('utilizador')  # vamos obter o campo 'utilizador' do 'POST'
    senha = request.POST.get('password')  # vamos obter o campo 'password' do 'POST'
    # tenta criar um utilizador que é devolvido pela função authenticate com username e password
    user = auth.authenticate(request, username=utilizador, password=senha)
    if not user:  # se authenticate não for bem sucedida, devolve None
        messages.error(request, 'Login falhou')  # cria uma mensagem de erro que é mostrada na página
        return render(request, 'contas/login.html')  # renderiza o documento 'login.html' passando o request
    else:  # se authenticate for bem sucedida, vai existir um objeto user
        auth.login(request, user)  # faz login do user através da função login(request, username)
        messages.success(request, 'Login com sucesso')
        return redirect('dashboard')


def logout(request):
    """
    View responsável por fazer logout ao utilizador
    :param request: HTTPrequest
    :return:HTTPresponse
    """
    auth.logout(request)
    return redirect('index_login')


def registo(request):
    """
    View responsável por criar o registo de um novo utilizador na base de dados
    :param request: HTTPrequest
    :return: HTTPresponse
    """
    if request.method != 'POST':
        return render(request, 'contas/registo.html')
    nome = request.POST.get('nome')
    apelido = request.POST.get('apelido')
    email = request.POST.get('email')
    utilizador = request.POST.get('utilizador')
    password1 = request.POST.get('password1')
    password2 = request.POST.get('password2')
    if not nome or not apelido or not email or not utilizador or not password1 or not password2:
        messages.error(request, "Nenhum campo pode estar em branco")
        return render(request, 'contas/registo.html')
    if not checkmail(email):
        messages.error(request, "Email inválido")
        return render(request, 'contas/registo.html')
    if len(password1) < 6:
        messages.error(request, 'Password tem de ter pelo menos 6 carateres')
        return render(request, 'contas/registo.html')
    else:
        if password1 != password2:
            messages.error(request, 'Passwords não coincidem')
            return render(request, 'contas/registo.html')
    if len(utilizador) < 6:
        messages.error(request, 'Utilizador tem de ter pelo menos 6 carateres')
        return render(request, 'contas/registo.html')
    else:
        if User.objects.filter(username=utilizador).exists():
            messages.error(request, 'Utilizador já existe')
            return render(request, 'contas/registo.html')
    if User.objects.filter(email=email).exists():
        messages.error(request, 'E-mail já existe')
        return render(request, 'contas/registo.html')
    messages.success(request, 'Utilizador registado com sucesso')
    user = User.objects.create_user(username=utilizador, email=email, password=password1, first_name=nome, last_name=apelido)
    user.save()
    return redirect('login')


@login_required(redirect_field_name='login')
def dashboard(request):
    """
    View responsável por apresentar a dashboard ao utilizador
    :param request: HTTPrequest
    :return: HTTPresponse
    """
    if request.method != 'POST':
        form = FormContacto()
        return render(request, 'contas/dashboard.html', {'form': form})
    form = FormContacto(request.POST, request.FILES)
    if not form.is_valid():
        messages.error(request, 'Erro na validação do formulário')
        form = FormContacto(request.POST)
        return render(request, 'contas/dashboard.html', {'form': form})
    form.save()
    return redirect('dashboard')
