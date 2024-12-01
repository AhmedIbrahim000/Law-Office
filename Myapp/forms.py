from django import forms
from .models import Client, Case, Sitting, Appointments

class ClientForm(forms.ModelForm):
    gender = forms.ChoiceField(
        label='الجنس',
        choices=[('ذكر', 'ذكر'), ('أنثى', 'أنثى')],
        widget=forms.RadioSelect(attrs={'class': 'radio-inline'})
    )
    class Meta:
        model = Client
        fields = ['client_id', 'client_name', 'gender', 'Date_Of_Birth', 'email', 'mobile', 'address', 'state', 'city']
        labels = {
            'client_id': 'الرقم القومي',
            'client_name': 'الاسم',
            'Date_Of_Birth': 'تاريخ الميلاد',
            'email': 'البريد الإلكتروني',
            'mobile': 'رقم المحمول',
            'address': 'العنوان',
            'state': 'المحافظة',
            'city': 'المدينة'
        }
        widgets = {
            'client_id': forms.NumberInput(attrs={'class': 'form-control'}),
            'client_name': forms.TextInput(attrs={'class': 'form-control'}),
            'Date_Of_Birth': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'mobile': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'state': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'})
        }


class CaseForm(forms.ModelForm):
    case_type = forms.ChoiceField(
        label='نوع القضية',
        choices=[('مخالفات', 'مخالفات'), ('جنح', 'جنح'), ('جنايات', 'جنايات'), 
                ('أحوال شخصية', 'أحوال شخصية'), ('إداري', 'إداري'), ('مجلس دولة', 'مجلس دولة'), 
                ('مدني', 'مدني'), ('تجاري', 'تجاري'), ('عمال', 'عمال')],
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    status = forms.ChoiceField(
        label='الحالة',
        choices=[('جارية', 'جارية'), ('مؤجلة', 'مؤجلة'), ('مؤرشفة', 'مؤرشفة')],
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    client_FK = forms.ModelChoiceField(
        label='العميل',
        queryset=Client.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        to_field_name='client_name'
    )
    results = forms.CharField(
        label='الحكم',
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    notes = forms.CharField(
        label='ملاحظات',
        required=False,
        widget=forms.Textarea(attrs={'class': 'form-control'})
    )
    class Meta:
        model = Case
        fields = ['case_number', 'case_date', 'case_type', 'court', 'status', 'results', 'notes', 'client_FK']
        labels = {
            'case_number': 'رقم القضية',
            'case_date': 'تاريخ القضية',
            'court': 'المحكمة',
        }
        widgets = {
            'case_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'case_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'court': forms.TextInput(attrs={'class': 'form-control'}),
        }

    # def init(self, args, **kwargs):
    #     super(CaseForm, self).init(args, **kwargs)
    #     self.fields['author'].queryset = Author.objects.all()


class SittingForm(forms.ModelForm):
    attachments = forms.FileField(
        label='الملحقات',
        required=False,
        widget=forms.FileInput(attrs={'class': 'form-control'})
    )
    notes = forms.CharField(
        label='ملاحظات',
        required=False,
        widget=forms.Textarea(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Sitting
        fields = ['sitting_number', 'sitting_date', 'attachments', 'notes']
        labels = {
            'sitting_number': 'رقم الجلسة',
            'sitting_date': 'تاريخ الجلسة',
        }
        widgets = {
            'sitting_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'sitting_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }


class AppointmentForm(forms.ModelForm):
    notes = forms.CharField(
        label='ملاحظات',
        required=False,
        widget=forms.Textarea(attrs={'class': 'form-control'})
    )
    client_FK = forms.ModelChoiceField(
        label='العميل',
        queryset=Client.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        to_field_name='client_name'
    )
    class Meta:
        model = Appointments
        fields = ['appointment_date', 'notes', 'client_FK']
        labels = {
            'appointment_date': 'تاريخ الميعاد',
        }
        widgets = {
            'appointment_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
