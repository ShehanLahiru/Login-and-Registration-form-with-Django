from django import forms
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


class UserRegistrationForm(forms.ModelForm):
    username = forms.CharField(max_length=56)
    email = forms.CharField(max_length=56)
    password = forms.CharField(widget=forms.PasswordInput,max_length=76)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta():
        model= User
        fields =['username','email','password','confirm_password']

    def clean_username(self):
        user = self.cleaned_data['username']
        try:
            match = admin.objects.get(username = user)
        except:
            return self.cleaned_data['username']
        raise forms.ValidationError("Username already exist")

    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            mt = validate_email(email)
            #match = admin.objects.get(email = email)
        except:
            return forms.ValidationError("Email is not in correct format")
        return email

    def clean_confirm_password(self):
        pas=self.cleaned_data['password']
        cpas=self.cleaned_data['confirm_password']
        MIN_LENGTH = 8
        if pas and cpas:
            if pas != cpas:
                raise forms.ValidationError("password and confirm password not matched")
            else:
                if len(pas) < MIN_LENGTH:
                    raise forms.ValidationError("password should contain atleast 8 characters")
                if pas.isdigit():
                    raise forms.ValidationError("password should not all numeric")



class UserLoginForm(forms.Form):

    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self,*args,**kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username,password=password)
            if not user:
                raise forms.ValidationError("This user does not exist")
            if not user.check_password(password):
                raise forms.ValidationError("Incorrect Password")   
            if not user.is_active:
                raise forms.ValidationError("This user is not active") 

        return super(UserLoginForm,self).clean(*args,**kwargs)    



   


