from django.shortcuts import render
from .models import FeedbackItem
from .forms import FeedbackCreateForm

def feedback_create(request):
    if request.method == 'POST':
        form = FeedbackCreateForm(request.POST)
        if form.is_valid():
            feed = form.save()
            return render(request, 'thanks.html')
    else:
        form = FeedbackCreateForm()
    return render(request, 'feedback_form.html', {'form': form})

# Create your views here.
