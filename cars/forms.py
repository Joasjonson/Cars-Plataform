from django import forms
from .models import Car, CarImage
from django.contrib.auth.models import User


class CarModelForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['name', 'brand','description', 'factory_year', 'model_year','plate', 'value', 'image']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Car Name'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Car Description'}),
            'plate': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Car Plate'}),
        }

    def clean_value(self):
        value = self.cleaned_data['value']
        if value < 1000:
            raise forms.ValidationError("Value must be greater than 1000.")
        return value
    
    def clean_model_year(self):
        model_year = self.cleaned_data['model_year']
        if model_year < 2000:
            raise forms.ValidationError("Model Year must be greater than 2000.")
        return model_year

    def clean_factory_year(self):
        factory_year = self.cleaned_data['factory_year']
        if factory_year < 2000:
            raise forms.ValidationError("Factory Year must be greater than 2000.")
        return factory_year
    
    def clean_plate(self):
        plate = self.cleaned_data['plate']
        if not plate:
            raise forms.ValidationError("Plate is required.")
        return plate
    


class CarImageForm(forms.ModelForm):
    class Meta:
        model = CarImage
        fields = ['image']


CarImageFormSet = forms.inlineformset_factory(Car, CarImage, form=CarImageForm, extra=3, can_delete=True)