from django import forms


class AdvertisementsForm(forms.Form):
    title = forms.CharField(max_length=64)
    description = forms.CharField()
    price = forms.DecimalField()
    auction = forms.BooleanField(required=False)
    image = forms.ImageField(required=False)