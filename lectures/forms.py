from django import forms

from .models import Lectures, Lessons, StudentStage

# lesson upload form
class LessonsCreateForm(forms.ModelForm):

    class Meta:
        model = Lessons
        fields = ['title','lectures', 'upload']

    

    def __init__(self,*args, **kwargs):
        user=kwargs.pop('user')
# getting the user's stage, to restrict lecture upload for the uploader
        if not user.is_superuser:
            super(LessonsCreateForm, self).__init__(*args, **kwargs)
            self.fields['lectures'].queryset = Lectures.objects.filter(stage=user.stage)
# if user is super_user, can upload for any lectures
        else:
            super(LessonsCreateForm, self).__init__(*args, **kwargs)
            self.fields['lectures'].queryset = Lectures.objects.order_by('stage')


class addNewLectureForm(forms.Form):
    name = forms.CharField(label="lecture name",max_length=200)


class addNewStageForm(forms.Form):
    stage = forms.CharField(label="stage name",max_length=20)