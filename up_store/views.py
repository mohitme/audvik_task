from django.shortcuts import render, redirect
from up_store.forms import upForm
import pandas as pd
from sqlalchemy import create_engine
from django.conf import settings
db_connection_url = "postgresql://{}:{}@{}:{}/{}".format(
    settings.DATABASES['default']['USER'],
    settings.DATABASES['default']['PASSWORD'],
    settings.DATABASES['default']['HOST'],
    settings.DATABASES['default']['PORT'],
    settings.DATABASES['default']['NAME'],
)

engine = create_engine(db_connection_url)
# Create your views here.
def upload(request):
    if request.method == 'POST':
        form = upForm(request.POST, request.FILES)
        if form.is_valid():
            #form.save()
            name = form.cleaned_data.get('name')
            df = pd.read_csv(request.FILES['file'])
            df.to_sql(name, con = engine, if_exists = 'append', chunksize = 1000)
            return render(request, 'display.html', {'data': df.to_html()})
    else:
        form = upForm()
    return render(request, 'upload.html', {'form': form})