import os

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.template.loader import render_to_string
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, FormView

from popularpeople.forms import AddPostForm, UploadFileForm
from popularpeople.models import People, Category, TagPost, UploadFiles
from popularpeople.utils import DataMixin

menu = [
    {"name": "About Us", "url": "about"},
    {"name": "Add Article", "url": "add_page"},
    {"name": "Contact Us", "url": "contact"},
    {"name": "Log In", "url": "login"}
]


class PeopleHome(ListView):
    template_name = 'popularpeople/index.html'
    #model = People
    context_object_name = 'posts'
    title_page = "Main Page"
    cat_selected = 0
    paginate_by = 3
    extra_context = {
        'title': "Main Page",
        'menu': menu,
        'cats_selected': 0
    }

    def get_queryset(self):
        return People.published.all().select_related('cat')



class ShowPost(DataMixin ,DetailView):
    model = People
    template_name = 'popularpeople/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.get_mixin_context(context, title=context['post'].title)

    def get_object(self, queryset=None):
        return get_object_or_404(People.published, slug=self.kwargs[self.slug_url_kwarg])



def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Page Not Found</h1>")


class AddPage(LoginRequiredMixin, FormView):
    template_name = 'popularpeople/addpage.html'
    form_class = AddPostForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        w = form.save(commit=False)
        w.author = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = "Add Article"
        return context

class ContactView(View):
    template_name = 'popularpeople/contact.html'

    def get(self, request):
        return render(request, self.template_name, {'title': 'Contact Us'})

    def post(self, request):
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        try:
            send_mail(
                subject=f'Contact Form Submission from {name}',
                message=message,
                from_email=email,
                recipient_list=['nazaruk7649@ukr.net'],
            )
            messages.success(request, 'Your message has been sent successfully!')
        except Exception as e:
            messages.error(request, 'There was an error sending your message. Please try again later.')
            print(e)

        return HttpResponseRedirect(reverse('users:contact'))

def login(request):
    return HttpResponse("Login")

# def handle_uploaded_file(f):
#     upload_dir = "popularpeople/uploads"
#     os.makedirs(upload_dir, exist_ok=True)
#     file_path = os.path.join(upload_dir, f.name)
#     with open(file_path, "wb+") as destination:
#         for chunk in f.chunks():
#             destination.write(chunk)

@login_required(login_url='/admin/')
def about(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = form.cleaned_data['file']
            UploadFiles.objects.create(file=uploaded_file)
            message = "File uploaded successfully!"
        else:
            message = "There was an error with the file upload."
    else:
        form = UploadFileForm()

    data = {'menu': menu, 'title': 'About Us', 'form': form}
    return render(request, 'popularpeople/about.html', data)


# def show_category(request, cat_slug):
#     category = get_object_or_404(Category, slug=cat_slug)
#     posts = People.published.filter(cat_id=category.pk)
#
#     data = {
#         'title': f'Category: {category.name}',
#         'menu': menu,
#         'posts': posts,
#         'cat_selected': category.pk,
#     }
#     return render(request, 'popularpeople/index.html', context=data)


class PeopleCategory(ListView):
    template_name = 'popularpeople/index.html'
    context_object_name = 'posts'
    allow_empty = False
    paginate_by = 3

    def get_queryset(self):
        return People.published.filter(cat__slug=self.kwargs['cat_slug']).select_related('cat')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cat = context['posts'][0].cat
        context['title'] = 'Category - ' + cat.name
        context['menu'] = menu
        context['cat_selected'] = cat.pk
        return context



def show_tag_postlist(request, tag_slug):
    tag = get_object_or_404(TagPost, slug=tag_slug)
    posts = tag.tags.filter(is_published=People.Status.PUBLISHED)

    data = {
        'title': f"Тег: {tag.tag}",
        'menu': menu,
        'posts': posts,
        'cat_selected': None,
    }

    return render(request, 'popularpeople/index.html', context=data)

class TagPostList(ListView):
    template_name = 'popularpeople/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return People.published.filter(cat__slug=self.kwargs['cat_slug']).select_related('cat')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tag = TagPost.objects.get(slug=self.kwargs['tag_slug'])
        context['title'] = 'Tag - ' + tag.tag
        context['menu'] = menu
        context['cat_selected'] = None
        return context