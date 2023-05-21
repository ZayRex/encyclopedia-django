from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import redirect
import markdown2

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


    # return HttpResponse(markdown2.markdown(util.get_entry(title)))
    # return render(request, "encyclopedia/index.html", {
    #     "entries": util.list_entries()
    # })