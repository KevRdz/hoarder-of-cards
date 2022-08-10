from django.shortcuts import render
from .models import Card
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.views import LoginView

# Create your views here.
class Home(LoginView):
  template_name = 'home.html'

def about(request):
  return render(request, 'about.html')

def cards_index(request):
  cards = Card.objects.all()
  return render(request, 'cards/index.html', {'cards': cards})

def cards_detail(request, card_id):
  card = Card.objects.get(id=card_id)
  return render(request, 'cards/detail.html', {'card': card})

class CardCreate(CreateView):
  model=Card
  fields='__all__'
  success_url='/cards/'

class CardDelete(DeleteView):
  model = Card
  success_url = '/cards/'

class CardUpdate(UpdateView):
  model=Card
  fields = ['name', 'nation', 'position', 'team']