from django import forms
from .models import Image


class ImageForm(forms.ModelForm):
    """Form for the image model"""

    class Meta:
        model = Image
        fields = ('Image_Name', 'image_upload')
