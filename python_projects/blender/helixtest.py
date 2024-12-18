import bpy
import math

def create_collections():
    # Create a collection for toruses
    if "TorusCollection" not in bpy.data.collections:
        torus_collection = bpy.data.collections.new("TorusCollection")
        bpy.context.scene.collection.children.link(torus_collection)
    
    if "HelixCollection" not in bpy.data.collections:
        helix_collection = bpy.data.collections.new("HelixCollection")
        bpy.context.scene.collection.children.link(helix_collection)
        
    if "CameraCollection" not in bpy.data.collections:
        camera_collection = bpy.data.collections.new("CameraCollection")
        bpy.context.scene.collection.children.link(camera_collection)
        
    if "LightCollection" not in bpy.data.collections:
        light_collection = bpy.data.collections.new("LightCollection")
        bpy.context.scene.collection.children.link(light_collection)
        
    if "PathCollection" not in bpy.data.collections:
        path_collection = bpy.data.collections.new("PathCollection")
        bpy.context.scene.collection.children.link(path_collection)
    
    if "CubeCollection" not in bpy.data.collections:
        cube_collection = bpy.data.collections.new("CubeCollection")
        bpy.context.scene.collection.children.link(cube_collection)
        
def unlink_from_original_collection(obj):
    """Unlink the object from its original collection."""
    for collection in obj.users_collection:
        collection.objects.unlink(obj)

def clear_scene():
    """Delete all objects in the current Blender scene."""
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete()

def add_curveaceous_galore_shape(i):
    """Add a helix shape using the Curveaceous Galore addon (if available)."""
    if hasattr(bpy.ops.curve, "curveaceous_galore"):
        bpy.ops.curve.curveaceous_galore(
            align='WORLD',
            location=(0, 0, 0),
            rotation=(0, 0, (18* i)),
            ProfileType='Helix',
            shape='3D',
            use_cyclic_u=False,
            helixPoints=250,
            helixHeight=5,
            helixEnd=1080,
            helix_a=1
        )
        helix = bpy.context.object
        helix.name = f"helix{i}"
        
        unlink_from_original_collection(helix)
        
        helix_collection = bpy.data.collections.get("HelixCollection")
        if helix_collection:
            helix_collection.objects.link(helix)
        return helix
    else:
        print("The operator 'curve.curveaceous_galore' is not available. Ensure the addon is installed and enabled.")
        return None

def add_torus(i):
    """Add a torus to the scene."""
    if hasattr(bpy.ops.mesh, "primitive_torus_add"):
        bpy.ops.mesh.primitive_torus_add(
            align='WORLD',
            location=(0, 0, 0), 
            rotation=(0, 0, 0), 
            major_radius=0.025, 
            minor_radius=0.0125, 
            abso_major_rad=1.25,
            abso_minor_rad=0.75
        )
        torus = bpy.context.object
        torus.name = f"torus{i}"
        
        unlink_from_original_collection(torus)
        
        torus_collection = bpy.data.collections.get("TorusCollection")
        if torus_collection:
            torus_collection.objects.link(torus)
        
        return torus  # Return the created torus
    else:
        print("Error adding torus")
        return None
    
    
def add_path():
    """Add a basic NURBS path to the scene.""" # this should be dynamic to the heigh of the spiral will have to change
    if hasattr(bpy.ops.curve,"primitive_nurbs_path_add"):
        bpy.ops.curve.primitive_nurbs_path_add(
            align='WORLD', 
            location=(0, 0, 2), 
            rotation=(0, math.radians(-90), 0),
            scale=(1, 1, 1.5)
        )
        path = bpy.context.object
        
        unlink_from_original_collection(path)
        
        path_collection = bpy.data.collections.get("PathCollection")
        if path_collection:
            path_collection.objects.link(path)
            
        return path

def add_cube():
    if hasattr(bpy.ops.mesh, "primitive_cube_add"):
        bpy.ops.mesh.primitive_cube_add(
            align="WORLD",
            location=(0, 0, 0),
            rotation=(0, 0, 0),
            scale=(0.01, 0.01, 0.01)
        )
        cube = bpy.context.object  # Get the created cube
        cube.name = "CameraCube"
        cube.hide_render = True
        
        unlink_from_original_collection(cube)
        
        cube_collection = bpy.data.collections.get("CubeCollection")
        if cube_collection:
            cube_collection.objects.link(cube)
            
        return cube
    
