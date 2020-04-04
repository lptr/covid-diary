from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Symptom, Reporter, EpidemicActivity
from rest_framework import viewsets, permissions
from .serializers import ReporterSerializer
# Create your views here.


class ReporterViewSet(viewsets.ModelViewSet):
    queryset = Reporter.objects.all()
    serializer_class = ReporterSerializer
    permission_classes = [permissions.IsAuthenticated]


def overview(request):
    reporter = Reporter.objects.get(id=1)
    symptoms = reporter.symptoms.all()
    return render(request, 'diarybase/overview.html', {'symptoms': symptoms, 'reporter': reporter})


def add_symptom(request):
    if request.method == 'POST':
        form = SymptomForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'diarybase/symptom_reg.html', {'fields': form})
    # if a GET (or any other method) we'll create a blank form
    else:
        pass
    return render(request, 'diarybase/symptom_reg.html', {'form': form})
