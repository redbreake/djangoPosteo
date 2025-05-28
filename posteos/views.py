from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, ListView, DetailView, UpdateView, DeleteView # Importar DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin # Importar UserPassesTestMixin
from django.contrib.auth import get_user_model # Importar get_user_model
from .forms import CustomUserCreationForm
from .models import Post, PageView # Importar el modelo Post y PageView

class LandingPageView(TemplateView):
    template_name = "landing_page.html"

    def get(self, request, *args, **kwargs):
        PageView.objects.create(path=request.path) # Registrar la visita
        return super().get(request, *args, **kwargs)

class PostListView(ListView):
    model = Post
    template_name = "lista_posteos.html" # Plantilla para listar posteos

    def get(self, request, *args, **kwargs):
        PageView.objects.create(path=request.path) # Registrar la visita
        return super().get(request, *args, **kwargs)

    context_object_name = "posteos" # Nombre de la variable en la plantilla
    ordering = ["-fecha_creacion"] # Ordenar por fecha de creación descendente

class AdminStatsView(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    template_name = "admin_stats.html"

    def test_func(self): # Solo permitir acceso a superusuarios
        return self.request.user.is_superuser

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        User = get_user_model()
        context["total_users"] = User.objects.count()
        context["total_posts"] = Post.objects.count()
        context["total_pageviews"] = PageView.objects.count()
        return context

class PostDetailView(DetailView):
    model = Post
    template_name = "detalle_posteo.html" # Plantilla para el detalle del posteo
    context_object_name = "post" # Nombre de la variable en la plantilla

class PostCreateView(LoginRequiredMixin, CreateView): # Requiere que el usuario esté autenticado
    model = Post
    fields = ["titulo", "contenido"] # Campos a incluir en el formulario
    template_name = "formulario_posteo.html" # Plantilla para el formulario
    success_url = reverse_lazy("lista_posteos") # Redirigir a la lista después de crear

    def form_valid(self, form):
        form.instance.autor = self.request.user # Asignar el autor actual al posteo
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView): # Requiere autenticación y pasa un test
    model = Post
    fields = ["titulo", "contenido"]
    template_name = "formulario_posteo.html"
    success_url = reverse_lazy("lista_posteos")

    def test_func(self): # Test para verificar si el usuario es el autor o superusuario
        post = self.get_object()
        return self.request.user == post.autor or self.request.user.is_superuser

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView): # Requiere autenticación y pasa un test
    model = Post
    template_name = "confirmar_eliminar_posteo.html" # Plantilla de confirmación
    success_url = reverse_lazy("lista_posteos") # Redirigir a la lista después de eliminar

    def test_func(self): # Test para verificar si el usuario es el autor o superusuario
        post = self.get_object()
        return self.request.user == post.autor or self.request.user.is_superuser

class RegistroView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("lista_posteos") # Redirigir a la lista de posteos después del registro y login
    template_name = "registration/registro.html" # Usaremos una plantilla en la carpeta registration

    def form_valid(self, form):
        user = form.save()
        login(self.request, user) # Iniciar sesión automáticamente después del registro
        return super().form_valid(form) # Usar la redirección por defecto de CreateView
