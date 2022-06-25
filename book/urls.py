

from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views

# app_name = 'book'

urlpatterns = [
   
    path('crear_autor/',login_required(views.CreateAuthor.as_view()) , name = 'crear_autor'),
    path('listar_autor/',login_required(views.AuthorList.as_view()) , name = 'listar_autor'),
    path('editar_autor/<int:pk>', login_required(views.UpdateAuthor.as_view()), name = 'editar_autor'),
    path('borrar_autor/<int:pk>', login_required(views.DeleteAuthor.as_view()), name = 'eliminar_autor'),
    path('listar_libro/', login_required(views.BookList.as_view()), name = 'book_list'),
    # path('registrar_libro/', login_required(views.CreateBook.as_view()), name = 'create_book'),
    path('eliminar_libro/<int:pk>', login_required(views.DeleteBook.as_view()), name = 'delete_book'),
    path('editar_libro/<int:pk>', login_required(views.UpdateBook.as_view()), name = 'update_book'),

    

    
    
    
    
    
    
]
