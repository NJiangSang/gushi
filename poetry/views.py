from django.shortcuts import render, get_object_or_404, redirect
from .models import Poem


def poem_list(request):
    poems = Poem.objects.filter(is_deleted=0)  # 仅获取未标记为删除的诗歌
    return render(request, 'poetry/poem_list.html', {'poems': poems})


def poem_create(request):
    if request.method == "POST":
        title = request.POST['title']
        author = request.POST['author']
        content = request.POST['content']
        type = request.POST['type']
        video_url = request.POST['video']  # 注意这里保留了视频链接的字段名称
        image = request.FILES.get('image')  # 获取上传的插图

        # 创建新的诗词对象
        Poem.objects.create(
            title=title,
            author=author,
            type=type,
            content=content,
            video_url=video_url,
            image=image
        )
        return redirect('poem_list')

    return render(request, 'poetry/poem_form.html')


def poem_update(request, poem_id):
    poem = get_object_or_404(Poem, id=poem_id)
    if request.method == "POST":
        poem.title = request.POST.get('title', poem.title)  # 使用现有值作为默认
        poem.author = request.POST.get('author', poem.author)
        poem.content = request.POST.get('content', poem.content)
        poem.video_url = request.POST.get('video_url', poem.video_url)
        poem.save()
        return redirect('poem_list')
    return render(request, 'poetry/poem_detail.html', {'poem': poem})


def poem_delete(request, poem_id):
    poem = get_object_or_404(Poem, id=poem_id)
    poem.is_deleted = 1  # 将 is_deleted 字段设置为 1，表示已删除
    poem.save()  # 保存变更
    return redirect('poem_list')  # 重定向到诗歌列表
