from django.shortcuts import render, redirect
from up_store.forms import uploadForm
# Create your views here.
def upload(request):
    if request.method == 'POST':
        form = uploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = uploadForm()
    return render(request, 'upload.html', {'form': form})
