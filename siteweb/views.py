from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.template.loader import get_template
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.conf import settings

# Page d'accueil
class IndexView(TemplateView):
  template_name = 'index.html'

# Tableau des clés
class DashBoardView(TemplateView):
  template_name = 'layouts/dashboard.html'

# Connexion
class LoginView(TemplateView):
  template_name = 'index.html'

  def post(self, request, **kwargs):
    username = request.POST.get('username', False)
    password = request.POST.get('password', False)
    user = authenticate(username=username, password=password)
    if user is not None and user.is_active:
        login(request, user)
        messages.success(request, 'Connexion réussie')
        return HttpResponseRedirect( settings.LOGIN_REDIRECT_URL )
    else:
      messages.error(request, 'Identifiants incorrects')
    return render(request, self.template_name)

# Inscription
class ProfileUpdate(TemplateView):
  def post(self, request, **kwargs):
    if request.POST.get('ln') != '' and request.POST.get('fn') != '' and request.POST.get('mdpactuel') != ''  and request.POST.get('mail') != '': # si la requete n'est pas nulle
      if(request.user.check_password(request.POST.get('mdpactuel'))):
        User.objects.filter(id=request.user.id).update(email = request.POST.get('mail'), first_name = request.POST.get('fn'), last_name = request.POST.get('ln'))
        if(request.POST.get('mdpnouveau') != ''):
          request.user.set_password(request.POST.get('mdpnouveau'))
          request.user.save()
        messages.success(request, 'Profil bien mis à jour')
      else:
        messages.error(request, 'Mauvais mot de passe fourni')
    else:
      messages.error(request, 'Veuillez remplir tous les champs !')
    return HttpResponseRedirect('/dashboard/profile/')
  def get(self, request, **kwargs):
    return render(request, 'layouts/empty.html')
    
# Inscription
class RegisterView(TemplateView):
  def post(self, request, **kwargs):
    if request.POST.get('ln') != '' and request.POST.get('fn') != '' and request.POST.get('mdpactuel') != ''  and request.POST.get('mail') != '': # si la requete n'est pas nulle
      if(request.user.check_password(request.POST.get('mdpactuel'))):
        User.objects.filter(id=request.user.id).update(email = request.POST.get('mail'), first_name = request.POST.get('fn'), last_name = request.POST.get('ln'))
        if(request.POST.get('mdpnouveau') != ''):
          request.user.set_password(request.POST.get('mdpnouveau'))
          request.user.save()
        messages.success(request, 'Profil bien mis à jour')
      else:
        messages.error(request, 'Mauvais mot de passe fourni')
    else:
      messages.error(request, 'Veuillez remplir tous les champs !')
    return HttpResponseRedirect('/dashboard/profile/')
  def get(self, request, **kwargs):
    return render(request, 'layouts/empty.html')

# Déconnexion
class LogoutView(TemplateView):
  template_name = 'index.html'

  def get(self, request, **kwargs):
    logout(request)
    return render(request, self.template_name)