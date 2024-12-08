import django_startup
from games.models import Genre, Games

# Genre.objects.create(title = "arcada")
# Genre.objects.create(title = "shooter")
arcada = Genre.objects.get(id=1)

Games.objects.get(id=2).genre.add(arcada)

# game1 = Games.objects.get(id=1)
# game1.genre.add(arcada)
# game1.save()