def add_plane():
    if hasattr(bpy.ops.mesh, "primitive_plane_add"):
        bpy.ops.mesh.primitive_plane_add(
            align="WORLD",
            location=(0, 0, 0),
            rotation=(0, 0, 0),
            scale=(5, 5, 0.1)
        )
        plane = bpy.context.object  # Get the created cube
        plane.name = "plane"
        
        unlink_from_original_collection(plane)
        
        cube_collection = bpy.data.collections.get("CubeCollection")
        if cube_collection:
            cube_collection.objects.link(plane)
            
        return plane
    
def parent_to_curve_with_animation(obj, curve, frame_start=1, frame_end=250):
    """Parent an object to a curve and animate it along the path."""
    # Deselect all objects
    bpy.ops.object.select_all(action='DESELECT')

    # Ensure the curve has Path Animation enabled
    curve.data.use_path = True  # Enable path animation
    curve.data.path_duration = frame_end - frame_start + 1  # Set duration

    # Add Follow Path constraint
    obj.select_set(True)
    bpy.context.view_layer.objects.active = obj
    constraint = obj.constraints.new(type='FOLLOW_PATH')
    constraint.target = curve
    constraint.use_curve_follow = True  # Align to curve
    constraint.offset_factor = 0.0
    constraint.use_fixed_location = True  # Ensures consistent start position

    # Animate offset_factor from 0 to 1 over the specified frame range
    obj.animation_data_clear()  # Clear existing animations
    constraint.keyframe_insert(data_path="offset_factor", frame=frame_start)
    constraint.offset_factor = 1.0
    constraint.keyframe_insert(data_path="offset_factor", frame=frame_end)

    print(f"Animation added: {frame_start} -> {frame_end}")
    return constraint


def create_glowing_material(color=(1, 0, 0, 1), strength=5):
    """Create a glowing emission material."""
    # Create a new material
    material = bpy.data.materials.new(name="GlowingMaterial")
    material.use_nodes = True

    # Get the material's node tree and clear default nodes
    nodes = material.node_tree.nodes
    nodes.clear()  # Remove all default nodes (e.g., Principled BSDF)

    # Add Emission Node
    emission_node = nodes.new(type='ShaderNodeEmission')
    emission_node.location = (0, 0)
    emission_node.inputs['Color'].default_value = color
    emission_node.inputs['Strength'].default_value = strength

    # Add Material Output Node
    material_output_node = nodes.new(type='ShaderNodeOutputMaterial')
    material_output_node.location = (200, 0)

    # Link Emission to Material Output
    material.node_tree.links.new(emission_node.outputs['Emission'], material_output_node.inputs['Surface'])

    return material

def setup_camera(location=(3, 0, 1), rotation=(1.1, 0, 1.5)):
    """Create and position the camera in the scene, with optional object focus."""
    # Add the camera
    bpy.ops.object.camera_add(location=location)
    camera = bpy.context.object
    camera.rotation_euler = rotation
    bpy.context.scene.camera = camera  # Set as active camera

    # Enable Depth of Field
    camera.data.dof.use_dof = True

    # Set the camera's focus target to the object
    #bpy.context.object.data.dof.focus_object = bpy.data.objects["CameraCube"]
    camera.data.dof.focus_object = bpy.data.objects["CameraCube"]
    print(f"Camera DOF focus set to object")

    # Enable Bloom in Eevee
    if bpy.context.scene.render.engine == 'BLENDER_EEVEE':
        bpy.context.scene.eevee.bloom = True
        bpy.context.scene.eevee.bloom_intensity = 0.5
        bpy.context.scene.eevee.bloom_threshold = 1.0
    
    unlink_from_original_collection(camera)
        
    camera_collection = bpy.data.collections.get("CameraCollection")
    if camera_collection:
        camera_collection.objects.link(camera)
    return camera

