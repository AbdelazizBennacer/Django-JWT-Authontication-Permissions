from rest_framework.response import Response
from base.models import Note
from .serializers import NoteSerializer




def getNotesList(request):
    #notes = Note.objects.all().order_by('-updated')
    user = request.user
    notes = user.note_set.all()
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)


def getNoteDetail(request, pk):
    user = request.user
    notes = user.note_set.get(id=pk)
    serializer = NoteSerializer(notes, many=False)
    return Response(serializer.data)


def createNote(request):
    user = request.user
    data = request.data
    note = user.note_set.create(
        body=data['body']
    )
    serializer = NoteSerializer(note, many=False)
    return Response(serializer.data)

def updateNote(request, pk):
    user = request.user
    data = request.data
    note = user.note_set.get(id=pk)
    serializer = NoteSerializer(instance=note, data=data)

    if serializer.is_valid():
        serializer.save()

    return serializer.data


def deleteNote(request, pk):
    user = request.user
    note = user.note_set.get(id=pk)
    note.delete()
    return Response('Note was deleted!')
