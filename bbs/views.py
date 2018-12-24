from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from .models import Board, Topic, Post
from .forms import NewTopicForm


def index(request):
    return HttpResponse("hello, django!")


def password_reset(request):
    user = {'username': 'CK Wong', 'email': 'CK@demo.com'}
    return render(request, 'bbs/password_reset.html', {'user': user})


def boards_list(request):
    boards = Board.objects.all()
    return render(request, 'bbs/boards_list.html', {'boards': boards})


class BoardList(ListView):
    model = Board
    context_object_name = 'boards'
    template_name = 'bbs/boards_list.html'


def board_topics(request, pk):
    board = Board.objects.get(id=pk)
    topics = board.topics.all()

    return render(request, 'bbs/board_topics.html', {'board': board, 'topics': topics})


def new_topic(request, pk):
    board = get_object_or_404(Board, pk=pk)
    user = User.objects.get(pk=1)
    if request.method == 'POST':
        form = NewTopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.board = board
            topic.starter = user
            topic.save()
            Post.objects.create(
                message=form.cleaned_data.get('message'),
                topic=topic,
                created_by=user
            )
            return redirect('topic_posts', pk=pk, topic_pk=topic.pk)
    else:
        form = NewTopicForm()
    return render(request, 'bbs/new_topic.html', {'board': board, 'form': form})


def topic_posts(request, pk, topic_pk):
    topic = Topic.objects.get(pk=topic_pk, board__pk=pk)
    posts = topic.posts.all()
    return render(request, 'bbs/posts.html',
                  {'board_pk': pk,
                   'topic': topic,
                   'posts': posts})