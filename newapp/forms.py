from django.forms import ModelForm
from .models import customer


class CustomerInfoForm(ModelForm):
    class Meta:
        model = customer
        fields = ['name', 'age', 'mobile']
