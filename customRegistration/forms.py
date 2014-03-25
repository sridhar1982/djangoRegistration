from registration.forms import RegistrationForm
from django import forms
from django.utils.translation import ugettext_lazy as _
from django.utils.safestring import mark_safe
from django.forms.extras.widgets import SelectDateWidget
 
class ExRegistrationForm(RegistrationForm):
    ishuman = forms.BooleanField(required=True,
                             label=mark_safe('is human'),
                             error_messages={'required': "You must agree to the terms to register"})
    dateofBirth=forms.DateField(label=mark_safe('Date of Birth'),
                                widget=SelectDateWidget(years=range(1900,2014)),
                                error_messages={'required': "You must agree to the terms to register"})
    
    
    
#     def clean_ishuman(self):
#         # Since User.username is unique, this check is redundant,
#         # but it sets a nicer error message than the ORM. See #13147.
#         print("called clean_is_human")
#         if 'ishuman' not in self.data:
#             raise forms.ValidationError("This field is required")
#         return self.cleaned_data['ishuman']
#     
#     def save(self, commit=True):
#             user = super(RegistrationForm, self).save(commit=False)
#             user.is_human=self.cleaned_data["ishuman"]
#             if commit:
#                 user.save()
#             print("from save %s" %user.ishuman)
#             return user