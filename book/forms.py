from django import forms
from . models import Author, Book


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name','last_name','nationality'] #campos que contiene el modelo
        
        labels = {
            'name': 'Nombre del autor',
            'last_name': 'Apellidos del autor',
            'nationality': 'Nacionalidad del autor'
        }
        #labels para cada campo del modelo

        widgets = {
            'name': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el nombre del autor',
                    'id':'nombre'
                }
            ),
            
            'last_name': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese los apellidos del autor',
                    'id':'apellidos'
                }
            ),

            'nationality': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder': 'Ingrese la nacionalidad del autor',
                    'id':'nacionalidad'
                }
            )

        }
    #class - da estilo bootstrap
    #placeholder - pone el placeholder de html
    #id- pone el id que normalmente ponemos en html


class BookForm(forms.ModelForm):
    def __init__(self, *args, **kwargs): 
        super(BookForm,self).__init__(*args, **kwargs)
        self.fields['author_id'].queryset = Author.objects.filter(state = True)
    class Meta:
        model = Book
        fields = ['title','author_id','publication_date'] #campos que contiene el modelo
        
        labels = {
            'title': 'Titulo del Libro',
            'author_id': 'Selecciona un Autor',
            'publication_date': 'fecha'
        }
        #labels para cada campo del modelo

        widgets = {
            'title': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el titulo del libro',
                    'id':'titulo'
                }
            ),
            

            'author_id': forms.RadioSelect(
                attrs = {
                    # 'class':'form-check'
                    'id':'autor'
                }
            ),

            'publication_date': forms.SelectDateWidget()

        }    
