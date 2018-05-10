from django.shortcuts import render, get_object_or_404
from .models import Paste
from .forms import PasteForm

def new_paste(request):
    paste = Paste.objects.create(
        title = request.POST.get('title'),
        language = request.POST.get('language'),
        content = request.POST.get('content')
    )
    ctx = {'paste': paste}
    return render(request, 'pastebin/paste-detail.jinja2', ctx)


def index(request):
    form = PasteForm()
    ctx = {'form': form}
    return render(request, 'pastebin/index.jinja2', ctx)

def paste(request, id):
    paste = Paste.objects.get(id=id)
    ctx = {'paste': paste}
    return render(request, 'pastebin/paste-detail.jinja2', ctx)


def language_list(request, language):
    if language == "python":
        pastes = Paste.objects.filter(language=1)
    elif language == "js":
        pastes = Paste.objects.filter(language=2)
    else:
        pastes = Paste.objects.filter(language=3)

    ctx = {'pastes': pastes, 'language': language}
    return render(request, 'pastebin/paste-language.jinja2', ctx)