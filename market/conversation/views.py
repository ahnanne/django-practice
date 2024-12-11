from django.shortcuts import render, redirect, get_object_or_404

from item.models import Item
from .models import Conversation

from .forms import ConversationMessageForm

# Create your views here.


def new_conversation(request, item_pk):
    item = get_object_or_404(Item, pk=item_pk)

    if item.created_by == request.user:
        return redirect('dashboard:index')

    conversations = Conversation.objects.filter(
        item=item).filter(members__in=[request.user.id])

    if conversations:
        pass  # redirect to conversation

    if request.method == 'POST':
        form = ConversationMessageForm(request.POST)

        if form.is_valid():
            converversation = Conversation.objects.create(item=item)
            converversation.members.add(request.user)
            converversation.members.add(item.created_by)
            converversation.save()

            conversation_message = form.save(commit=False)
            conversation_message.conversation = converversation
            conversation_message.created_by = request.user
            conversation_message.save()

            return redirect('item:detail', pk=item_pk)
    else:
        form = ConversationMessageForm()

    return render(request, 'conversation/new.html', {
        'form': form
    })
