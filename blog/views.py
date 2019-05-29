from django.shortcuts import render
from .forms import InputForm


# Create your views here.
def post_list(request):
    if request.method == "POST":
        #print(request.years)
        print("POST")
        form = InputForm(request.POST)
        if form.is_valid():
            year = form.cleaned_data["years"]
            month = form.cleaned_data["months"]
            print(year,",",month)
    else:
        form = InputForm()

    return render(request, 'blog/post_list.html', {})