from django.template.loader import get_template
from django.http import HttpResponse


def index(request):
    return HttpResponse("hello, django!")


def password_reset(request):
    user = {'username': 'CK Wong', 'email': 'CK@demo.com'}
    t = get_template('bbs/password_reset.html')
    context = {'user': user}
    # 在django 1.1版本中可以直接传入Context对象，
    # 在1.11 后只能传入字典
    html = t.render(context)
    return HttpResponse(html)
