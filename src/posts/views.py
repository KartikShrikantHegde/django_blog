from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

# This is a function based view, so it takes in request and returns a response
# render takes in a request

def post_create(request):
    return HttpResponse("<h1>Create<h1>")

# Retrieve operation

def post_detail(request):

    context = {
        "title": "Detail"
    }
    return render(request, "index.html", context)

def post_list(request):
    #return HttpResponse("<h1>List<h1>")

    context = {
            "title": "List"
        }
    return render(request, "index.html", context)

    # This case works for me as i am still logged into admin page

    # if request.user.is_authenticated():
    #     context = {
    #         "title": "My User list"
    #     }
    # else:
    #     context = {
    #         "title": "List"
    #     }



def post_update(request):
    return HttpResponse("<h1>Update<h1>")

def post_delete(request):
    return HttpResponse("<h1>Delete<h1>")