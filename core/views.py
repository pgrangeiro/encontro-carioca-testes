from django.views.generic import ListView

from core.models import Patient


class PatientListView(ListView):
    model = Patient
