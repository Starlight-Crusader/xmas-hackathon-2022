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

    return response.Response('Successfully added a new record.',
                            status=status.HTTP_200_OK)


@api_view(['GET'])
def delete_student(request):
    try:
        student = models.Student.objects.delete(name=request.query_params.get('name'))
        student.save()
    except models.Student.DoesNotExist:
        return response.Response('Unable to find this record.',
                                status=status.HTTP_400_BAD_REQUEST)

    return response.Response('Successfully deleted a record.',
                            status=status.HTTP_200_OK)


@api_view(['GET'])
def list_students(request):
    try:
        records = models.Student.objects.all()
    except models.Student.DoesNotExist:
        return response.Response('User does not exist.',
                                status=status.HTTP_400_BAD_REQUEST)

    return response.Response(**serializer.data())