def set_camera_to_follow_path_and_cube(camera, nurbs_path, CameraCube, frame_start=1, frame_end=250):

    bpy.ops.object.select_all(action='DESELECT')

    if camera and nurbs_path:
        camera.select_set(True)

        # sets follow path constraint to the camera
        follow_path_camera_constraint = camera.constraints.new(type="FOLLOW_PATH")
        follow_path_camera_constraint.target = nurbs_path  # Set the target to the NURBS path

        follow_path_camera_constraint.offset_factor = 0.0
        follow_path_camera_constraint.use_fixed_location = True

        follow_path_camera_constraint.keyframe_insert(data_path="offset_factor", frame=frame_start)
        follow_path_camera_constraint.offset_factor = 1.0
        follow_path_camera_constraint.keyframe_insert(data_path="offset_factor", frame=frame_end)

        #sets track_to
        track_constraint = camera.constraints.new(type="TRACK_TO")
        track_constraint.target = CameraCubeData

        #deselect
        bpy.ops.object.select_all(action='DESELECT')

        CameraCubeData.select_set(True)
        follow_path_cube_constraint = CameraCubeData.constraints.new(type="FOLLOW_PATH")
        follow_path_cube_constraint.target = nurbs_path  # Set the target to the NURBS path

        copy_loc_constraint = CameraCubeData.constraints.new(type="COPY_LOCATION")
        copy_loc_constraint.target = torus  # Set the target to the NURBS path
        copy_loc_constraint.use_x = False
        copy_loc_constraint.use_y = False
    else:
        print("Error: Either 'Camera' or 'NurbsPath' not found!")


def add_light(location=(5, 5, 5), light_type='SUN', energy=3.0):
    """Add a light source to the scene."""
    bpy.ops.object.light_add(type=light_type, location=location)
    light = bpy.context.object
    light.data.energy = energy  # Adjust brightness
    print(f"Added {light_type} light at {location}")
    
    unlink_from_original_collection(light)
        
    light_collection = bpy.data.collections.get("LightCollection")
    if light_collection:
        light_collection.objects.link(light)    

def render(resolution=(1920, 1080), frame_rate=24, start_frame=1, end_frame=250):
    """Set render parameters and render the animation."""
    
    # Set the resolution
    bpy.context.scene.render.resolution_x = resolution[0]
    bpy.context.scene.render.resolution_y = resolution[1]
    bpy.context.scene.render.resolution_percentage = 100  # 100% scale of the resolution

    # Set the frame rate
    bpy.context.scene.render.fps = frame_rate

    # Set the start and end frame for rendering
    bpy.context.scene.frame_start = start_frame
    bpy.context.scene.frame_end = end_frame

    # Set the  format (e.g., MP4, AVI, etc.)
    bpy.context.scene.render.image_settings.file_format = 'FFMPEG'
    bpy.context.scene.render.ffmpeg.format = 'MPEG4'  # Video format
    bpy.context.scene.render.ffmpeg.codec = 'H264'  # Codec for MP4

    # Set video encoding options
    bpy.context.scene.render.ffmpeg.constant_rate_factor = 'HIGH'  # Set the video quality
    bpy.context.scene.render.ffmpeg.audio_codec = 'AAC'  # Audio codec if there's any audio
    
    # Start rendering the animation
    print(f"Rendering animation from frame {start_frame} to {end_frame}")
    bpy.ops.render.render(animation=True, write_still=False)

    print("Rendering complete.")

# Ensure we're in the right context (e.g., Object Mode)
if bpy.context.mode != 'OBJECT':
    bpy.ops.object.mode_set(mode='OBJECT')


# Clear the scene
clear_scene()

create_collections()
material = create_glowing_material(color=(1, 0.0, 1, 1.0))
add_plane()
# Create helix and torus
for i in range(21):
    helix = add_curveaceous_galore_shape(i)
    torus = add_torus(i)
    parent_to_curve_with_animation(torus, helix)    
    material = bpy.data.materials.get("GlowingMaterial")
    torus.data.materials.append(material)
    
add_path()
add_cube()
CameraCube = bpy.context.object.get("CameraCube")
setup_camera()
add_light()

CameraCubeData = bpy.data.objects.get("CameraCube")
torus = bpy.data.objects.get("torus0")
camera = bpy.data.objects.get("Camera")
nurbs_path = bpy.data.objects["NurbsPath"]
set_camera_to_follow_path_and_cube(camera, nurbs_path, CameraCube)

#render()