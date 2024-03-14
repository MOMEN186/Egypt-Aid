from django.urls import path 
from . import views

urlpatterns=[
    path("dashboard", views.dashboard, name="dashboard"),
    path("villages",views.get_all_villages, name="villages"),
    path("villages/<int:id>",views.get_village,name="get_village"),
    path("schools",views.get_schools,name="schools"),
    path("medical",views.get_medicals,name="medicals"),
    path("holly_places",views.get_holly_places,name="holly_places"),
    path("infrastructures",views.get_infrastructures,name="infrastructures"),
    path("population",views.get_population,name="population"),
    path("centers",views.get_centers,name="centers"),
    path("public_safety",views.get_public_safety,name="public_safety"),
    path("login",views.login,name="login"),
    path("logout",views.logout,name="logout"),
    path("admin_view",views.admin_view,name="admin_view")
]