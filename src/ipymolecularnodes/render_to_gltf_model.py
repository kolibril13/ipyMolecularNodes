import bpy
from pathlib import Path
import molecularnodes as mn

def apply_mods(obj):
    """
    Applies the modifiers on the modifier stack

    This will realise the computations inside of any Geometry Nodes modifiers, ensuring
    that the result of the node trees can be compared by looking at the resulting
    vertices of the object.
    """
    bpy.context.view_layer.objects.active = obj
    for modifier in obj.modifiers:
        bpy.ops.object.modifier_apply(modifier = modifier.name)

def render_to_gltf_structure(counter, light_position):
    # Ensure the glTF exporter is activated
    bpy.ops.preferences.addon_enable(module='io_scene_gltf2')

    # Delete all mesh objects from the scene
    bpy.ops.object.select_all(action="DESELECT")
    bpy.ops.object.select_by_type(type="MESH")
    bpy.ops.object.delete()

    torus = mn.load.molecule_rcsb('6N2Y', starting_style = "cartoon", center_molecule = True)
    torus.scale = [10, 10, 10]
    apply_mods(torus)

    # Light
    light = bpy.data.objects["Light"]
    light.location = (0, 0, 2)  # Position the light

    # Exporting the model to .glb format for Three.js
    # Specify the path where you want to save the exported model
    gltf_path = Path() / "_MY_MODEL_DATA.gltf"

    # Select only the torus object
    bpy.ops.object.select_all(action='DESELECT')
    torus.select_set(True)

    # Export the selected torus object to a .glb file
    bpy.ops.export_scene.gltf(filepath=str(gltf_path), export_format='GLTF_EMBEDDED', use_selection=True)


    data = gltf_path.read_text()
    gltf_path.unlink()

    return data
