from display_surface import DisplaySurface


class ScreenDisplaySurface(DisplaySurface):

    instance = None
    calls = 0

    @classmethod
    def get_display_surface(cls):

        return cls.instance

    @classmethod
    def instantiate_display(cls, w, h):
        if cls.calls > 0:
            raise Exception('multiple root displays not allowed')
        else:
            cls.calls += 1
        cls.instance = cls(w, h)

    def __init__(self, w, h):

        DisplaySurface.__init__(self, w, h, refresh=True)
