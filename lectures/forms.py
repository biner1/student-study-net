from django import forms

from .models import Lectures, Lessons


class LessonsForm(forms.ModelForm):

    class Meta:
        model = Lessons
        fields = ['title','lectures', 'upload']

    

    def __init__(self,*args, **kwargs):
        
        user=kwargs.pop('user')
        if not user.is_superuser:
            super(LessonsForm, self).__init__(*args, **kwargs)
            self.fields['lectures'].queryset = Lectures.objects.filter(stage=user.stage)
        else:
            super(LessonsForm, self).__init__(*args, **kwargs)
            self.fields['lectures'].queryset = Lectures.objects.order_by('stage')