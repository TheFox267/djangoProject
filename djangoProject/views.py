from django.http import HttpResponseRedirect


def redirect_main(request):
    return HttpResponseRedirect('news/')
