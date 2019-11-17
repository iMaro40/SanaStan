from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from forum.models import ForumTopic, Title, Post
from django.views import generic
from .forms import TitleCreationForm, PostCreationForm

def index(request,topic):
    context = {
        'topics' : ForumTopic.objects.all()
    }
    return render(request,'forum/index.html',context)

class ForumTopicView (generic.ListView):
    model = ForumTopic
    context_object_name = 'ForumTopics'
    template_name = 'forum/index.html'



class TopicTitlesView (generic.DetailView):
    model = ForumTopic
    context_object_name = 'ForumTopic'
    slug_field = 'topic'
    slug_url_kwarg = 'topic'

    template_name = 'forum/topic_titles.html'

    def get_context_data (self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Titles'] = self.object.titles.all()
        return context

class ForumPosts(generic.DetailView):
    model = Title
    template_name = "forum/title_posts.html"
    context_object_name = "Title"
    def get_context_data (self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Posts'] = self.object.posts.all()
        return context

@login_required(login_url='/login/')
def createTitle (request,topic):
    current_topic = ForumTopic.objects.get(topic=topic)
    if request.method == 'POST':
        titleCreationForm = TitleCreationForm(request.POST)
        if titleCreationForm.is_valid():
            new_title = titleCreationForm.save(commit=False)
            new_title.topic = current_topic
            new_title.creator = request.user
            new_title.save()

            return redirect(current_topic.get_absolute_url())
    else:
        titleCreationForm = TitleCreationForm()

    context = {
        'titleCreationForm': titleCreationForm,
    }
    return render(request, 'forum/create_title.html',context)

def createPost(request,topic,pk):
    current_topic = ForumTopic.objects.get(topic=topic)
    current_title = Title.objects.get(pk=pk)
    if request.method == 'POST':
        postCreationForm = PostCreationForm(request.POST)
        if postCreationForm.is_valid():
            new_post = postCreationForm.save(commit=False)
            new_post.title = current_title
            new_post.author = request.user
            new_post.topic = current_topic
            new_post.save()
            return redirect(current_title.get_absolute_url())
    else:
        postCreationForm = PostCreationForm()

    context = {
        'postCreationForm': postCreationForm
    }
    return render(request, 'forum/create_post.html',context)
