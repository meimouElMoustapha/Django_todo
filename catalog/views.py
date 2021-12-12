from django.shortcuts import render,get_object_or_404
from django.urls import reverse_lazy
from django.http import HttpResponse,HttpResponseRedirect,Http404
# from django.core.paginator import Paginator
# from django.contrib import messages
from django.views.generic.edit import FormView ,UpdateView,DeleteView


# from django.utils import timezone
from .models import Musician,Product,Post
# from django.http.response import JsonResponse
# from .serializers import MoviesSerializer,AlbmSerializer
from django.views.generic.detail import DetailView
# from django.views.generic import View
from rest_framework import generics

from .forms import Productform
# from .forms import Productform




def about(request):
    template_name='about.html'
    context={}
    return render(request, template_name, context)


class DeletePostView(DeleteView):
    model = Product
    template_name = "delete.html"
    context_object_name='post'
    success_url = ('/')
    
    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Product,id=id_)
    
    
    
class postCreate(FormView):
    template_name="postcreate.html"
    
    form_class= Productform
    success_url='/home'
    
    def form_valid(self,form):
        if form.is_valid():
          form.save()
          return super().form_valid(form)
    


class editview(UpdateView):
    model = Product
    
    template_name='edit.html'
    fields = '__all__'
    pk_url_kwarg = 'pk'
    # success_url = reverse_lazy('post:post')
    success_url='home'
   
   
   
class ModelNameDetail(DetailView):
    model = Product
    post=Product.objects.all()
    template_name='detail.html'
    context_object_name='post'
    success_url='home/'
   


    

def home(request):
    post=Product.objects.all()
    # paginator=Paginator(Product.objects.all(),2)
    # page_num = request.GET.get('page')
    # page = paginator.page(2)
    template_name = ('list.html')
    context = {'post':post}
    
    return render(request,template_name,context)




# def home1(request):
    
#     Album=[
#         {
#             'artist':'sidi',
#             'name':'molay',
#             'release_date':'12/05/2021'
#         },
        
#         {
#             'artist':'sidi tttt',
#             'name':'molay mouhamed',
#             'release_date':'12/03/2021'
#         },
#     ]
    
#     return JsonResponse(Album,safe=False) 



# class NoteList(generics.ListCreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = MoviesSerializer
    
# class NoteDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Post.objects.all()
#     serializer_class = MoviesSerializer
