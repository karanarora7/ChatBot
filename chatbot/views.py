from django.shortcuts import render
from .forms import ChatForm


def chatbot_view(request):
    response=""
    if request.method=='POST':
        form=ChatForm(request.POST)
        if form.is_valid():
            user_message=form.cleaned_data['message']
            response= get_chatbot_response(user_message)
    else:
        form=ChatForm()

    return render(request, 'chat.html', {'form':form,'response':response})
    
def get_chatbot_response(message):
    # Here you can use NLP libraries like NLTK, spaCy, or integrate with services like Dialogflow or OpenAI GPT-3
    # For simplicity, let's use a dummy response
    return f"You said: {message}"

