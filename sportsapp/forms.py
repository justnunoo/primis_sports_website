from django import forms
from django.contrib.auth.models import User
from .models import Trainees


class TraineeForm(forms.ModelForm):
    class Meta:
        model = Trainees
        fields = ['firstName', 'lastName', 'email', 'phoneNumber', 'residence', 'birthday', 'sports']

        widgets = {
            'birthday': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'sports': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(TraineeForm, self).__init__(*args, **kwargs)
        # Add Bootstrap classes to form fields
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})

# class RegisterForm(forms.Form):
#     username = forms.CharField(max_length=30)
#     email = forms.EmailField()
#     password1 = forms.CharField(label="Password ",widget=forms.PasswordInput())
#     password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput())
    

#     def clean_password2(self):
#         password1 = self.cleaned_data.get("password1")
#         password2 = self.cleaned_data.get("password2")
#         if password1 and password2:
#             if password1 != password2:
#                 raise forms.ValidationError("Passwords do not match")
#             return password2 

#     def clean_username(self):
#         user = User.objects.filter(
#             username__iexact=self.cleaned_data["username"]
#         ).first()
#         if user:
#             raise forms.ValidationError("Username already exists")
#         return self.cleaned_data["username"]

#     def save(self, commit=True):
#         # Create a new user with the given details
#         user = User.objects.create_user(
#             username=self.cleaned_data['username'],
#             email=self.cleaned_data['email'],
#             password=self.cleaned_data['password1']
#         )
#         # Optionally, you can save the IP address if you have a 'last_login_ip' field in your user model.
#         # user.last_login_ip = request.META['REMOTE_ADDR']
#         if commit:
#             user.save()
#         return user
