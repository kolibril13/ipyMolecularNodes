import importlib.metadata
import pathlib
from .render_to_gltf_model import render_to_gltf_structure
import anywidget
from traitlets import Int, Unicode, observe,Float

try:
    __version__ = importlib.metadata.version("ipymolecularnodes")
except importlib.metadata.PackageNotFoundError:
    __version__ = "unknown"


class BlenderInteractiveWidget(anywidget.AnyWidget):
    label = Unicode("Color: ").tag(sync=True)

    model_data = render_to_gltf_structure(3, 10)
    torusname = Unicode(model_data).tag(sync=True)

    _esm = pathlib.Path(__file__).parent / "static" / "interactive_widget.js"
    # _css = pathlib.Path(__file__).parent / "static" / "widget.css"

