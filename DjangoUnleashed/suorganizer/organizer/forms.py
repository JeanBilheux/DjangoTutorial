from django import forms
from django.core.exceptions import ValidationError

from organizer.models import Tag, Startup, NewsLink


#class TagForm(forms.Form):
    
    #name = forms.CharField(max_length = 31)
    #slug = forms.SlugField(max_length = 31, help_text = 'A label for URL config')
    
    #def save(self):
        #new_tag = Tag.objects.create( name = self.cleaned_data['name'],
                                      #slug = self.cleaned_data['slug'])
        #return new_tag
    
    #def clean_name(self):
        #return self.cleaned_data['name'].lower()
    
    #def clean_slug(self):
        #new_slug = self.cleaned_data['slug'].lower()
        #if new_slug == 'create':
            #raise ValidationError('Slug may not be "create"')
        #else:
            #return new_slug

"""Using ModelForm, we can connect the models with the form"""
class TagForm(forms.ModelForm, SlugCleanMixing):
    
    class Meta:
        model = Tag
        fields = '__all__'    
        # fields = ['slug', 'name'] 
        # exclude = tuple()
    
    def clean_name(self):
        return self.cleaned_data['name'].lower()
    
    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()
        if new_slug == 'create':
            raise ValidationError('Slug may not be "create"')
        else:
            return new_slug
    
class StartupForm(forms.ModelForm, SlugCleanMixing):
    
    class Meta:
        model = Startup
        fields = '__all__'
        
class NewsLinkForm(forms.ModelForm):
    
    class Meta:
        model = NewsLink
        fields = '__all__'
        
class SlugCleanMixing:
    
    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()
        if new_slug == 'create':
            raise ValidationError('Slug may not be "create"')
        else:
            return new_slug