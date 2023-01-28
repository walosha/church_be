from rest_framework.authentication import TokenAuthentication as BaseAuthentication

class TokenAuthentication(BaseAuthentication):
    keyword ='Bearer'