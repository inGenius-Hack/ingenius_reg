from django import forms

class LoginForm(forms.Form):
	username 	= forms.CharField(label="Username",max_length=50,required=True)
	password	= forms.CharField(label="Password",max_length=50,required=True,
		widget=forms.PasswordInput)

class RegForm(forms.Form):
	GENDER_CHOICES = (
		('M', 'Male'),
		('F', 'Female'),
	)
	pid = forms.CharField(label="Participant ID or Mobile Number",\
		max_length=10,required=True)
	noc_submitted = forms.BooleanField(label="NOC Submitted", required=False)
	barcode	= forms.CharField(label="Barcode",max_length=100,required=False)

	def __init__(self, *args, **kwargs):
		from django.forms.widgets import HiddenInput
		show_noc = kwargs.pop('show_noc',None)
		hide_barcode = kwargs.pop('hide_barcode',None)
		super(RegForm, self).__init__(*args, **kwargs)
		if not show_noc:
			self.fields['noc_submitted'].widget = HiddenInput()
		if hide_barcode:
			self.fields['barcode'].widget = HiddenInput()

class CheckInForm(forms.Form):
	barcode = forms.CharField(max_length=100, required=True)

class LunchForm(forms.Form):
	barcode = forms.CharField(max_length=50, required=True)

class BreakfastForm(forms.Form):
	barcode = forms.CharField(max_length=50, required=True)

class DinnerForm(forms.Form):
	barcode = forms.CharField(max_length=50, required=True)

class SnacksEveningForm(forms.Form):
	barcode = forms.CharField(max_length=50, required=True)	

class SnacksMidnightForm(forms.Form):
	barcode = forms.CharField(max_length=50, required=True)	
