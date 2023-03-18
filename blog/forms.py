from django import forms

from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ["post"]
        labels = {
            "user_name": "Vaše jméno",
            "user_email": "Váš email",
            "text": "vložte příspěvek",
            }
        error_messages = {
            "user_name": {
                "required": "pole nemůže být prázdné, prosím vyplňte jméno",
                "max_length": "Vaše jméno je příliš dlouhé, zadejte prosím kratší verzi"
            },
            "text": {
                "required": "pole nemůže být prázdné, prosím vyplňte textové pole",
                "max_length": "Váš komentář je příliš dlouhý, zadejte prosím kratší verzi. Maximálně 400 znaků"
            }
        }

