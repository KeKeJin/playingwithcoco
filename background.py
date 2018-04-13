class BackgroundLayer(Layer):

    def __init__(self):
        # always call super()
        super(BackgroundLayer, self).__init__()

        # load the image form file
        self.image = pyglet.resource.image('flag.png')

    def draw(self):
        # blit the image on every frame
        self.image.blit(0, 0)