from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.db.models import Q
from vehicles.models import *
from service.models import *
from vehicles.forms import *
from vehicles.serializers import CarSerializer
from django.contrib.auth.mixins import PermissionRequiredMixin
from rest_framework import generics

# Главная
class HomeView(TemplateView):
    template_name = 'index.html'
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('car_list')
        else:
            return redirect('car_search_list')

class CarSearchView(ListView):
    model = Car
    template_name = 'vehicles/car_search.html'
    queryset = Car.objects.all()

class CarListView(LoginRequiredMixin, ListView):
    model = Car
    template_name = 'vehicles/car_list.html'

    def get_queryset(self):
        if not self.request.user.is_staff:
            user = User.objects.get(pk = self.request.user.pk)
            try:
                profile = UserProfile.objects.get(user = user)
                if profile.is_service:
                    return Car.objects.filter(service_company = profile.service_company)
            except:
                return Car.objects.filter(client = user)
        else:
            return Car.objects.all()

class CarDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    permission_required = 'vehicles.view_car'
    model = Car
    template_name = 'vehicles/car_view.html'
    context_object_name = 'obj'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class CarCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'vehicles.add_car'
    model = Car
    form_class = CarForm
    template_name = 'vehicles/car_create.html'
    success_url = reverse_lazy('car_list')

class CarUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'vehicles.change_car'
    model = Car
    form_class = CarForm
    template_name = 'vehicles/car_update.html'
    success_url = reverse_lazy('car_list')

class CarDescriptionView(TemplateView):
    template_name= 'service/modal_description.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        car = Car.objects.get(pk = self.kwargs["pk"])
        atribute = context['atribute']
        if atribute == 'technic':
            context['atribute'] = car.technic
            context['description'] = car.technic.description 
        elif atribute == 'engine':
            context['atribute'] = car.engine
            context['description'] = car.engine.description 
        elif atribute == 'transmission':
            context['atribute'] = car.transmission
            context['description'] = car.transmission.description
        elif atribute == 'driving_bridge':
            context['atribute'] = car.driving_bridge
            context['description'] = car.driving_bridge.description 
        elif atribute == 'controlled_bridge':
            context['atribute'] = car.controlled_bridge
            context['description'] = car.controlled_bridge.description 
        elif atribute == 'equipment':
            context['atribute'] = 'Комплектация'
            context['description'] = car.equipment
        elif atribute == 'service_company':
            context['atribute'] = car.service_company
            context['description'] = car.service_company.description 
        return context

class CarDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = 'vehicles.delete_car'
    model = Car
    template_name_suffix = '_confirm_delete'
    success_url = reverse_lazy('car_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["type"] = 'car'
        return context


# API
class CarListAPI(generics.ListAPIView):
    serializer_class = CarSerializer
    queryset = Car.objects.all()

class CarUserListAPI(generics.ListAPIView):
    serializer_class = CarSerializer
    
    def get_queryset(self):
        try:
            user = int(self.kwargs['user'])
        except:
            user = self.kwargs['user']
        if type(user) == int:
            queryset = Car.objects.filter(client = user)
        elif type(user) == str:
            queryset = Car.objects.filter(client__username = user)
        return queryset

class CarDetailAPI(generics.RetrieveAPIView):
    serializer_class = CarSerializer

    def get_object(self):
        obj = Car.objects.get(pk = self.kwargs['pk'])
        return obj