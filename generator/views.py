from django.shortcuts import render
from .models import Idea

def idea_list(request):
    ideas = Idea.objects.filter(is_checked=True)
    return render(request, 'generator/ideas.html', {'ideas': ideas})

