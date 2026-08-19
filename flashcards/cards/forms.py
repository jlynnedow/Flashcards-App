from django import forms

class CardCheckForm(forms.Form):
    card_id = forms.IntegerField(required=True)
    user_answer = forms.CharField(max_length=100, label='User Answer')