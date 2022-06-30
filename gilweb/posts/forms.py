from turtle import textinput
from django import forms
from .models import User_posts
from django.forms import NumberInput, Textarea


class User_postsForm(forms.ModelForm):
    class Meta:
        model = User_posts
        fields = [
            'post_header',
            'game_name',
            'post_text',
            'game_rating',
        ]
        widgets = {
            'post_text': Textarea(attrs={'cols': 80, 'rows': 20}),
            'game_rating': NumberInput
        }