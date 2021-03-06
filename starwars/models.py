# Models and fixtures taked from Swapi
# Swapi URL project: https://github.com/phalt/swapi/
# https://github.com/phalt/swapi/blob/master/resources/models.py

from django.db import models


class DateTimeModel(models.Model):
    """ A base model with created and edited datetime fields """

    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Planet(DateTimeModel):
    """ A planet i.e. Tatooine """

    name = models.CharField(max_length=100)
    rotation_period = models.CharField(max_length=40)
    orbital_period = models.CharField(max_length=40)
    diameter = models.CharField(max_length=40)
    climate = models.CharField(max_length=40)
    gravity = models.CharField(max_length=40)
    terrain = models.CharField(max_length=40)
    surface_water = models.CharField(max_length=40)
    population = models.CharField(max_length=40)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class People(DateTimeModel):
    """ A person i.e. - Luke Skywalker """

    name = models.CharField(max_length=100)
    height = models.CharField(max_length=10, blank=True)
    mass = models.CharField(max_length=10, blank=True)
    hair_color = models.CharField(max_length=20, blank=True)
    skin_color = models.CharField(max_length=20, blank=True)
    eye_color = models.CharField(max_length=20, blank=True)
    birth_year = models.CharField(max_length=10, blank=True)
    gender = models.CharField(max_length=40, blank=True)
    homeworld = models.ForeignKey(Planet, related_name="residents", on_delete=models.CASCADE)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class Transport(DateTimeModel):
    name = models.CharField(max_length=40)
    model = models.CharField(max_length=40)
    manufacturer = models.CharField(max_length=80)
    cost_in_credits = models.CharField(max_length=40)
    length = models.CharField(max_length=40)
    max_atmosphering_speed = models.CharField(max_length=40)
    crew = models.CharField(max_length=40)
    passengers = models.CharField(max_length=40)
    cargo_capacity = models.CharField(max_length=40)
    consumables = models.CharField(max_length=40)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class Starship(Transport):
    """ A starship is a transport with a hypderdrive """

    hyperdrive_rating = models.CharField(max_length=40)
    MGLT = models.CharField(max_length=40)
    starship_class = models.CharField(max_length=40)
    pilots = models.ManyToManyField(
        People,
        related_name="starships",
        blank=True
    )

    def __str__(self):
        return self.name


class Vehicle(Transport):
    """ A vehicle is anything without hyperdrive capability """

    vehicle_class = models.CharField(max_length=40)
    pilots = models.ManyToManyField(
        People,
        related_name="vehicles",
        blank=True
    )


class Species(DateTimeModel):
    "A species is a type of alien or person"

    name = models.CharField(max_length=40)
    classification = models.CharField(max_length=40)
    designation = models.CharField(max_length=40)
    average_height = models.CharField(max_length=40)
    skin_colors = models.CharField(max_length=200)
    hair_colors = models.CharField(max_length=200)
    eye_colors = models.CharField(max_length=200)
    average_lifespan = models.CharField(max_length=40)
    homeworld = models.ForeignKey(Planet, blank=True, null=True, on_delete=models.CASCADE)
    language = models.CharField(max_length=40)
    people = models.ManyToManyField(People, related_name="species")

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class Film(DateTimeModel):
    """ A film i.e. The Empire Strikes Back (which is also the best film) """
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100)
    episode_id = models.IntegerField()
    opening_crawl = models.TextField(max_length=1000)
    director = models.CharField(max_length=100)
    producer = models.CharField(max_length=100)
    release_date = models.DateField(null=True)
    characters = models.ManyToManyField(
        People,
        related_name="films",
        blank=True
    )
    planets = models.ManyToManyField(
        Planet,
        related_name="films",
        blank=True
    )

    starships = models.ManyToManyField(
        Starship,
        related_name="films",
        blank=True
    )
    vehicles = models.ManyToManyField(
        Vehicle,
        related_name="films",
        blank=True
    )
    species = models.ManyToManyField(
        Species,
        related_name="films",
        blank=True
    )

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title


class Hero(DateTimeModel):
    name = models.CharField(max_length=100)
    homeworld = models.ForeignKey(Planet, related_name="heroes", on_delete=models.CASCADE)
