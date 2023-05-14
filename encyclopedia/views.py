from django.shortcuts import render
from django.http import HttpResponse
import markdown2

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry_page(request, title):
    page_content = markdown2.markdown(util.get_entry(title))
    return render(request, "encyclopedia/entry_page.html", {
        "title": title,
        "page_content": page_content
    })
    # return HttpResponse(markdown2.markdown(util.get_entry(title)))
    # return render(request, "encyclopedia/index.html", {
    #     "entries": util.list_entries()
    # })