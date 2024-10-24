from .models import Review
from django import forms

class ReviewForm(forms.ModelForm):
    class Meta:
        madel = Review
        fields = ['review', 'book']