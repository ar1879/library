from distutils.log import error
from sre_parse import State
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect, render
from django.urls import reverse_lazy

from .forms import AuthorForm, BookForm
from .models import Author, Book
from django.views.generic import TemplateView, ListView,UpdateView,CreateView,DeleteView
# Create your views here.

def home(request):
    return render(request, 'index.html')


""" 1.dispatch(): valida la peticion y elige que metodo http se utiliza para la solicitud
2.http_method_not_allowed(): retorna un error cuando se utiliza un metodo HTTP no soportado o definido
3.options()   

estos 3 pasos se utilizan por defecto al utilizar views"""

class Inicio(TemplateView):
    template_name = 'index.html'#asi definimos el template que queremos renderizar


#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////


class AuthorList(ListView):
    model = Author
    template_name = 'book/author/listar_autor.html'
    queryset = Author.objects.filter(state = True)
    context_object_name = 'authors' #nombre del contexto, por defecto es = object_list

#la vista basada en clases anterior se sustitullo por la vista basada en funciones de abajo
""" def authorList(request):
    authors = Author.objects.filter(state = True)  
    return render(request, 'book/listar_autor.html', {'authors':authors})  """   


#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
class UpdateAuthor(UpdateView):
    model = Author
    template_name = 'book/author/crear_autor.html'    
    form_class = AuthorForm
    success_url = reverse_lazy('listar_autor')
    # context_object_name = 'author_form'(quize pasarlo a este otro context pero no funciono)
    #el context_object_name por defecto sera = form

    """ def editAuthor(request,id):
    author_form = None
    error = None
    try:
        author = Author.objects.get(id = id)
        if request.method == 'GET':
            author_form = AuthorForm(instance=author)
        else:
            author_form = AuthorForm(request.POST, instance=author)   
            if author_form.is_valid():
                author_form.save()     
            return redirect('index')   

    except ObjectDoesNotExist as e:
        error = e
    return render(request, 'book/crear_autor.html', {'author_form':author_form,'error':error})  """  


#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
class CreateAuthor(CreateView):
    model = Author
    form_class = AuthorForm
    template_name = 'book/author/crear_autor.html'
    success_url = reverse_lazy('listar_autor')
#la vista basada en clases anterior se sustitullo por la vista basada en funciones de abajo
""" def createAuthor(request):
    if request.method == 'POST':
        author_form = AuthorForm(request.POST)         
        if author_form.is_valid():
            author_form.save()
            return redirect('index')

    else:
        author_form = AuthorForm() 
        # print(author_form)           
    return render(request, 'book/crear_autor.html', {'author_form':author_form})  """       


#**************************************************************************************************************
class DeleteAuthor(DeleteView):
    model = Author

    # success_url = reverse_lazy('listar_autor') aqui no se puede utilizar reverse_lazy por que estamos modificando el metodo post usando la funcion de abajo

    def post(self,request,pk,*args,**kwargs):
        object = Author.objects.get(id=pk)
        object.state = False
        object.save()
        return redirect('listar_autor')

#la vista basada en clases anterior se sustitullo por la vista basada en funciones de abajo
""" def deleteAuthor(request,id):
    author = Author.objects.get(id=id)
    # if request.method == 'POST':
    author.state = False
    author.save()
    return redirect('listar_autor')
            
    return render(request, 'book/eliminar_autor', {'author':author}) """




          


class BookList(ListView):
    model = Book
    template_name = 'book/books/book_list.html'
    # queryset = Book.objects.filter(state=True)
    # esta consulta si no la ponemos se implementa por defecto pero de la sig manera: queryset = Book.objects.all()
    context_object_name ='book' # este por defecto sera object_list


class CreateBook(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'book/books/create_book.html'
    success_url = reverse_lazy('book_list')
    

class DeleteBook(DeleteView):
    model = Book
    def post(self,request,pk,*args,**kwargs):
        object = Book.objects.get(id=pk)
        object.delete()
        return redirect('book_list')


class UpdateBook(UpdateView):
    model = Book
    template_name = 'book/books/create_book.html'
    form_class = BookForm
    success_url = reverse_lazy('book_list')
