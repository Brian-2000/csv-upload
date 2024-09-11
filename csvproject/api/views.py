import pandas as pd
from django.shortcuts import render
from .forms import CSVUploadForm
from .models import CSVData
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def upload_csv(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['file']

            # Load the CSV file into a pandas DataFrame
            try:
                df = pd.read_csv(csv_file)
            except Exception as e:
                return render(request, 'api/upload_csv.html', {'error': 'Error reading CSV file: ' + str(e)})

            # Check for null values
            if df.isnull().values.any():
                return render(request, 'api/upload_csv.html', {'error': 'CSV file contains null values'})

            # Convert the DataFrame to JSON
            data_json = df.to_json(orient='records')

            # Save the JSON data to the database
            csv_data = CSVData(data=data_json)
            csv_data.save()

            # Pass the JSON data to the template
            return render(request, 'api/upload_csv.html', {
                'message': 'File uploaded and saved successfully',
                'data_json': data_json  # Pass JSON data to template
            })

        return render(request, 'api/upload_csv.html', {'error': 'Invalid form submission'})

    return render(request, 'api/upload_csv.html')
