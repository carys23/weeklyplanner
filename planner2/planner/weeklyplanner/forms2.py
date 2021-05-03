from django import forms
from .models import Note

class ListForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ["notes", "completed", "day"]

    # def get_event(request):
    #     if request.method == 'POST':
    #         form = EventForm(request.POST)
    #         form.save()
    #         return HttpResponseRedirect('/thanks/')
    #         return render(request, 'notes.html', context)