from django.db import models

# python manage.py makemigrations Myapp
# python manage.py migrate
# python manage.py runserver

class Client(models.Model):
    client_id = models.CharField(max_length=255, default='')
    client_name = models.CharField(max_length=255, default='')
    gender = models.CharField(max_length=255, default='', choices=[('ذكر', 'ذكر'), ('أنثى', 'أنثى')])
    Date_Of_Birth = models.DateField(default=None)
    email = models.EmailField(max_length=255, default='')
    mobile = models.CharField(max_length=255, default='')
    address = models.CharField(max_length=255, default='')
    state = models.CharField(max_length=255, default='')
    city = models.CharField(max_length=255, default='')

    def __str__(self):
        return f"{self.client_name}"


class Case(models.Model):
    case_number = models.CharField(max_length=255, default='')
    case_date = models.DateField(default=None)
    case_type = models.CharField(max_length=255, default='', 
                                 choices=[('مخالفات', 'مخالفات'), ('جنح', 'جنح'), ('جنايات', 'جنايات'), 
                                          ('أحوال شخصية', 'أحوال شخصية'), ('إداري', 'إداري'), ('مجلس دولة', 'مجلس دولة'), 
                                          ('مدني', 'مدني'), ('تجاري', 'تجاري'), ('عمال', 'عمال')])
    court = models.CharField(max_length=255, default='')
    status = models.CharField(max_length=255, default='', choices=[('جارية', 'جارية'), ('مؤجلة', 'مؤجلة'), ('مؤرشفة', 'مؤرشفة')])
    results = models.CharField(max_length=255, blank=True, null=True)
    notes = models.TextField(max_length=255, blank=True, null=True)
    client_FK = models.ForeignKey(Client, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.case_number} {', '} {self.case_type} {', '} {self.status}"


class Sitting(models.Model):
    sitting_number = models.CharField(max_length=255, default='')
    sitting_date = models.DateField(default=None)
    attachments = models.FileField(upload_to='media/', blank=True, null=True)
    notes = models.TextField(max_length=255, blank=True, null=True)
    case_FK = models.ForeignKey(Case, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.sitting_number} {', '} {self.sitting_date}"


class Appointments(models.Model):
    appointment_date = models.DateField(default=None)
    notes = models.TextField(max_length=255, blank=True, null=True)
    client_FK = models.ForeignKey(Client, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.appointment_date} {', '} {self.notes} {', '} {self.client_FK}"

