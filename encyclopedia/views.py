from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import redirect
from django.contrib import messages
import markdown2
import random

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })
    

def entry_page(request, title):
    entries = set(util.list_entries())
    if title not in entries:
        raise Http404()  
    page_content = markdown2.markdown(util.get_entry(title))   
    return render(request, "encyclopedia/entry_page.html", {
        "title": title,
        "page_content": page_content
    })

def search_results(request):
    query = request.GET.get('q', '')
    entries = set(util.list_entries())
    if query in entries:
        return redirect('wiki:entry_page', query)
    else:
        potential_matches = [title for title in entries if query in title]
        return render(request, "encyclopedia/search_results.html", {
        "query": query,
        "potential_matches": potential_matches
    })

def random_page(request):
    entries = util.list_entries()
    random_entry = random.choice(entries)
    return redirect('wiki:entry_page', random_entry)


class CreatePage(View):

    def get(self, request):
        return render(request, "encyclopedia/create_new_page.html")
        
    def post(self, request):
        title = request.POST.get("title")
        entries = set(util.list_entries())
        if title in entries:
            messages.error(request, "The Page you are trying to create already exist. You can't overwrite it (Please try to \"Edit Page\" to modify it).")
            return render(request, "encyclopedia/create_new_page.html")
        page_content = request.POST.get("page_content")
        util.save_entry(title, page_content)
        return redirect('wiki:entry_page', title)


class EditPage(View):

    def get(self, request, title):
        page_content = util.get_entry(title)   
        return render(request, "encyclopedia/edit_page.html",  {
        "title": title,
        "page_content":page_content
    })
        
    def post(self, request, title):
        page_content = request.POST.get("page_content")
        util.save_entry(title, page_content)
        return redirect('wiki:entry_page', title)