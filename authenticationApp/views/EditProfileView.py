import sys

from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required

from authenticationApp.models import Profile
from authenticationApp.forms import EditProfileForm


@login_required
def EditProfileView(request):
    user = request.user
    profile = Profile.get_profile_by_user(user)

    if not profile.is_verified:
        return redirect(reverse('authenticationApp:account-verification'))

    form = EditProfileForm(initial={'firstname': profile.firstname,
                                    'lastname': profile.lastname,
                                    'phone': profile.phone})

    context = {'form': form}

    if request.method == "POST":
        form = EditProfileForm(request.POST, request.FILES, instance=profile)

        if form.is_valid():
            form.save()

            new_profilepic = form.cleaned_data['profilepic']
            profile.profilepic = new_profilepic
            profile.save()

            return redirect(reverse('authenticationApp:profile'))
        else:
            print(form.errors)

    return render(request, 'authenticationApp/editprofile.html', context)


sys.modules[__name__] = EditProfileView
