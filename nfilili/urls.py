from django.urls import path
from . import views

urlpatterns = [
    path("",views.Index.as_view(),name="index-view"),
    path("form/",views.Form.as_view(),name="form-view"),
    path("form/success/",views.success.as_view(),name="success-view")
]
