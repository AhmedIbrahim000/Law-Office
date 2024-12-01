from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import reverse
from datetime import datetime, timedelta

from .models import Client, Case, Sitting, Appointments
from .forms import ClientForm, CaseForm, SittingForm, AppointmentForm

# Create your views here.

def index(request):
    # check to see if the user logged in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in!")
            return redirect('index')
        else:
            messages.success(request, "There was an error logging in, PLaese try again.")
            return redirect('index')
    else:
        return render(request, 'index.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('index')


def clients(request):
    if request.user.is_authenticated:
        return render(request, 'clients.html', {"clients": Client.objects.all()})
    else:
        messages.success(request, "You Must Be Logged In To View That Page...")
        return redirect('index')


def add_client(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ClientForm(request.POST)
            if form.is_valid():
                new_client_id = form.cleaned_data['client_id']
                new_client_name = form.cleaned_data['client_name']
                new_gender = form.cleaned_data['gender']
                new_Date_Of_Birth = form.cleaned_data['Date_Of_Birth']
                new_email = form.cleaned_data['email']
                new_mobile = form.cleaned_data['mobile']
                new_address = form.cleaned_data['address']
                new_state = form.cleaned_data['state']
                new_city = form.cleaned_data['city']

                new_client = Client(
                    client_id = new_client_id,
                    client_name = new_client_name,
                    gender = new_gender,
                    Date_Of_Birth = new_Date_Of_Birth,
                    email = new_email,
                    mobile = new_mobile,
                    address = new_address,
                    state = new_state,
                    city = new_city
                )
                new_client.save()
                return render(request, 'add_client.html', {
                    'form': ClientForm(),
                    'success': True
                })
        else:
            form = ClientForm()
        return render(request, 'add_client.html', {'form': form})
    else:
        messages.success(request, "You Must Be Logged In...")
        return redirect('index')


def client_details(request, id):
    if request.user.is_authenticated:
        client_detail = Client.objects.get(pk=id)
        return render(request, 'client_details.html', {'client_detail': client_detail})
    else:
        messages.success(request, "You Must Be Logged In To View That Page...")
        return redirect('index')
    

def update_client(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            current_record = Client.objects.get(pk=id)
            form = ClientForm(request.POST, instance=current_record)
            if form.is_valid():
                form.save()
                return render(request, 'update_client.html', {
                    'form': form,
                    'success': True
                    })
        else:
            current_record = Client.objects.get(pk=id)
            form = ClientForm(instance=current_record)
        return render(request, 'update_client.html', {
            'form': form
            })
    else:
        messages.success(request, "You Must Be Logged In To View That Page...")
        return redirect('index')


def delete_client(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            client = Client.objects.get(pk=id)
            client.delete()
        return HttpResponseRedirect(reverse('clients'))
    else:
        messages.success(request, "You Must Be Logged In To View That Page...")
        return redirect('index')


def cases(request):
    if request.user.is_authenticated:
        cases = Case.objects.all()

        # Set default date range
        today = datetime.now().date()
        first_day_of_month = today.replace(month=1, day=1)
        default_from_date = first_day_of_month.strftime("%Y-%m-%d")
        default_to_date = today.strftime("%Y-%m-%d")

        # Handling date range filtering
        from_date = request.GET.get('fromdate', default_from_date)
        to_date = request.GET.get('todate', default_to_date)

        if from_date and to_date:
            cases = cases.filter(case_date__range=[from_date, to_date])

        return render(request, 'cases.html', {
            "cases": cases,
            "default_from_date": default_from_date,
            "default_to_date": default_to_date
        })
    else:
        messages.success(request, "You Must Be Logged In To View That Page...")
        return redirect('index')
    

def add_case(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = CaseForm(request.POST)
            if form.is_valid():
                new_case_number = form.cleaned_data['case_number']
                new_case_date = form.cleaned_data['case_date']
                new_case_type = form.cleaned_data['case_type']
                new_court = form.cleaned_data['court']
                new_status = form.cleaned_data['status']
                new_results = form.cleaned_data['results']
                new_notes = form.cleaned_data['notes']
                new_client_FK = form.cleaned_data['client_FK']

                new_case = Case(
                    case_number = new_case_number,
                    case_date = new_case_date,
                    case_type = new_case_type,
                    court = new_court,
                    status = new_status,
                    results = new_results,
                    notes = new_notes,
                    client_FK = new_client_FK,
                )
                new_case.save()
                return render(request, 'add_case.html', {
                    'form': CaseForm(),
                    'success': True
                })
        else:
            form = CaseForm()
        return render(request, 'add_case.html', {'form': form})
    else:
        messages.success(request, "You Must Be Logged In...")
        return redirect('index')
    

def case_details(request, id):
    if request.user.is_authenticated:
        case_detail = Case.objects.get(pk=id)
        return render(request, 'case_details.html', {'case_detail': case_detail})
    else:
        messages.success(request, "You Must Be Logged In To View That Page...")
        return redirect('index')
    

def update_case(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            current_record = Case.objects.get(pk=id)
            form = CaseForm(request.POST, instance=current_record)
            if form.is_valid():
                form.save()
                return render(request, 'update_case.html', {
                    'form': form,
                    'success': True
                    })
        else:
            current_record = Case.objects.get(pk=id)
            form = CaseForm(instance=current_record)
        return render(request, 'update_case.html', {
            'form': form
            })
    else:
        messages.success(request, "You Must Be Logged In To View That Page...")
        return redirect('index')


def delete_case(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            case = Case.objects.get(pk=id)
            case.delete()
        return HttpResponseRedirect(reverse('cases'))
    else:
        messages.success(request, "You Must Be Logged In To View That Page...")
        return redirect('index')


def sittings(request):
    if request.user.is_authenticated:
        sittings = Sitting.objects.all()

        # Set default date range
        today = datetime.now().date()
        first_day_of_month = today.replace(month=1, day=1)
        default_from_date = first_day_of_month.strftime("%Y-%m-%d")
        default_to_date = today.strftime("%Y-%m-%d")

        # Handling date range filtering
        from_date = request.GET.get('fromdate', default_from_date)
        to_date = request.GET.get('todate', default_to_date)

        if from_date and to_date:
            sittings = sittings.filter(sitting_date__range=[from_date, to_date])

        return render(request, 'sittings.html', {
            "sittings": sittings,
            "default_from_date": default_from_date,
            "default_to_date": default_to_date
        })
    else:
        messages.success(request, "You Must Be Logged In To View That Page...")
        return redirect('index')
    

def case_sittings(request, id):
    if request.user.is_authenticated:
        case = Case.objects.get(pk=id)
        case_sittings = case.sitting_set.all()

        # Set default date range
        today = datetime.now().date()
        first_day_of_month = today.replace(month=1, day=1)
        default_from_date = first_day_of_month.strftime("%Y-%m-%d")
        default_to_date = today.strftime("%Y-%m-%d")

        # Handling date range filtering
        from_date = request.GET.get('fromdate', default_from_date)
        to_date = request.GET.get('todate', default_to_date)

        if from_date and to_date:
            case_sittings = case_sittings.filter(sitting_date__range=[from_date, to_date])

        return render(request, 'case_sittings.html', {
            "case_sittings": case_sittings,
            "case_id": id,
            "default_from_date": default_from_date,
            "default_to_date": default_to_date
        })
    else:
        messages.success(request, "You Must Be Logged In To View That Page...")
        return redirect('index')


def add_sitting(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = SittingForm(request.POST, request.FILES)
            if form.is_valid():
                new_sitting_number = form.cleaned_data['sitting_number']
                new_sitting_date = form.cleaned_data['sitting_date']
                new_attachments = form.cleaned_data['attachments']
                new_notes = form.cleaned_data['notes']

                case = Case.objects.get(pk=id)

                new_sitting = Sitting(
                    sitting_number = new_sitting_number,
                    sitting_date = new_sitting_date,
                    attachments = new_attachments,
                    notes = new_notes,
                    case_FK = case,
                )
                new_sitting.save()
                return render(request, 'add_sitting.html', {
                    'form': SittingForm(),
                    "case_id": id,
                    'success': True
                })
        else:
            form = SittingForm()
        return render(request, 'add_sitting.html', {'form': form, "case_id": id})
    else:
        messages.success(request, "You Must Be Logged In...")
        return redirect('index')
    

def sitting_details(request, id):
    if request.user.is_authenticated:
        sitting_detail = Sitting.objects.get(pk=id)
        return render(request, 'sitting_details.html', {'sitting_detail': sitting_detail})
    else:
        messages.success(request, "You Must Be Logged In To View That Page...")
        return redirect('index')
    

def update_sitting(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            current_record = Sitting.objects.get(pk=id)
            form = SittingForm(request.POST, instance=current_record)
            if form.is_valid():
                form.save()
                return render(request, 'update_sitting.html', {
                    'form': form,
                    'success': True
                    })
        else:
            current_record = Sitting.objects.get(pk=id)
            form = SittingForm(instance=current_record)
        return render(request, 'update_sitting.html', {
            'form': form
            })
    else:
        messages.success(request, "You Must Be Logged In To View That Page...")
        return redirect('index')


def delete_sitting(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            sitting = Sitting.objects.get(pk=id)
            sitting.delete()
        return HttpResponseRedirect(reverse('sittings'))
    else:
        messages.success(request, "You Must Be Logged In To View That Page...")
        return redirect('index')


def appointments(request):
    if request.user.is_authenticated:
        appointments = Appointments.objects.all()

        # Set default date range
        today = datetime.now().date()
        first_day_of_month = today.replace(month=1, day=1)
        default_from_date = first_day_of_month.strftime("%Y-%m-%d")
        default_to_date = today.strftime("%Y-%m-%d")

        # Handling date range filtering
        from_date = request.GET.get('fromdate', default_from_date)
        to_date = request.GET.get('todate', default_to_date)

        if from_date and to_date:
            appointments = appointments.filter(appointment_date__range=[from_date, to_date])

        return render(request, 'appointments.html', {
            "appointments": appointments,
            "default_from_date": default_from_date,
            "default_to_date": default_to_date
        })
    else:
        messages.success(request, "You Must Be Logged In To View That Page...")
        return redirect('index')


def add_appointment(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = AppointmentForm(request.POST)
            if form.is_valid():
                new_client_FK = form.cleaned_data['client_FK']
                new_appointment_date = form.cleaned_data['appointment_date']
                new_notes = form.cleaned_data['notes']

                new_client = Appointments(
                    client_FK = new_client_FK,
                    appointment_date = new_appointment_date,
                    notes = new_notes,
                )
                new_client.save()
                return render(request, 'add_appointment.html', {
                    'form': AppointmentForm(),
                    'success': True
                })
        else:
            form = AppointmentForm()
        return render(request, 'add_appointment.html', {'form': form})
    else:
        messages.success(request, "You Must Be Logged In...")
        return redirect('index')


def appointment_details(request, id):
    if request.user.is_authenticated:
        appointment_detail = Appointments.objects.get(pk=id)
        return render(request, 'appointment_details.html', {'appointment_detail': appointment_detail})
    else:
        messages.success(request, "You Must Be Logged In To View That Page...")
        return redirect('index')
    

def update_appointment(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            current_record = Appointments.objects.get(pk=id)
            form = AppointmentForm(request.POST, instance=current_record)
            if form.is_valid():
                form.save()
                return render(request, 'update_appointment.html', {
                    'form': form,
                    'success': True
                    })
        else:
            current_record = Appointments.objects.get(pk=id)
            form = AppointmentForm(instance=current_record)
        return render(request, 'update_appointment.html', {
            'form': form
            })
    else:
        messages.success(request, "You Must Be Logged In To View That Page...")
        return redirect('index')


def delete_appointment(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            appointment = Appointments.objects.get(pk=id)
            appointment.delete()
        return HttpResponseRedirect(reverse('appointment'))
    else:
        messages.success(request, "You Must Be Logged In To View That Page...")
        return redirect('index')

