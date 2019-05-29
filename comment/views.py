from django.shortcuts import render, HttpResponseRedirect, redirect, HttpResponse
from .models import Comment, URL, Reply
from .forms import CommentModelForm, URLModelForm, ReplyModelForm


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
    if request.method == 'POST':

        form = CommentModelForm(request.POST)

        comment_inst.author = form.data['author']
        comment_inst.text = form.data['text']
        comment_inst.highlighted = form.data['highlighted']
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


def comment(request, identify):
    reply_inst = Reply()
    comment = Comment.objects.get(pk=identify)
    if request.method == 'POST':

        form = ReplyModelForm(request.POST)

        reply_inst.author = form.data['author']
        reply_inst.text = form.data['text']
        reply_inst.comment_id = identify

        reply_inst.save()
        form = ReplyModelForm()
    else:
        form = ReplyModelForm()

    replies = Reply.objects.filter(comment_id=identify)
    return render(request, 'comment/comment.html', {'comment': comment, 'form': form, 'replies': replies})
