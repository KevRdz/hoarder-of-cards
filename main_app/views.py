from django.shortcuts import render, redirect
from .models import Card
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
class Home(LoginView):
  template_name = 'home.html'

def about(request):
  return render(request, 'about.html')

def cards_index(request):
  cards = Card.objects.all()
  return render(request, 'cards/index.html', {'cards': cards})

class CardCreate(CreateView):
  model= Card
  fields='__all__'
  success_url='/cards/'

  def from_valid(self, form):
    form.instance.user= self.request.user
    return super().form_valid(form)

def cards_detail(request, card_id):
  card = Card.objects.get(id=card_id)
  return render(request, 'cards/detail.html', {'card': card})


class CardDelete(DeleteView):
  model = Card
  success_url = '/cards/'

class CardUpdate(UpdateView):
  model= Card
  fields = ['name', 'nation', 'position', 'team']


def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('cards_index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message':
  error_message}
  return render(request, 'signup.html', context)