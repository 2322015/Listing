from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from .models import good
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import ListingForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required




class ListingSuccessView(TemplateView):
    template_name='Listing_success.html'


class IndexView(ListView):
    template_name='home.html'

# Create your views here.
class goodsListView(ListView):
    template_name = 'home.html' #表示したいHTML
    context_object_name = 'goods'
    model=good



@method_decorator(login_required, name='dispatch')
class CreateListingView(CreateView):
    form_class= ListingForm
    template_name="Listing.html"
    success_url=reverse_lazy('shop:listing_done')
    def form_valid(self, form):
        Listing=form.save(commit=False)
        Listing.user= self.request.user
        Listing.save()
        return super().form_valid(form)
    

