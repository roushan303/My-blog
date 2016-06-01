from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from .forms import PostForm

def blog_list(request):
	queryset = Post.objects.all()
	if request.user.is_authenticated():
		context = {
		"object_list":queryset,
		"title":"My user List"
	}
	else:
		context = {
			"title":"Unathorised List"
		}
	return render(request, "post_list.html", context)
def blog_create(request):
	form = PostForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "Successfully updated")
		return HttpResponseRedirect(instance.get_absolute_url())	
	context = {
		"form":form,
	}

	exit

	return render(request, "post_form.html", context)
	
def blog_detail(request, id=None):
	instance = get_object_or_404(Post, id=id)
	context = {
		"title":instance.title,
		"instance": instance,
	}
	return render(request, "post_detail.html", context)

	
def blog_update(request, id=None):
	instance = get_object_or_404(Post, id=id)
	form = PostForm(request.POST or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "<a href='#'>item</a> saved", extra_tags='html_safe')
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {
		"title":instance.title,
		"instance": instance,
		"form":form,
	}
	return render(request, "post_form.html", context)


def blog_delete(request, id=None):
	instance = get_object_or_404(Post, id=id)
	instance.delete()
	messages.success(request, "Successfully deleted")
	return redirect("blog:list")
