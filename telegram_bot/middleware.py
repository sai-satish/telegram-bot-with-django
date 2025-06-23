# your_project/your_app/middleware.py

import jwt
import logging
from django.conf import settings
from django.contrib.auth.models import User
from django.http import JsonResponse

logger = logging.getLogger(__name__)

class JWTAuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        token = request.COOKIES.get("jwt")
        
        if token:
            try:
                # Decode the JWT token
                payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
                user = User.objects.get(id=payload['user_id'])
                request.user = user
                logger.info(f"Authenticated user: {user.username}")  # Log the authenticated user
            except jwt.ExpiredSignatureError:
                logger.error("Token has expired")
                return JsonResponse({"error": "Token has expired"}, status=401)
            except jwt.DecodeError:
                logger.error("Error decoding token")
                return JsonResponse({"error": "Error decoding token"}, status=400)
            except User.DoesNotExist:
                logger.error("User does not exist")
                return JsonResponse({"error": "User not found"}, status=404)
        else:
            request.user = None
            logger.info("No JWT token found, user not authenticated.")

        response = self.get_response(request)
        return response
