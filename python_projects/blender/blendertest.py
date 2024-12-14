import bpy

# Create a helix (spiral) spline
bpy.ops.curve.primitive_bezier_circle_add(radius=1)
spline = bpy.context.object.data

# Move the curve along the Z-axis for spiral effect
for i, point in enumerate(spline.splines[0].bezier_points):
    point.co.z = i * 0.1  # Change this value for more/less height
    point.co.x = i * 0.1  # Adjust this for spiral effect along X-axis
