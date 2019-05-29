from django.shortcuts import render
from .forms import InputForm
from .getChgRate import getChgRate as gcr


# Create your views here.
def rate_list(request):
    in_val = {}
    if request.method == "POST":
        form = InputForm(request.POST)
        if form.is_valid():
            in_val["year"]= form.cleaned_data["years"]
            in_val["month"] = form.cleaned_data["months"]
            in_val["curr"] = form.cleaned_data["curr"]
    else:
        form = InputForm()

    gcr(in_val)
    return render(request, 'blog/rate_list.html', {})
