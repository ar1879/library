from django.contrib.auth.forms import AuthenticationForm

class FormularioLogin(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(FormularioLogin, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control' #dando clase form-control de bootstrap al campo username
        self.fields['username'].widget.attrs['placeholder'] = 'Nombre de Usuario' #poniendo un place holder al campo username
        
        
        
        self.fields['password'].widget.attrs['class'] = 'form-control' #dando clase form-control de bootstrap al campo password
        self.fields['password'].widget.attrs['placeholder'] = 'Contraseña' #poniendo un place holder al campo password

        