from rest_framework.views import APIView
from rest_framework.response import Response

class ProfileView(APIView):
    def get(self, request):
        data = {
            "name": "Luis Pacheco",
            "role": "Backend / Fullstack Developer",
            "bio": "Desarrollador enfocado en construir software limpio y funcional.",
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