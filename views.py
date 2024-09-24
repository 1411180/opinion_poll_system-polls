from django.shortcuts import render, get_object_or_404, redirect
from .models import Poll, Question, Choice, Vote
from django.contrib.auth.decorators import login_required
from .forms import PollForm, QuestionForm, ChoiceForm
from django.shortcuts import render
from .models import Poll, Vote
import json

@login_required
def create_poll(request):
    if request.method == "POST":
        form = PollForm(request.POST)
        if form.is_valid():
            poll = form.save(commit=False)
            poll.created_by = request.user
            poll.save()
            return redirect('polls:poll_list')
    else:
        form = PollForm()
    return render(request, 'polls/create_poll.html', {'form': form})

@login_required
def update_poll(request, poll_id):
    poll = get_object_or_404(Poll, id=poll_id, created_by=request.user)
    if request.method == "POST":
        form = PollForm(request.POST, instance=poll)
        if form.is_valid():
            form.save()
            return redirect('polls:poll_list')
    else:
        form = PollForm(instance=poll)
    return render(request, 'polls/update_poll.html', {'form': form})

@login_required
def delete_poll(request, poll_id):
    poll = get_object_or_404(Poll, id=poll_id, created_by=request.user)
    if request.method == "POST":
        poll.delete()
        return redirect('polls:poll_list')
    return render(request, 'polls/delete_poll.html', {'poll': poll})

def poll_list(request):
    polls = Poll.objects.all()
    return render(request, 'polls/poll_list.html', {'polls': polls})

def poll_detail(request, poll_id):
    poll = get_object_or_404(Poll, id=poll_id)
    return render(request, 'polls/poll_detail.html', {'poll': poll})

@login_required
def vote(request, poll_id, choice_id):
    poll = get_object_or_404(Poll, id=poll_id)
    choice = get_object_or_404(Choice, id=choice_id, question__poll=poll)
    Vote.objects.create(poll=poll, user=request.user, choice=choice)
    return redirect('polls:poll_detail', poll_id=poll.id)

def poll_detail(request, poll_id):
    # Get the poll and its options
    poll = Poll.objects.get(id=poll_id)
    votes = poll.vote_set.all()

    # Prepare data for the chart
    poll_results = [
        {'option': vote.option.text, 'votes': vote.count}
        for vote in votes
    ]

    # Pass the data to the template
    context = {
        'poll': poll,
        'poll_results_data': json.dumps(poll_results)  # Convert data to JSON
    }

    return render(request, 'polls/poll_detail.html', context)
