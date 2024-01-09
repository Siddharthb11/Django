from django.shortcuts import render
from django.http import HttpResponse
from movies.models import Movies_Table

# Create your views here.
def display(request):
    msg = "this is display of views movies"
    return HttpResponse(msg)


def show_movies(request):
    result = Movies_Table.objects.all()
    my_data = {'movie_list':result}
    return render(request,'movies/index.html', context = my_data)