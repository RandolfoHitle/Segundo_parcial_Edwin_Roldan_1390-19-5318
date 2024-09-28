from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Profesor, Mascota
from .forms import ProfesorForm, MascotaForm
from rest_framework import viewsets, filters
from .serializers import ProfesorSerializer, MascotaSerializer
from rest_framework.permissions import IsAuthenticated

# Vistas para Profesor
class ProfesorListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Profesor
    template_name = 'gestion/profesor_list.html'
    context_object_name = 'profesores'
    permission_required = 'gestion.view_profesor'

class ProfesorCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Profesor
    form_class = ProfesorForm
    template_name = 'gestion/profesor_form.html'
    success_url = reverse_lazy('profesor_list')
    permission_required = 'gestion.add_profesor'

class ProfesorUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Profesor
    form_class = ProfesorForm
    template_name = 'gestion/profesor_form.html'
    success_url = reverse_lazy('profesor_list')
    permission_required = 'gestion.change_profesor'

class ProfesorDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Profesor
    template_name = 'gestion/profesor_confirm_delete.html'
    success_url = reverse_lazy('profesor_list')
    permission_required = 'gestion.delete_profesor'

# Vistas para Mascota
class MascotaListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Mascota
    template_name = 'gestion/mascota_list.html'
    context_object_name = 'mascotas'
    permission_required = 'gestion.view_mascota'

class MascotaCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Mascota
    form_class = MascotaForm
    template_name = 'gestion/mascota_form.html'
    success_url = reverse_lazy('mascota_list')
    permission_required = 'gestion.add_mascota'

class MascotaUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Mascota
    form_class = MascotaForm
    template_name = 'gestion/mascota_form.html'
    success_url = reverse_lazy('mascota_list')
    permission_required = 'gestion.change_mascota'

class MascotaDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Mascota
    template_name = 'gestion/mascota_confirm_delete.html'
    success_url = reverse_lazy('mascota_list')
    permission_required = 'gestion.delete_mascota'






# API 
class ProfesorViewSet(viewsets.ModelViewSet):
    queryset = Profesor.objects.all()
    serializer_class = ProfesorSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['nombre', 'apellido']

class MascotaViewSet(viewsets.ModelViewSet):
    queryset = Mascota.objects.all()
    serializer_class = MascotaSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['nombre', 'raza']
