from django.http import Http404
from django.shortcuts import redirect, render
from user.models import User
from .forms import BoardForm
from .models import Board
from django.core.paginator import Paginator
from tag.models import Tag

def board_list(request):
    all_boards = Board.objects.all().order_by('-id')
    paginator = Paginator(all_boards, 2)
    page = int(request.GET.get('p', 1))
    boards = paginator.get_page(page)       
    return render(request, 'board_list.html', {'boards': boards})


def board_write(request):
    if not request.session.get('user'):
        return redirect('/fcuser/login/')

    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            user_id = request.session.get('user')
            user = User.objects.get(pk=user_id)

            board = Board()
            board.title = form.cleaned_data['title']
            board.contents = form.cleaned_data['contents']
            board.writer = user
            board.save()

            tags = form.cleaned_data['tags'].split(',')
            for tag in tags:
                _tag, _ = Tag.objects.get_or_create(name=tag)
                board.tags.add(_tag)
            return redirect('/board/list')
    else:
        form = BoardForm()
    return render(request, 'board_write.html', {'form': form})


def board_detail(request, pk):
    try:
        board = Board.objects.get(pk=pk)
    except Board.DoesNotExist:
        raise Http404('게시글을 찾을 수 없습니다.')
    
    return render(request, 'board_detail.html', {'board': board})

# _tag 자리는 객체 created 는 새로만든건지 원래있던거지 여부를 가져다줌
# _tag, created = Tag.objects.get_or_create(name=tag)
# _tag, _ = Tag.objects.get_or_create(name=tag, defaults={'test'})
# _ 는 다중 값 반환할 때 사용하지 않겠다 라는 의미
# 중요 !! board_tag 테이블에 항목을 넣기 위해서는 board와 tag 테이블에 먼저 만들어져야 하므로 위에서 board.save()로 만들고 바로 위애서 create하거나 원래 존재했던거임
