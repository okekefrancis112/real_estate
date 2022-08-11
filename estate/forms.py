from django import forms
from .models import Profile, NewUser


class UserCreationForm(forms.ModelForm):
    user_name = forms.CharField(label="",required=True, widget=forms.TextInput(attrs={'placeholder':'Username'}))
    full_name = forms.CharField(label="",required=False, widget=forms.TextInput(attrs={'placeholder':'Fullname'}))
    email = forms.EmailField(label="",required=True, widget=forms.EmailInput(attrs={'placeholder':'Email'}))
    state = forms.CharField(label="",required=False, widget=forms.TextInput(attrs={'placeholder':'State'}))
    residential_address = forms.CharField(label="",required=False, widget=forms.TextInput(attrs={'placeholder':'Residential Address'}))
    account_name = forms.CharField(label="",required=False, widget=forms.TextInput(attrs={'placeholder':'Account Merchant'}))
    account_number = forms.IntegerField(label="",required=False, widget=forms.TextInput(attrs={'placeholder':'Account Number'}))
    date_of_birth = forms.DateTimeField(label="",required=True, widget=forms.TextInput(attrs={'placeholder':'Date of birth format 2022-12-12'}))
    phone_number = forms.IntegerField(label="",required=False, widget=forms.TextInput(attrs={'placeholder':'Phone number'}))
    pass1 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder':'Password'}))
    pass2 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder':'Confirm password'}))
    
    class Meta:
        model = NewUser
        fields = ("user_name", 'full_name', 'email', 'residential_address', 'state',
                  'account_name', 'account_number', 'date_of_birth', 
                  'phone_number')

class ProfileForm(forms.ModelForm):
    user_name = forms.CharField(label="Username",required=True, widget=forms.TextInput(attrs={'placeholder':''}))
    full_name = forms.CharField(label="Full name",required=False, widget=forms.TextInput(attrs={'placeholder':''}))
    email = forms.EmailField(label="Email",required=True, widget=forms.EmailInput(attrs={'placeholder':''}))
    state = forms.CharField(label="State of origin",required=False, widget=forms.TextInput(attrs={'placeholder':''}))
    residential_address = forms.CharField(label="Address",required=False, widget=forms.TextInput(attrs={'placeholder':''}))
    account_name = forms.CharField(label="Account merchant",required=False, widget=forms.TextInput(attrs={'placeholder':''}))
    account_number = forms.IntegerField(label="Account number",required=False, widget=forms.TextInput(attrs={'placeholder':''}))
    date_of_birth = forms.DateTimeField(label="Date of birth",required=True, widget=forms.TextInput(attrs={'placeholder':''}))
    phone_number = forms.IntegerField(label="Phone number",required=False, widget=forms.TextInput(attrs={'placeholder':''}))
    
    image = forms.ImageField(label="Image",required=False, widget=forms.TextInput(attrs={'placeholder':''}))
    
    class Meta:
        model = Profile
        fields = ( 'full_name', 'email', 'residential_address', 'state',
                  'account_name', 'account_number', 'date_of_birth', 
                  'phone_number', 'image')
        
# class PaymentForm(forms.ModelForm):  
#     village = forms.ModelChoiceField(queryset=Mission.objects.all(), empty_label="Select a Community", label='')    
#     name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Name'}), label='')
#     email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder':'Email'}), label='')
#     phone_number = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Phone number'}), label='')
#     description = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Description'}), label='')
#     amount = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Amount'}), label='')