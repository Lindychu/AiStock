# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# Create your views here.
def test(request):
    # if 'e_id' not in request.session:
        
    context = {
    }
    return render(request, 'test.html', {})