import csv
import io

from django.shortcuts import render
from ..forms import CSVUploadForm
from ..models import Aluno

def import_csv_view(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csvfile = request.FILES['file']
            # data_set = csvfile.read().decode('UTF-8')
            data_set = csvfile.read().decode('latin-1')
            # data_set = csvfile.read().decode('ISO-8859-1')
            io_string = io.StringIO(data_set)
            next(io_string)  # Ignora o cabeçalho, se houver
            for row in csv.reader(io_string, delimiter=':', quotechar="|"):
                _, created = Aluno.objects.update_or_create(
                    aluno_nome=row[0],
                    aluno_cpf=row[1],
                    aluno_email=row[2]
                )
            return render(request, 'csv/sucesso.html')
    else:
        form = CSVUploadForm()
    return render(request, 'csv/import.html', {'form': form})

    