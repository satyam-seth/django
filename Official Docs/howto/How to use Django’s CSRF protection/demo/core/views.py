import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from core.forms import TodoForm

# Create your views here.


def index(request):
    if request.method == 'GET':
        form = TodoForm()
        return render(request, 'core/index.html', {'form': form})

    elif request.method == 'POST':
        form = TodoForm(request.POST)

        if form.is_valid():
            return HttpResponse(f'Submitted 👏 Title > "{request.POST["title"]}"')

        return render(request, 'core/index.html', {'form': form})


def ajax_submit(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        return JsonResponse(data)
