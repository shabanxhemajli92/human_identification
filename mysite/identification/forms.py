from django import forms
from .models import Human

class HumanForm(forms.ModelForm):
    class Meta:
        model = Human
        fields = ['full_name', 'dob', 'address', 'nationality', 'residency', 'bank_account', 'payment_methods', 'cell_phone_provider', 'car_info', 'registration_plate', 'criminal_record', 'photo']