from django.shortcuts import render, HttpResponseRedirect, redirect
from .models import Comment, URL
from .forms import CommentModelForm, URLModelForm


def comments_list(request):
    if request.method == 'POST':
        url = request.POST.get('site_url', False)
        file = open('args.txt', 'w')
        file.write(url)
        file.close()
        return redirect('new')
    comments = Comment.objects.all()
    url_inst = URLModelForm()
    return render(request, 'comment/comments_list.html', {'comments': comments, 'url': url_inst})


def new_comment(request):
    comment_inst = Comment()
    file = open('args.txt', 'r')
    url = file.read()
    file.close()
    print(url)
    if request.method == 'POST':

        form = CommentModelForm(request.POST)

        comment_inst.author = form.data['author']
        comment_inst.text = form.data['text']
        comment_inst.page_url = url

        comment_inst.save()
        comments = Comment.objects.all()
        form = CommentModelForm()
        return redirect('/..')

    else:
        form = CommentModelForm()
    url_inst = URLModelForm()
    url_inst.page_url = url
    return render(request, 'comment/new_comment.html', {'form': form, 'url': url_inst})
