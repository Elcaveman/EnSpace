from django.urls import path
from . import views

app_name = 'library'
urlpatterns = [
    path('', views.library_home_view , name='library_home'),
    path('<int:item_id>/', views.library_item , name="item_detail")
]
