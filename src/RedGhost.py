from mlgame.view.view_model import create_image_view_data

from .Ghost import Ghost

GO_OUT_FRAME = 60


class RedGhost(Ghost):
    def __init__(self, construction, **kwargs):
        super().__init__(construction, **kwargs)
        self.image_id = "red_ghost"
        self.go_out_frame = GO_OUT_FRAME

    def update(self):
        super().update()
        if self.is_blue:
            self.image_id = "blue_ghost"
        else:
            self.image_id = "red_ghost"