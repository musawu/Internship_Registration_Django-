from django import forms


class InternForm(forms.Form):
    Intern_fname = forms.CharField(max_length=30)
    Intern_lname = forms.CharField(max_length=30)
    Intern_email = forms.EmailField(max_length=30)
    Intern_phoneNum = forms.CharField(max_length=13)
    # Intern_profile_picture = CloudinaryField('image', default='https://example.com/default-image.jpg')
   
    



#This form only has one field because we will search the participants from their names
class SearchForm(forms.Form):
    Intern_fname = forms.CharField(max_length=30)


class CancelForm(forms.Form):
    Intern_phoneNum = forms.CharField(max_length=30)

