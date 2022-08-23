from django import forms
from .models import Application, Branch

materials = (
    ('Debit Card', 'Debit Card'), ('Credit Card', 'Credit Card'), ('Checkbook', 'Checkbook'),)
class ApplicationForm(forms.ModelForm):
    m_name=forms.MultipleChoiceField(choices=materials,label="materials Required",widget=forms.CheckboxSelectMultiple(attrs={'class':'form-group'}))
    class Meta:
        model = Application
        fields = ['name','age','birth_date','mobile','email','address','gender','district','branch','m_name','acc_type']
        labels ={'name':'FullName','age':'Age','birth_date':'DateofBirth','mobile':'Mobile Number','address':'Address',
                 'gender':'Gender','district':'District','branch':'Branch','m_name':'Materials Required','acc_type':'Account Type'}
        attrs=({'district':{'class':'form-control'}})
        widgets=({
            'gender':forms.RadioSelect,
            'acc_type':forms.Select,
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'age':forms.NumberInput(attrs={'class':'form-control'}),
            'birth_date':forms.DateInput(attrs={'class':'form-control'},format="%d/%m/%Y"),
            'mobile':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'address':forms.Textarea(attrs={'class':'form-control'}),
            'acc_type':forms.Select(attrs={'class':'form-control'}),
            'district':forms.Select(attrs={'class':'form-control'}),
            'branch':forms.Select(attrs={'class':'form-control'}),
        })

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['branch'].queryset = Branch.objects.none()

        if 'district' in self.data:
            try:
                district_id = int(self.data.get('district'))
                self.fields['branch'].queryset = Branch.objects.filter(district_id=district_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['branch'].queryset = self.instance.district.branch_set.order_by('name')
