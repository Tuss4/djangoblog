from django import forms

class new_post_form(forms.Form):
	title = forms.CharField()
	post = forms.CharField(widget=forms.Textarea)

class submit_comment(forms.Form):
	name = forms.CharField(max_length=30)
	email = forms.EmailField(required=False)
	message = forms.CharField(widget=forms.Textarea)