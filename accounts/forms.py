from typing import Any
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .constrants import GENDER_TYPE,ACCOUNT_TYPE
from .models import UserAddress,UserBankAccount

class UserRegistrationForm(UserCreationForm):
    account_type=forms.ChoiceField(choices=ACCOUNT_TYPE)
    birth_date=forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    gender=forms.ChoiceField(choices=GENDER_TYPE)
    street_address=forms.CharField(max_length=100)
    city=forms.CharField(max_length=100)
    postal_code=forms.IntegerField()
    country=forms.CharField(max_length=100)

    class Meta:
        model = User
        fields=['username','password1','password2','first_name','last_name','email','account_type','birth_date','gender','street_address','city','postal_code','country']
    
    def save(self,commit=True):
        user=super().save(commit=False)
        if commit==True:
            user.save() #user model data save
            account_type=self.cleaned_data.get('account_type')
            gender=self.cleaned_data.get('gender')
            street_address=self.cleaned_data.get('street_address')
            birth_date=self.cleaned_data.get('birth_date')
            city=self.cleaned_data.get('city')
            postal_code=self.cleaned_data.get('postal_code')
            country=self.cleaned_data.get('country')

            UserAddress.objects.create(
                user=user,
                postal_code=postal_code,
                country=country,
                city=city,
                street_address=street_address
            )

            UserBankAccount.objects.create(
                user=user,
                account_type=account_type,
                gender=gender,
                birth_date=birth_date,
                account_no=100000+user.id
            )

        return user
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class':( 
                    'appearance-none block w-full bg-gray-200 '
                    'text-gray-700 border border-gray-200 rounded '
                    'py-3 px-4 leading-tight focus:outline-none '
                    'focus:bg-white focus:border-gray-500')
            })
