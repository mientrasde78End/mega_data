from rest_framework.views import APIView
from rest_framework.response import Response

class ProfileView(APIView):
    def get(self, request):
        data = {
           
  "name": "Luis Pacheco",
  "role": "Backend Developer",
  "bio": "Desarrollador apasionado por crear aplicaciones reales y resolver problemas con código.",
  "location": "Perú",
  "links": {
    "github": "https://github.com/mientrasde78End",
    "linkedin": ""
  }

        }
        return Response(data)

class SkillsView(APIView):
    def get(self, request):
        skills = [
            {"name": "Python"},
            {"name": "Django"},
            {"name": "React"},
        ]
        return Response(skills)