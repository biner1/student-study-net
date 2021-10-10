from django import forms

from .models import Lectures, Lessons

# lesson upload form
class LessonsForm(forms.ModelForm):

    class Meta:
        model = Lessons
        fields = ['title','lectures', 'upload']

    

    def __init__(self,*args, **kwargs):
        user=kwargs.pop('user')
# getting the user's stage, to restrict lecture upload for the uploader
        if not user.is_superuser:
            super(LessonsForm, self).__init__(*args, **kwargs)
            self.fields['lectures'].queryset = Lectures.objects.filter(stage=user.stage)
# if user is super_user, can upload for any lectures
        else:
            super(LessonsForm, self).__init__(*args, **kwargs)
            self.fields['lectures'].queryset = Lectures.objects.order_by('stage')