game_objects = []


def add(game_object):
    game_objects.append(game_object)


def update():
    print(len(game_objects))
    for game_object in game_objects:
        if game_object.is_active:
            game_object.update()


def render(canvas):
    for game_object in game_objects:
        if game_object.is_active:
            game_object.render(canvas)


def collide_with_enemy(box_collider, t):
    for game_object in game_objects:
        if game_object.is_active and type(game_object) == t:
            if game_object.box_collider.collide_with(box_collider):
                return game_object

    return None

def recyle(t, x, y):
    for game_object in game_objects:
        if not game_object.is_active and type(game_object) == t:
            game_object.is_active = True
            game_object.x = x
            game_object.y = y
            return game_object

    new_game_object = t(x, y)
    add(new_game_object)
    return new_game_object


class GameObject:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = None
        self.box_collider = None
        self.is_active = True

    def update(self):
        if self.box_collider is not None:
            self.box_collider.x = self.x
            self.box_collider.y = self.y

    def render(self, canvas):
        if self.image is not None:
            width = self.image.get_width()
            height = self.image.get_height()
            render_pos = (self.x - width / 2, self.y - height / 2)
            canvas.blit(self.image, render_pos)

        if self.box_collider is not None:
            self.box_collider.render(canvas)

    def deactivate(self):
        self.is_active = False