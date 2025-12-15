from django.http import HttpResponse


def index(request):
    return HttpResponse('Copyright © 2025 Danilo Dias .Dev - All rights reserved.')
