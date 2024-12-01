from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name="index"),
    #path("login/", views.login_user, name="login"),
    path("logout/", views.logout_user, name="logout"),
    
    path("clients/", views.clients, name="clients"),
    path("add_client/", views.add_client, name="add_client"),
    path("client_details/<int:id>", views.client_details, name="client_details"),
    path("update_client/<int:id>", views.update_client, name="update_client"),
    path("delete_client/<int:id>", views.delete_client, name="delete_client"),

    path("cases/", views.cases, name="cases"),
    path("add_case/", views.add_case, name="add_case"),
    path("case_details/<int:id>", views.case_details, name="case_details"),
    path("update_case/<int:id>", views.update_case, name="update_case"),
    path("delete_case/<int:id>", views.delete_case, name="delete_case"),

    path("sittings/", views.sittings, name="sittings"),
    path("case_sittings/<int:id>", views.case_sittings, name="case_sittings"),
    path("add_sitting/<int:id>", views.add_sitting, name="add_sitting"),
    path("sitting_details/<int:id>", views.sitting_details, name="sitting_details"),
    path("update_sitting/<int:id>", views.update_sitting, name="update_sitting"),
    path("delete_sitting/<int:id>", views.delete_sitting, name="delete_sitting"),

    path("appointments/", views.appointments, name="appointments"),
    path("add_appointment/", views.add_appointment, name="add_appointment"),
    path("appointment_details/<int:id>", views.appointment_details, name="appointment_details"),
    path("update_appointment/<int:id>", views.update_appointment, name="update_appointment"),
    path("delete_appointment/<int:id>", views.delete_appointment, name="delete_appointment"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
