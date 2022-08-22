from games.TankMan.src.GameFramework import Props

DOT_IMG_ID = "dots"


class Dot(Props):
    def update(self, *args, **kwargs) -> None:
        pass

    def get_info(self):
        info = {"id": DOT_IMG_ID, "x": self.rect.x, "y": self.rect.y}
        return info

    def get_image_data(self):
        image_data = {"id": DOT_IMG_ID, "x": self.rect.x, "y": self.rect.y,
                      "width": self.rect.width, "height": self.rect.height, "angle": 0}
        return image_data
