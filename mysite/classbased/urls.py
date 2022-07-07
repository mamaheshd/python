from classbased import views
from django.contrib import admin
from django.urls import path,include
urlpatterns = [
    path('admin/', admin.site.urls,name='admin'),
    path('',views.LaptopListView.as_view(),name="Laptop-list"),
    #path('<int:pk>/update', views.BookUpdateView.as_view(), name='book-update'),
    #path('<int:pk>/delete', views.BookDeleteView.as_view(), name='book-delete'),
    #path('detail/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('create',views.LaptopCreateView.as_view(),name='Laptop-create'),
    path('<int:pk>/update',views.LaptopsUpdateView.as_view(),name='Laptop-updates'),
    path( '<int:pk>/delete',views.LaptopDeleteViews.as_view(),name='Laptop-delete'),
]