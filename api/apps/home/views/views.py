from django.views.generic import TemplateView

# Create your views here.
class HomeTemplateView(TemplateView):
    
    template_name = 'home.html'

class ContatoTemplateView(TemplateView):
    template_name = 'contato.html'