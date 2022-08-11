from django import forms


INPUT_CLASSES = 'border-2 border-solid border-slate-300'

class SignupForm(forms.Form):
    email = forms.EmailField(
        required=True,
        widget=forms.TextInput(attrs={'class': INPUT_CLASSES})
    )
    full_name = forms.CharField(
        required=True,
        max_length=9000,
        widget=forms.TextInput(attrs={'class': INPUT_CLASSES})
    )
