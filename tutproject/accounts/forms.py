from django import forms
from django.contrib.auth.models import User

from django.core.exceptions import ValidationError



class registerFormModel(forms.ModelForm):

    class Meta : 
        model = User
        fields = ('username','email','password','first_name','last_name')


    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user














# class customForms(forms.ModelForm):
#     error_messages = {
#         'password_mismatch': 'عدم تطابق پسورد',
#     }
#     password1 = forms.CharField(
#         label="Password",
#         strip=False,
#         widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        
#     )
#     password2 = forms.CharField(
#         label="Password confirmation",
#         widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
#         strip=False,
        
#     )
#     class Meta : 
#         model = User
#         fields = ('username','email','first_name',)
    

#     def clean_password2(self):
#         password1 = self.cleaned_data.get("password1")
#         password2 = self.cleaned_data.get("password2")
#         if password1 and password2 and password1 != password2:
#             raise ValidationError(
#                 self.error_messages['password_mismatch'],
#                 code='password_mismatch',
#             )
#         return password2



#     def save(self, commit=True):
#         user = super().save(commit=False)
#         user.set_password(self.cleaned_data["password1"])
#         if commit:
#             user.save()
#         return user