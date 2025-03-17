from django.shortcuts import render

from stream.consumers import active_streams


def index(request):
    return render(request, "index.html")

def viewer(request):
    return render(request, "viewer.html", {"streams": list(active_streams.keys())})
