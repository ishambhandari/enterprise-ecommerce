from django import forms
from .models import ShippingAddress

class ShippingAddressForm(forms.ModelForm):
    class Meta:
        model = ShippingAddress
        fields = ['address', 'country']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['address'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter Address'})
        self.fields['country'].widget.attrs.update({'class': 'form-control'})
