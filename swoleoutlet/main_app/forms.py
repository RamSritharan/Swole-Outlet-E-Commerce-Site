from .models import Review
from django import forms

class ReviewCreateForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('content', 'stars')
        labels = {
            "content" : "Review",
            "stars" : "Rating",
        }