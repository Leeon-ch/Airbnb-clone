from django.db import models


class TimeStampedModel(models.Model):

    """ Time Stamped Model Definition """

    # auto_now_add=True
    # Automatically set the field to now when the object is first created.
    # Useful for creation of timestamps.
    created = models.DateTimeField(auto_now_add=True)

    # auto_now=True
    # Automatically set the field to now every time the object is saved.
    # Useful for "last-modified" timestamps.
    updated = models.DateTimeField(auto_now=True)

    # I wnat this for the other models
    # but I don't want db has this contents

    class Meta:
        abstract = True

    # abstract model is we can use but not shown on the db
