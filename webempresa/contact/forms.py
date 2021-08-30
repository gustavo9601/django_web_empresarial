from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(label='Nombre', max_length=100, min_length=1, required=True, widget=forms.TextInput(attrs={
        'class' : 'form-control'
    }))
    email = forms.EmailField(label='Email', required=True, widget=forms.EmailInput(attrs={
        'class' : 'form-control'
    }))
    content = forms.CharField(label='Contenido', max_length=500, required=True, widget=forms.Textarea(attrs={
        'class' : 'form-control',
        'rows' : 3
    }))
