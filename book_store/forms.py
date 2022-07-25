from django import forms
from .models import Comment, Categories

class registerUser(forms.Form):
    username = forms.CharField()
    email = forms.CharField()
    password = forms.CharField()

class CartForm(forms.Form):
    book_pk = forms.IntegerField(min_value=1)
    next_link = forms.CharField(max_length=240)

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ["score", "title", "content"]

class FilterSearchForm(forms.Form):
    query = forms.CharField(
        min_length=2,
        max_length=360,
        required=False
    )
    maxprice = forms.IntegerField(
        label="Ціна до",
        min_value=0,
        max_value=99999,
        initial=99999
    )
    category = forms.ChoiceField(
        choices=[
            (category.pk, category.name)
            for category in Categories.objects.all()
        ],
        label="Категорія книги",
        required=False
    )