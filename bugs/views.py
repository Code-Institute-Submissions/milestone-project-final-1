from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.core.paginator import Paginator
from django.contrib import messages
from .models import Bug, Comment
from .forms import BugCommentForm, BugPostForm

# Create your views here.
def bugs_list(request):
	"""
	This view will list all bugs 
	"""
	bugs = Bug.objects.order_by('-created_on').all()
	paginator = Paginator(bugs, 4)
	page = request.GET.get('page')
	bugs = paginator.get_page(page)
	return render(request, 'bugs/bugs.html', {'bugs': bugs})

def bug_detail(request, pk):
	"""
	This view allow users to see a specific bug report in a separate window
	"""
	bug = get_object_or_404(Bug, pk=pk)
	bug.views += 1
	bug.save()
	comments = bug.comments.filter(active=True)
	new_comment = None

	if request.method == 'POST':
		comment_form = BugCommentForm(data=request.POST)
		if comment_form.is_valid:
			# Create Comment object but don't save to database yet
			new_comment = comment_form.save(commit=False)
			# Assign the current post to the comment
			new_comment.bug = bug
			# Save the comment to the database
			new_comment.save()
	else:
		comment_form = BugCommentForm
	return render(request, 'bugs/bug_detail.html', {'bug': bug, 
											'comments': comments,
											'new_comment': new_comment,
											'comment_form': comment_form})

def bug_add(request):
	"""
	This view allow users to submit their own bug reports
	"""
	if request.method == 'POST':
		bug_form = BugPostForm(request.POST)
		if bug_form.is_valid:
			bug = bug_form.save(commit=False)
			bug.author = request.user
			bug.save()
			return redirect('bugs_list', pk=bug.pk)
	else:
		bug_form = BugPostForm()
	return render(request, 'bugs/bug_add.html', {'bug_form': bug_form})

def bug_delete(request, pk):
	"""
	This view allow a user to delete a bug report, but only if is the author 
	"""
	bug = get_object_or_404(Bug, pk=pk)
	if request.user == bug.author:
		bug.delete()
		messages.success(request, 'Successfully deleted!')
	else:
		messages.error(request, 'You can\'t delete this!')
	return redirect('bugs:bugs_list')
