from django.db import models
from django.contrib.auth.models import User

class Outfit(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='outfits/')

    def __str__(self):
        return self.name
    
class Clothing(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='clothes/')
    price = models.IntegerField()
    bonus = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Toy(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='toys/')
    price = models.IntegerField()
    bonus = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    
class Cat(models.Model):
    name = models.CharField(max_length=100, default="Микки")
    level = models.IntegerField(default=0)
    last_petted_date = models.DateTimeField(null=True, blank=True)
    current_outfit = models.ForeignKey(Outfit, on_delete=models.CASCADE)
    current_clothing = models.ForeignKey(Clothing, on_delete=models.CASCADE, null=True, blank=True, related_name='current_clothing_for_cats')
    current_toy = models.ForeignKey(Toy, on_delete=models.CASCADE, null=True, blank=True, related_name='current_toy_for_cats')
    wardrobe = models.ManyToManyField(Clothing, blank=True, related_name='cats_with_wardrobe')
    inventory = models.ManyToManyField(Toy, blank=True, related_name='cats_with_inventory')

    def __str__(self):
        return f"{self.name} (уровень {self.level})"
    
class Pair(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cat = models.OneToOneField(Cat, on_delete=models.CASCADE)
    coins = models.IntegerField(default=0)

    def __str__(self):
        return f"Аккаунт пары {self.user.username}"

class WeatherChoices(models.TextChoices):
    SUNNY = 'Sunny', 'Солнечно'
    RAINY = 'Rainy', 'Дождливо'
    SNOWY = 'Snowy', 'Снег'
    CLOUDY = 'Cloudy', 'Облачно'
    STORM = 'Storm', 'Гроза'
    FOGGY = 'Foggy', 'Туманно'
    WINDY = 'Windy', 'Ветренно'
    ANY = 'Any', 'Любая'

class TimeChoices(models.TextChoices):
    MORNING = 'Morning', 'Утро'
    DAY = 'Day', 'День'
    EVENING = 'Evening', 'Вечер'
    NIGHT = 'Night', 'Ночь'
    ANY = 'Any', 'Любое'

class MoodChoices(models.TextChoices):
    BAD = 'Bad', 'Плохое'
    NORMAL = 'Normal', 'Нормальное'
    GOOD = 'Good', 'Хорошее'
    GREAT = 'Great', 'Отличное'
    PERFECT = 'Perfect', 'Замечательное'

class Idea(models.Model):
    title = models.CharField(max_length=100)
    weather = models.CharField(max_length=20, choices=WeatherChoices.choices)
    temperature = models.IntegerField()
    time = models.CharField(max_length=20, choices=TimeChoices.choices)
    budget = models.IntegerField()
    mood = models.CharField(max_length=20, choices=MoodChoices.choices)
    image = models.ImageField(upload_to='ideas/')
    pair = models.ForeignKey(Pair, on_delete=models.CASCADE, null=True, blank=True)
    is_checked = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Date(models.Model):
    title = models.CharField(max_length=100)
    comment = models.TextField(blank=True)
    image = models.ImageField(upload_to='dates/', null=True, blank=True)
    pair = models.ForeignKey(Pair, on_delete=models.CASCADE)
    idea = models.ForeignKey(Idea, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
