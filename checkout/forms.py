from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    """
    This is the order form to allow user to enter details
    """
    class Meta:
        model = Order
        fields = ('full_name', 'email', 'phone_number',
                  'street_address1', 'street_address2', 'postcode',
                  'county',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'county': 'County, State or Locality',
            'postcode': 'Postal Code',
        }

        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False


class CheckoutForm(forms.Form):
    """
    Form for user to enter their card details to make a payment
    """
    MONTH_EXP = [(i, i) for i in range(1, 12)]
    YEAR_EXP = [(i, i) for i in range(2018, 2040)]

    card_number = forms.IntegerField(
        label='Credit card number', required=False)
    cvv = forms.IntegerField(label='Security code (CVV)', required=False)
    expiry_month = forms.ChoiceField(
        label='Month', choices=MONTH_EXP, required=False)
    expiry_year = forms.ChoiceField(
        label='Year', choices=YEAR_EXP, required=False)
    stripe_id = forms.CharField(widget=forms.HiddenInput)
