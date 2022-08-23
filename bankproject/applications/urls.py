from django.urls import path
from . import views
app_name='applications'
urlpatterns = [
    path('',views.create,name="create"),
    path('ajax/load-branches/', views.load_branches, name='ajax_load_branches'),  # AJAX

]
