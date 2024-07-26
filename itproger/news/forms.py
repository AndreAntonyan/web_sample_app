from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class ArticlesFrom(ModelForm):
    class Meta:
        model =Articles
        fields = ['title', 'anons', 'full_text', 'date']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Հոդվածի վերնագիրը'
            }),
            "anons": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Հոդվածի հայտարարությունը'
            }),
            "date": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Հրապարակման ամսաթիվը'
            }),
            "full_text":  Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Հոդվածի տեքստ'
            })
        }