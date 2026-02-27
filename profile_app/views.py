from rest_framework.views import APIView
from rest_framework.response import Response

class ProfileView(APIView):
    def get(self, request):
        data = {
           
  "name": "Luis Pacheco",
  "role": "Backend Developer",
  "bio": "Desarrollador backend en constante aprendizaje, enfocado en expandir mis habilidades y conocimientos en Python y Django. Disfruto enfrentando desafíos de programación y construyendo aplicaciones funcionales mientras sigo explorando nuevas tecnologías y mejores prácticas. Me interesa crear soluciones simples y efectivas, mejorar mi comprensión de APIs, bases de datos y estructuras de datos, y aprender constantemente para crecer como desarrollador.",
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