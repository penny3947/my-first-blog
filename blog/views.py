from django.shortcuts import render
from .forms import InputForm
from .getChgRate import get_chg_rate


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

    out_val = get_chg_rate(in_val)

    return render(request, 'blog/rate_list.html', {})
