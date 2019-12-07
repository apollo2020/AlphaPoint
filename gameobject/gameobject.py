from uuid import uuid4


class GameObject(object):
    """Base class for all game objects."""

    def __init__(self, *args, **kwargs):
        self.id = str(uuid4())
        self.config_id = None
        self.name = ''
        self.description = 'game object'
        self.visible = True
        self.interactive = True
        self.blocking = False
        self.x = 0
        self.y = 0

    def __str__(self):
        """A brief description."""

        return self.description

    def location(self):
        """Return the (x, y) location of the item."""

        return self.x, self.y