from django.shortcuts import render, redirect
from django.utils.text import slugify
from .models import Page
from .identify_page_links import identify_page_links


def main_menu(request):
    if request.GET.get('search_by_title', None):
        pages = Page.objects.filter(title__contains=request.GET['search_by_title'])
    else:
        pages = Page.objects.all()
    content = {
        'current_user': request.user,
        'pages': pages
    }
    return render(request, "index.html", content)


def increment_page_view(page_object):
    view_counter = page_object.view_counter
    page_object.view_counter = view_counter+1
    return page_object.save()


def transform_page_links(page_content):
    links = identify_page_links(page_content)
    for i in links:
        slug = slugify(i)
        pages_with_slug = Page.objects.filter(slug=slug)
        css_class = 'class="non-existing"' if len(pages_with_slug) == 0 else ''
        link_html = f'<a href="page-{slug}" {css_class}>{i}</a>'
        page_content = page_content.replace(f'[{i}]', link_html)
    return page_content


def page(request, slug):
    page_obj = Page.objects.filter(slug=slug).first()
    if not page_obj:
        return redirect(f'/page_edit-{slug}')

    increment_page_view(page_obj)
    page_content_parsed = transform_page_links(page_obj.content)

    content = {
        'authenticated': request.user.is_authenticated,
        'current_user': request.user,
        'page': page_obj,
        'page_content_parsed': page_content_parsed
    }

    return render(request, "page_view.html", content)


def page_edit(request, slug):
    if not request.user.is_authenticated:
        return redirect('/')

    page_obj = Page.objects.filter(slug=slug).first()

    title = str(slug).replace('-', ' ').capitalize() if not page_obj else page_obj.title
    content = '' if not page_obj else page_obj.content

    content = {
        'title': title,
        'content': content
    }
    return render(request, "page_edit.html", content)


def post_page_edit(request):
    if request.method != 'POST':
        return redirect('/')

    title = request.POST['title']
    content = request.POST['content']

    page_obj, created = Page.objects.get_or_create(title=title)
    page_obj.content = content
    page_obj.save()

    return redirect(f'/page-{page_obj.slug}')
