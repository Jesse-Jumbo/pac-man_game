from games.PacMan.src.Ghost import Ghost

GO_OUT_FRAME = 1200


class OrangeGhost(Ghost):
    def __init__(self, _id: int, _no: int, x: int, y: int, width: int, height: int):
        super().__init__(_id, _no, x, y, width, height)
        self.image_id = "orange_ghost"
        self.go_out_frame = GO_OUT_FRAME

    def update_children(self):
        if self.is_blue:
            self.image_id = "blue_ghost"
        else:
            self.image_id = "orange_ghost"

    def get_image_data(self):
        image_data = {"id": f"{self.image_id}_{self.act_command}", "x": self.rect.x, "y": self.rect.y,
                      "width": self.rect.width, "height": self.rect.height, "angle": 0}
        return image_data

    def get_info(self):
        info = {"id": self.image_id, "x": self.rect.x, "y": self.rect.y, "speed": self.speed}
        return info
