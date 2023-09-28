import bpy
import base64
from pathlib import Path

import molecularnodes as mn


def render_to_image(counter, light_position):
    temp_filepath = Path(bpy.context.scene.render.filepath)
    with temp_filepath.open("rb") as f:
        my_img = base64.b64encode(f.read()).decode("utf-8")

    temp_filepath.unlink()

    return "data:image/png;base64," + my_img
