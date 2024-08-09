from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
from django.shortcuts import redirect, render
from django.urls import reverse
from django.template.loader import render_to_string


menu = [
    {"name": "About Us", "url": "about"},
    {"name": "Add Article", "url": "add_page"},
    {"name": "Contact Us", "url": "contact"},
    {"name": "Log In", "url": "login"}
]



sportsmen = [
    {
        "id": 1,
        "title": "Lionel Messi",
        "content": (
            "Lionel Messi is an Argentine professional footballer widely regarded as one of the greatest players of all time. "
            "He has spent the majority of his career with FC Barcelona, where he won numerous titles, including multiple La Liga and Champions League trophies. "
            "Messi has also been awarded the Ballon d'Or multiple times, highlighting his exceptional skills and contributions to the sport."
        ),
        "is_published": True
    },
    {
        "id": 2,
        "title": "LeBron James",
        "content": (
            "LeBron James is an American professional basketball player known for his incredible athleticism and versatility. "
            "Playing primarily as a forward, he has achieved success with the Cleveland Cavaliers, Miami Heat, and Los Angeles Lakers. "
            "LeBron is a four-time NBA champion and has been named NBA Finals MVP multiple times. His impact extends beyond the court, as he is also known for his philanthropic efforts and activism."
        ),
        "is_published": True
    },
    {
        "id": 3,
        "title": "Roger Federer",
        "content": (
            "Roger Federer is a Swiss professional tennis player celebrated for his grace on the court and his remarkable career achievements. "
            "With numerous Grand Slam titles to his name, including Wimbledon and the Australian Open, Federer is considered one of the greatest tennis players in history. "
            "His playing style and sportsmanship have earned him admiration from fans and fellow athletes alike."
        ),
        "is_published": True
    },
    {
        "id": 4,
        "title": "Usain Bolt",
        "content": (
            "Usain Bolt is a Jamaican former sprinter who holds the world record for the 100 meters and 200 meters. "
            "Known as 'Lightning Bolt' for his incredible speed, he is an eight-time Olympic gold medalist and has set numerous world records. "
            "Bolt's charismatic personality and dominance in sprinting events have made him a global icon in athletics."
        ),
        "is_published": False
    },
    {
        "id": 5,
        "title": "Cristiano Ronaldo",
        "content": (
            "Cristiano Ronaldo is a Portuguese professional footballer renowned for his goal-scoring ability and physical prowess. "
            "He has played for top clubs like Manchester United, Real Madrid, and Juventus, winning multiple domestic and international titles. "
            "Ronaldo has also been awarded the Ballon d'Or several times and is known for his dedication to fitness and his impact on and off the field."
        ),
        "is_published": True
    }
]

cats_db = [
    {"id": 1, "name": "Sportsmen"},
    {"id": 2, "name": "Actors"},
    {"id": 3, "name": "Scientists"},
    {"id": 4, "name": "Musicians"},
    {"id": 5, "name": "Authors"},
    {"id": 6, "name": "Entrepreneurs"},
    {"id": 7, "name": "Politicians"},
    {"id": 8, "name": "Philanthropists"},
    {"id": 9, "name": "Inventors"},
    {"id": 10, "name": "Artists"},
    {"id": 11, "name": "Explorers"}
]

def index(request):
    data = {'title': "Main Page",
            'menu': menu,
            'posts': sportsmen,
            'cats_selected': 0
            }

    return render(request, 'popularpeople/index.html', context=data)

def show_post(request, post_id):
    return HttpResponse(f"Article with id = {post_id}")


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Page Not Found</h1>")


def addpage(request):
    return HttpResponse("Add article")

def contact(request):
    return HttpResponse("Contact Us")

def login(request):
    return HttpResponse("Login")


def about(request):
    data = {'menu': menu}
    return render(request, 'popularpeople/about.html', data)



def show_category(request, cat_id):
    data = {
        'title': 'Articles by categories',
        'menu': menu,
        'posts': sportsmen,
        'cat_selected': cat_id,
    }
    return render(request, 'popularpeople/index.html', context=data)

