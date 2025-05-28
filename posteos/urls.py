from django.urls import path, include
from django.urls import path, include
from .views import RegistroView, LandingPageView, PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, AdminStatsView

urlpatterns = [
    path("", LandingPageView.as_view(), name="landing_page"), # URL para la landing page
    path("registro/", RegistroView.as_view(), name="registro"),
    path("posteos/", PostListView.as_view(), name="lista_posteos"), # URL para listar posteos
    path("posteos/<int:pk>/", PostDetailView.as_view(), name="detalle_post"), # URL para ver detalle de posteo
    path("posteos/nuevo/", PostCreateView.as_view(), name="crear_post"), # URL para crear nuevo posteo
    path("posteos/<int:pk>/editar/", PostUpdateView.as_view(), name="editar_post"), # URL para editar posteo
    path("posteos/<int:pk>/eliminar/", PostDeleteView.as_view(), name="eliminar_post"), # URL para eliminar posteo
    # path("admin/stats/", AdminStatsView.as_view(), name="admin_stats"), # URL para estadísticas de administración (Movida a urls.py principal)
    # Las URLs de autenticación de Django ya están incluidas en el urls.py principal
    # path("accounts/", include("django.contrib.auth.urls")), # Esto ya está en el urls.py principal
]