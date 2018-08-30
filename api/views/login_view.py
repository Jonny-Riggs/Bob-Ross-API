import json
from django.http import HttpResponse
from django.contrib.auth.models import User
from api.models import Customer

from rest_framework.authtoken.models import Token
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def login_user(request):
    req_body = json.loads(request.body.decode())

