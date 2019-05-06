from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class MyRegistrationForm(UserCreationForm):
	email=forms.EmailField(required=True)
	first_name=forms.TextInput()
	last_name=forms.TextInput()
	
	class Meta:
		model=User
		fields=('username','first_name','last_name','email','password1','password2')

	def save(self,commit=True):
		user=super(UserCreationForm,self).save()
		user.set_password(self.cleaned_data['password1'])
		user.set_password(self.cleaned_data['password2'])
		user.first_name=self.cleaned_data['first_name']
		user.last_name=self.cleaned_data['last_name']
		user.email=self.cleaned_data['email']

		if commit:
			user.save()
		return user	
		
class ContactForm(forms.Form):
	full_name = forms.CharField(required=True)
	email = forms.EmailField(required=True)
	message = forms.CharField(widget=forms.Textarea,required=True)