# # office/views.py
# from django.contrib.auth import authenticate, login
# from django.contrib.auth.models import User
# from rest_framework.authtoken.models import Token
# from rest_framework.authtoken.views import ObtainAuthToken
# from rest_framework.response import Response
# from rest_framework.views import APIView

# class UserProfileView(APIView):
#     def post(self, request, *args, **kwargs):
#         # Get username and password from request data
#         username = request.data.get('username', '')
#         password = request.data.get('password', '')

#         # Authenticate user
#         user = authenticate(request, username=username, password=password)

#         if user is not None:
#             # Login the user (optional, depends on your requirements)
#             login(request, user)

#             # Get or create a token for the user
#             token, created = Token.objects.get_or_create(user=user)

#             # Return the token
#             return Response({'token': token.key})
#         else:
#             # Return invalid credentials response
#             return Response({'error': 'Invalid credentials'}, status=401)

# class CustomAuthToken(ObtainAuthToken):
#     def post(self, request, *args, **kwargs):
#         serializer = self.serializer_class(data=request.data,
#                                            context={'request': request})
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data['user']
#         login(request, user)
#         token, created = Token.objects.get_or_create(user=user)
#         return Response({'token': token.key})

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response({'username': user.username, 'email': user.email})
