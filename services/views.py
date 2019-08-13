from django.shortcuts import render
import requests


# Create your views here.
def index(request):

    return render(request, 'services/index.html')

def artii(request):
    return render(request, 'services/artii.html')

def artii_result(request):
    text = request.GET.get('word')
    font = request.GET.get('font')
    response = requests.get(f'http://artii.herokuapp.com/make?text={text}&font={font}')
    context = {
        'result': response.text
    }
    return render(request, 'services/artii_result.html',context)

def num_push(request):
    return render(request, 'services/num_push.html')

def num_pull(request):
    number = request.GET.get('number')
    context = {
        'number': number
    }
    return render(request, 'services/num_pull.html', context)