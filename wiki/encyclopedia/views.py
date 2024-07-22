from django.utils.safestring import mark_safe
from django.shortcuts import render
from . import util
import markdown2
import random
from random import randint

def conversion(title):
    content = util.get_entry(title)
    markdowner = markdown2.markdown(content)
    safe_content = mark_safe(markdowner)
    if content == None:
        return None
    else:
        return safe_content

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def get(request, title):
    entry = util.get_entry(title)
    if entry == None:
        return render(request, "encyclopedia/error.html", {
            'alert': f"Requested {title} page does not exist" 
        })
    else:
        return render(request, "encyclopedia/pages.html", {
        "a_entry": conversion(title),
        "title": title
            })
    
def fetch_data(request):
    all_pages = util.list_entries()
    searched = request.POST['q']
    if searched in all_pages:
        return render(request, "encyclopedia/pages.html", {
            "a_entry": conversion(searched)
        })
    else:
        all_pages_found = [entry for entry in all_pages if searched.lower() in entry.lower()]
        return render(request, "encyclopedia/results.html", {"all_pages_found": all_pages_found})

def new_page(request):
    if request.method == 'GET':
        return render(request, "encyclopedia/newpage.html")
    else:
        new_title = request.POST.get('newtitle')
        new_content = request.POST.get('newcontent')
        
 # Check if the new_title already exists
        if new_title and new_title.lower() in [entry.lower() for entry in util.list_entries()]:
            return render(request, "encyclopedia/error.html", {
                'alert': f"{new_title.capitalize()} page already exists"
            })
        else:
            util.save_entry(new_title, new_content)
            return render(request, "encyclopedia/newpage.html")
        
def edit_page(request):
    if request.method == 'POST':
        title = request.POST['title']
        entry = util.get_entry(title)
        return render(request, "encyclopedia/edit.html", {
            "title": title,
            "content": entry
                })
    
def save_changes(request):
    if request.method == "POST":
        changed_title = request.POST['newtitle']
        changed_content = request.POST['newcontent']
        util.save_entry(changed_title, changed_content)
        return render(request, "encyclopedia/pages.html", {
            "a_entry": conversion(changed_title),
            "title": changed_title
        })

def random_page(request):
    all_pages = util.list_entries()
    random_num = random.randint(0, len(all_pages))
    random_page = all_pages[random_num]
    return render(request, "encyclopedia/pages.html", {
        "a_entry": conversion(random_page)
    })






    


