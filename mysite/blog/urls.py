from django.urls import path
from . import views


urlpatterns = [
    path('', views.post_list, name='base'),
    path('<int:year>/<int:month>/<int:day>/<slug:post_slug>/', views.post_detail, name='post_detail')
]