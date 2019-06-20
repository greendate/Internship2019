from django.shortcuts import render, HttpResponseRedirect, redirect, HttpResponse
from .models import Comment, URL, Reply
from .forms import CommentModelForm, URLModelForm, ReplyModelForm
import smtplib, ssl

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
        comment_inst.email = form.data['email']
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

        relevant_emails = set()
        comment_email = Comment.objects.get(pk=identify)
        replies_email = Reply.objects.filter(comment_id=identify)
        relevant_emails.add(comment_email.email)
        for reply_email in replies_email:
            relevant_emails.add(reply_email.email)

        for mail in relevant_emails:
            print(mail)
            port = 465  # For SSL
            smtp_server = "smtp.gmail.com"
            sender_email = "commenting.tool@gmail.com"
            receiver_email = mail
            password = "Q6N>qTb'ePCL\dA]"
            message = """\
            Subject: New activity

            Hello,
            You have new activity on comment """ + str(identify) + """.
            Please check: http://ravon.pythonanywhere.com/comment/""" + str(identify) +"""/

            Regards,
            Website Commenting Tool Team"""

            context = ssl.create_default_context()
            with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, message)


        form = ReplyModelForm(request.POST)

        reply_inst.author = form.data['author']
        reply_inst.email = form.data['email']
        reply_inst.text = form.data['text']
        reply_inst.comment_id = identify

        reply_inst.save()
        form = ReplyModelForm()
    else:
        form = ReplyModelForm()

    replies = Reply.objects.filter(comment_id=identify)
    return render(request, 'comment/comment.html', {'comment': comment, 'form': form, 'replies': replies})


def author(request, username):
    comments = Comment.objects.filter(author=username)
    return render(request, 'comment/author.html', {'comments': comments, 'username': username})
