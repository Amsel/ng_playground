from django.db import models
from django.contrib.auth.models import User


# can be an NPC or Player Character
# This will move out of this app later, since it is just referenced
class Character(models.Model):
    first_name = models.CharField(max_length=127)
    last_name = models.CharField(max_length=127)

    # the owner of the character
    user = models.OneToOneField(User)


# generic categorization mechanism
class PlayerCreationCategory(models.Model):
    name = models.CharField(max_length=127)

    def __str__(self):
        return self.name


class UseCase(models.Model):
    name = models.CharField(max_length=127)

    def __str__(self):
        return self.name


# generic grouping mechanism
class EffectCategory(models.Model):
    name = models.CharField(max_length=127)

    def __str__(self):
        return self.name


class Effect(models.Model):
    name = models.CharField(max_length=127)
    description = models.TextField()
    category = models.ManyToManyField(EffectCategory)

    # restricts, for what the effect can be used
    # still pretty generic
    use_case = models.ForeignKey(UseCase)

    # this describes the aspect which gets modified by the Effect
    # not clear yet how to attach this to something
    # without building hard dependencies
    target_aspect = models.CharField(max_length=127)

    # various states needed for the approval process
    # smells like it could be factored out into another model,
    # especially if this process becomes more complex
    user_accepted = models.BooleanField(default=False)
    admin_accepted = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def is_pending(self):
        return self.user_accepted and self.admin_accepted


class PlayerCreation(models.Model):
    name = models.CharField(max_length=127)
    description = models.TextField(blank=True)

    # assume, that the User can be always retrieved from the Character!
    creator = models.OneToOneField(Character)
    category = models.ForeignKey(PlayerCreationCategory, null=True)

    effects = models.ManyToManyField(Effect)

    # various states needed for the approval process
    # smells like it could be factored out into another model,
    # especially if this process becomes more complex
    user_accepted = models.BooleanField(default=False)
    admin_accepted = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def is_pending(self):
        return self.user_accepted and self.admin_accepted
