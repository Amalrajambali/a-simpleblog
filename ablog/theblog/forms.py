
#used to style the form

from django import forms
from .models import Post,Category,Comment

#choices=[('coding','coding'),('sports','sports'),('entertainment','entertainment')]
choices=Category.objects.all().values_list('name','name')
choices_list=[]
for item in choices:
    choices_list.append(item)

#First is defined the things
class Postform(forms.ModelForm):
    class Meta:
        model = Post
        fields =('title','title_tag','author','category','body','snippet','header_image')

#Second is to do actual styling
        widgets = {
        'title': forms.TextInput(attrs={'class':'form-control' }),# atters- change the attributes of that box
        'title_tag': forms.TextInput(attrs={'class':'form-control' }),
        'author': forms.TextInput(attrs={'class':'form-control','value':'','id':'elder','type':'hidden'}),
        #'author': forms.Select(attrs={'class':'form-control'}),
        'category': forms.Select(choices=choices_list,attrs={'class':'form-control'}),
        'body': forms.Textarea(attrs={'class':'form-control'}),
        'snippet': forms.Textarea(attrs={'class':'form-control'}),
        }

#-----------------------for update post-------------------------

class Editform(forms.ModelForm):
    class Meta:
        model = Post
        fields =('title','title_tag','category','body','snippet')

#to do actual styling
        widgets = {
        'title': forms.TextInput(attrs={'class':'form-control' }),
        'title_tag': forms.TextInput(attrs={'class':'form-control' }),
        'author': forms.Select(attrs={'class':'form-control' }),
        'category': forms.Select(choices=choices_list,attrs={'class':'form-control' }),
        'body': forms.Textarea(attrs={'class':'form-control'}),
        'snippet': forms.Textarea(attrs={'class':'form-control'}),

    }

#-----------------------for Add comment-------------------------

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields =('name','body')

#to do actual styling
        widgets = {
        'name': forms.TextInput(attrs={'class':'form-control' }),
        'body': forms.Textarea(attrs={'class':'form-control'}),

 }
