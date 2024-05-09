from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.views import View
from .models import UserSubscription
from users.models import User



def test_subscription(request):
    sub = UserSubscription.objects.get(user=request.user)
    sub.validate_subscription()
    if sub.is_active == True:
        return HttpResponse("True")
    else:
        return HttpResponse("False")