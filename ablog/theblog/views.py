from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category, Comment
from .forms import Postform, Editform, CommentForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect


# Create your views here.
# def home(request):
#    return render(request,"home.html",{})

# To add the like & go to article details page

def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id')) #we are looking for a post by an id post what ever the post that we click
    liked = False
    if post.likes.filter(id=request.user.id).exists(): #like cheythoon nokum user id vech
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('article-detail', args=[str(pk)]))


# __________________________________________

class HomeView(ListView):  # home pagil list ayitt blog kanikan
    model = Post
    template_name = 'home.html'
    ordering = ['-post_date']

    # ordering = ['-id']


    #code for category view in tge home page dropdown

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context


# --------------------------------------------------------------------

# function based view
#home pagil allathe sthalath categories varan

def CategoryListView(request):
    cat_list = Category.objects.all()
    return render(request, 'categories_list.html', {'cat_list': cat_list})


def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats.replace('-', ' '))  # searching for the category thats is placed in the cats
    return render(request, 'categories.html',
                  {'cats': cats.title().replace('-', ' '), 'category_posts': category_posts}) #passing the things into variable thats is to be called from webpage  html


# ----------------------------------------------------------------------------------------
# get_context_data inte adya section home viewil category drop down ayii varan ulla code athil nin copy cheythathan

class ArticleDetailView(DetailView):
    model = Post
    template_name = "article_details.html"

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)

        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()

        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True

        context["cat_menu"] = cat_menu
        context["total_likes"] = total_likes #so this items cat_menu,totalalike...liked... are gona use in html page
        context['liked'] = liked
        return context


class AddPostView(CreateView):
    model = Post
    form_class = Postform
    template_name = "add_post.html"
    # fields = '__all__' : form.py style cheyumbol fiels avide specify cheythal mathi


class UpdatePostView(UpdateView):
    model = Post
    form_class = Editform
    template_name = "update_post.html"
    # fields =['title','title_tag','body']


class DeletePostView(DeleteView):
    model = Post
    template_name = "delete_post.html"
    success_url = reverse_lazy('home')  # delete postil get_absolute_url work avolla athond succes_url upayogikum


class AddCategoryView(CreateView):
    model = Category
    # form_class =Postform
    template_name = "add_category.html"
    fields = '__all__'

# ---------------------------------------------------------------------------------------

class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = "add_comments.html"

    # fields = '__all__'

    def form_valid(self, form): #create profile submit cheymbo eth suer an create cheyannen formilek kodukan
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

    success_url = reverse_lazy('home')


