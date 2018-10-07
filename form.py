from django import forms
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError
import datetime

class IdForm(forms.Form):
    the_id = forms.IntegerField(label = 'Item Id')

    def cleaned_data(self):
        data = self.cleaned_data['the_id']

        return data


class OrderForm(forms.Form):
    customer_name = forms.CharField(label = 'customer', required = True)
    productNum = forms.IntegerField(validators=[MinValueValidator(1)])
    pickupLoc = forms.CharField(label = 'pickUp', required = True)
    quantity = forms.IntegerField(validators=[MinValueValidator(1)])



    def cleaned_order_data(self):
        quantity = self.cleaned_data['quantity']
        productNum = self.cleaned_data['productNum']
        pickupLoc = self.cleaned_data['pickupLoc']
        customer_name = self.cleaned_data['customer_name']





class CreditCardForm(forms.Form):
    creditCard_num = forms.IntegerField(required = True)
    expirationDate = forms.IntegerField(required = True)
    amount = forms.DecimalField(required = True)
    name = forms.CharField(required = True)


    def clean_card_date(self):
        creditCard_num = self.cleaned_data["creditCard_num"]
        amount = self.cleaned_data["amount"]
        name = self.cleaned_data["name"]
        expirationDate = self.cleaned_data["expirationDate"]
        if expirationDate < datetime.date.today():
            raise ValidationError(_('Card Expire'))
