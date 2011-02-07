from django import forms
from helpwanted.models import JobListing

class JobListingForm(forms.ModelForm):
    class Meta:
        model = JobListing
        exclude = ("is_filled","date_published","published_until")