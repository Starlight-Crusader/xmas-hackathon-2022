from rest_framework import generics, status, response
from rest_framework.decorators import api_view
from students import serializers, models


@api_view(['GET'])
def create_student(request):
    try:
        student = models.Student.objects.create(name=request.query_params.get('name'))
        student.save()
    except models.Student.DoesNotExist:
        return response.Response('Something went wrong.',
                                status=status.HTTP_400_BAD_REQUEST)

    data = {
        "question_text": "Successfully added a new record!"
    }

    return response.Response(data)


@api_view(['GET'])
def delete_student(request):
    try:
        student = models.Student.objects.delete(name=request.query_params.get('name'))
        student.save()
    except models.Student.DoesNotExist:
        return response.Response('Unable to find this record.',
                                status=status.HTTP_400_BAD_REQUEST)

    data = {
        "question_text": "Successfully deleted a record!"
    }

    return response.Response(data)


class StudentsList(generics.ListAPIView):
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer
