from django.http import HttpResponse,JsonResponse

def http_test(request):
    return HttpResponse("<h1>this is a test<h1>")

def jeson_test(request):
    return JsonResponse({'name':'mmd'})