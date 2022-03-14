from django.shortcuts import render

from django.views.generic import TemplateView


class BlogTemplateView(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, 'blog/blog.html')


    def post(self, request, *args, **kwargs):
        pass



class BlogDetailTemplateView(TemplateView):
    def get(self, request, slug, *args, **kwargs):
        return render(request, 'blog/blog-single.html')


    def post(self, request, *args, **kwargs):
        pass




