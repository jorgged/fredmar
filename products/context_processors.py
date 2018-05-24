from .models import Category


def CategoryList(request):
    categories=dict()
    categories = Category.objects.all()
    return {'categories':categories}
