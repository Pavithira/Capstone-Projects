# from django import forms
# from .models import *
#
#
# class childInfoForm(forms.ModelForm):
#     class Meta():
#         model = childModel
#         fields = '__all__'
#         widgets = {
#             'Mood': forms.Select(attrs={'class': 'form-control'}),
#             'Screen_Time': forms.NumberInput(attrs={'class': 'form-control'}),
#             'Study_Hours': forms.NumberInput(attrs={'class': 'form-control'}),
#             'Meals_Per_Day': forms.NumberInput(attrs={'class': 'form-control'}),
#             'Sleep_Hours': forms.NumberInput(attrs={'class': 'form-control'}),
#         }
#         # fields = ['Mood', 'Screen_Time', 'Study_Hours', 'Meals_Per_Day', 'Sleep_Hours']


from django import forms
from .models import *

class childInfoForm(forms.ModelForm):
    class Meta:
        model = childModel
        fields = '__all__'
        widgets = {
            # 'mood': forms.Select(attrs={'class': 'form-control'}),
            'Age': forms.NumberInput(attrs={'class': 'form-control'}),
            'Screen_Time': forms.NumberInput(attrs={'class': 'form-control'}),
            'Study_Hours': forms.NumberInput(attrs={'class': 'form-control'}),
            'Meals_Per_Day': forms.NumberInput(attrs={'class': 'form-control'}),
            'Sleep_Hours': forms.NumberInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(childInfoForm, self).__init__(*args, **kwargs)
        # Replace '----' with 'Select Mood'
        # self.fields['Mood'].choices = [('', 'Select Mood')] + list(self.fields['Mood'].choices)[1:]
