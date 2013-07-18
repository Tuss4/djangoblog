from django import forms

class new_post_form(forms.Form):
	title = forms.CharField()
	post = forms.Field(widget=forms.Textarea)