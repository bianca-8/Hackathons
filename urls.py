from django.urls import path,include
from mymemento_app import views
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('add-memento/', views.addMemento, name='add-memento'),
    path('profile/', views.profile, name='profile'),
    path('memento/<int:id>', views.memento, name='memento'),
    path('login/', views.signin, name="login"),
    path('logout/', views.signout, name='logout'),
    path('register/', views.register, name='register'),
    path('delete-memento/<int:id>', views.delete_memento, name='delete-memento'),
    path('edit-memento/<int:memento_id>/', views.edit_memento, name='edit_memento'),

    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()