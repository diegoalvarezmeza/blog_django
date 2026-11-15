from django.shortcuts import render

def inicio(request):
    return render(request, "posts/inicio.html")
def lista_posts(request):
    posts = [
        {"id": 1, "titulo": "Mi primer post", "autor": "Ana"},
        {"id": 2, "titulo": "Aprendiendo Django", "autor": "Luis"},
        {"id": 3, "titulo": "Rutas y vistas", "autor": "Marta"},
    ]
    return render(request, "posts/lista_posts.html", {"posts": posts})

def acerca(request):
    return render(request, "posts/acerca.html")