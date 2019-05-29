from django.shortcuts import render
from .forms import InputForm
from .getChgRate import getChgRate as gcr


# Create your views here.
def rate_list(request):
    if request.method == "POST":
        form = InputForm(request.POST)
        if form.is_valid():
            year = form.cleaned_data["years"]
            month = form.cleaned_data["months"]
            print(year,",",month)
    else:
        form = InputForm()

    gcr(year+month)
    return render(request, 'blog/rate_list.html', {})
