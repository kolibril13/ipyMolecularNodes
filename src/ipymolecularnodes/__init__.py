import importlib.metadata
import pathlib
import anywidget
from traitlets import Unicode

try:
    __version__ = importlib.metadata.version("ipymolecularnodes")
except importlib.metadata.PackageNotFoundError:
    __version__ = "unknown"


class BlenderInteractiveWidget(anywidget.AnyWidget):

    torusname = Unicode("").tag(sync=True)

    _esm = pathlib.Path(__file__).parent / "static" / "interactive_widget.js"
    # _css = pathlib.Path(__file__).parent / "static" / "widget.css"
