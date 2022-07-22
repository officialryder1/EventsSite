from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Post, Category


# choices = Category.objects.all().values_list('name','name')

# choice_list = []

# for item in choices:
#     choice_list.append(item)
# try:
#     cat_choices = Category.objects.all().values_list('name','name')
# except (OperationalError, ProgrammingError) as e:
#     cat_choices=[]

class AddPost(forms.ModelForm):

    
    class Meta:
        model = Post
        fields = ('title', 'author', 'description', 'category', 'location', 'date')
    
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Event Title'}),
            'author':forms.Select(attrs={'class':'form-control', 'placeholder':'Author'}),
            'description':forms.Textarea(attrs={'class':'form-control', 'placeholder':'Description'}),
            'category':forms.Select(attrs={'class':'form-control', 'placeholder':'Category'}),
            'location':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Location'}),
            'date':forms.SelectDateWidget(attrs={'class':'form-control', 'placeholder':'Date'})
        }