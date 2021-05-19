import sys

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from authenticationApp.models import Profile


@login_required
def AccountVerificationView(request):
    profile = Profile.get_profile_by_user(request.user)
    context = {'profile': profile}

    return render(request, 'authenticationApp/accountverification.html', context)


sys.modules[__name__] = AccountVerificationView