from django.urls import path
from .views import index, upload_post, category, detail, update, delete, search
urlpatterns =[
    path('', index, name='home'),
    path('upload', upload_post, name='upload'),
    path('category/<str:cats>/', category, name='category' ),
    path('detail/<int:pk>', detail, name='detail'),
    path('update/<int:pk>', update, name='update'),
    path('delete/<int:pk>', delete, name='delete'),
    path('search', search, name='search'),
]