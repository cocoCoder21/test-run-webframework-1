from django.shortcuts import render
from sampleApp import forms

# Create your views here.
def index(request):
    return render(request, 'index.html')

def form_name_view(request):
    form = forms.FormName(request.POST)

    if form.is_valid():
        print("VALIDATION SUCCESS!")
        print("NAME: "+form.cleaned_data['name'])
        print("EMAIL: "+form.cleaned_data['email'])
        print("TEXT: "+form.cleaned_data['text'])


    return render(request, 'forms.html', {'form':form})
