from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import RegisterSerializer
from .tasks import send_welcome_email_task

BookshelfUser = get_user_model()


class UserRegisterView(APIView):
    def post(self, request):
        """
        Post request for registration. Contains celery task.
        :param request:
        :return:
        """
        data = request.data
        serializer = RegisterSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            send_welcome_email_task.delay(user.username, user.email)
        return Response('User created', status=status.HTTP_200_OK)


class LoginView(APIView):
    """
    not implemented
    """
    pass
