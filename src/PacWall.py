from games.TankMan.src.GameFramework.Props import Props


class PacWall(Props):
    def update(self, *args, **kwargs) -> None:
        pass

    def get_info(self):
        info = {"id": f"wall_{self._id}", "x": self.rect.x, "y": self.rect.y}
        return info

    def get_image_data(self):
        image_data = {"id": f"wall_{self._id}", "x": self.rect.x, "y": self.rect.y,
                      "width": self.rect.width, "height": self.rect.height, "angle": 0}
        return image_data
