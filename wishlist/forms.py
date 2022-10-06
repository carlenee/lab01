from django import forms

from .models import *

class WishlistForm(forms.ModelForm):
    title= forms.CharField(widget= forms.TextInput())
    harga = forms.IntegerField(widget= forms.TextInput())
    description= forms.CharField(widget=forms.Textarea(attrs={'style': 'width: 15em;'}))

    class Meta:
        model = BarangWishlist
        fields = ('title', 'harga', 'description')