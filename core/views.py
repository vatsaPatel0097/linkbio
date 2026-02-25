from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Link, Profile
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

@login_required
def dashboard(request):
    profile = request.user.profile
    links = profile.links.all()
    
    return render(request, "dashboard.html", {"links": links})


@login_required
def add_link(request):
    if request.method == "POST":
        title = request.POST.get("title")
        url = request.POST.get("url")

        profile = request.user.profile

        Link.objects.create(
            profile=profile,
            title=title,
            url=url
        )

        return redirect("dashboard")

    return render(request, "add_link.html")

@login_required
def delete_link(request, link_id):
    profile = request.user.profile

    link = Link.objects.get(id=link_id, profile=profile)
    link.delete()

    return redirect("dashboard")


def public_profile(request, username):
    
    user = get_object_or_404(User, username=username)
    profile = user.profile
    links = profile.links.all()

    return render(request, "public_profile.html", {
        "profile_user": user,
        "links": links,
        "bio": profile.bio
    })

@login_required
def edit_profile(request):

    profile = request.user.profile

    if request.method == "POST":
        bio = request.POST.get("bio")
        profile.bio = bio
        profile.save()

        return redirect("dashboard")

    return render(request, "edit_profile.html", {"profile": profile})

