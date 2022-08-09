import math
import bpy

ob = bpy.data.objects['root']
bpy.context.view_layer.objects.active = ob
bpy.ops.object.mode_set(mode='POSE')

pbone = ob.pose.bones['upperarm_l']
# Set rotation mode to Euler XYZ, easier to understand
# than default quaternions
pbone.rotation_mode = 'XYZ'
# select axis in ['X','Y','Z']  <--bone local
axis = 'X'
angle = 5.31
pbone.rotation_euler.rotate_axis(axis, math.radians(angle))
axis = 'Y'
angle = -59
pbone.rotation_euler.rotate_axis(axis, math.radians(angle))
axis = 'Z'
angle = -6.68
pbone.rotation_euler.rotate_axis(axis, math.radians(angle))
pbone.keyframe_insert(data_path="rotation_euler" ,frame=1)



pbone = ob.pose.bones['upperarm_r']
# Set rotation mode to Euler XYZ, easier to understand
# than default quaternions
pbone.rotation_mode = 'XYZ'
# select axis in ['X','Y','Z']  <--bone local
axis = 'X'
angle = 5.31
pbone.rotation_euler.rotate_axis(axis, math.radians(angle))
axis = 'Y'
angle = -59
pbone.rotation_euler.rotate_axis(axis, math.radians(angle))
axis = 'Z'
angle = -6.68
pbone.rotation_euler.rotate_axis(axis, math.radians(angle))
pbone.keyframe_insert(data_path="rotation_euler" ,frame=1)


pbone = ob.pose.bones['lowerarm_l']
# Set rotation mode to Euler XYZ, easier to understand
# than default quaternions
pbone.rotation_mode = 'XYZ'
# select axis in ['X','Y','Z']  <--bone local
axis = 'X'
angle = 1.4
pbone.rotation_euler.rotate_axis(axis, math.radians(angle))
axis = 'Y'
angle = 3.19
pbone.rotation_euler.rotate_axis(axis, math.radians(angle))
axis = 'Z'
angle = 48.8
pbone.rotation_euler.rotate_axis(axis, math.radians(angle))
pbone.keyframe_insert(data_path="rotation_euler" ,frame=1)


pbone = ob.pose.bones['lowerarm_r']
# Set rotation mode to Euler XYZ, easier to understand
# than default quaternions
pbone.rotation_mode = 'XYZ'
# select axis in ['X','Y','Z']  <--bone local
axis = 'X'
angle = 3.19
pbone.rotation_euler.rotate_axis(axis, math.radians(angle))
axis = 'Y'
angle = 1.4
pbone.rotation_euler.rotate_axis(axis, math.radians(angle))
axis = 'Z'
angle = 48.8
pbone.rotation_euler.rotate_axis(axis, math.radians(angle))
pbone.keyframe_insert(data_path="rotation_euler" ,frame=1)


pbone = ob.pose.bones['hand_l']
# Set rotation mode to Euler XYZ, easier to understand
# than default quaternions
pbone.rotation_mode = 'XYZ'
# select axis in ['X','Y','Z']  <--bone local
axis = 'X'
angle = -22.3
pbone.rotation_euler.rotate_axis(axis, math.radians(angle))
axis = 'Y'
angle = 0
pbone.rotation_euler.rotate_axis(axis, math.radians(angle))
axis = 'Z'
angle = 0
pbone.rotation_euler.rotate_axis(axis, math.radians(angle))
pbone.keyframe_insert(data_path="rotation_euler" ,frame=1)


pbone = ob.pose.bones['hand_r']
# Set rotation mode to Euler XYZ, easier to understand
# than default quaternions
pbone.rotation_mode = 'XYZ'
# select axis in ['X','Y','Z']  <--bone local
axis = 'X'
angle = -22.3
pbone.rotation_euler.rotate_axis(axis, math.radians(angle))
axis = 'Y'
angle = 0
pbone.rotation_euler.rotate_axis(axis, math.radians(angle))
axis = 'Z'
angle = 0
pbone.rotation_euler.rotate_axis(axis, math.radians(angle))
pbone.keyframe_insert(data_path="rotation_euler" ,frame=1)

pbone = ob.pose.bones['thigh_l']
# Set rotation mode to Euler XYZ, easier to understand
# than default quaternions
pbone.rotation_mode = 'XYZ'
# select axis in ['X','Y','Z']  <--bone local
axis = 'X'
angle = -5
pbone.rotation_euler.rotate_axis(axis, math.radians(angle))
axis = 'Y'
angle = 2.54
pbone.rotation_euler.rotate_axis(axis, math.radians(angle))
axis = 'Z'
angle = 0
pbone.rotation_euler.rotate_axis(axis, math.radians(angle))
pbone.keyframe_insert(data_path="rotation_euler" ,frame=1)

pbone = ob.pose.bones['thigh_r']
# Set rotation mode to Euler XYZ, easier to understand
# than default quaternions
pbone.rotation_mode = 'XYZ'
# select axis in ['X','Y','Z']  <--bone local
axis = 'X'
angle = -5
pbone.rotation_euler.rotate_axis(axis, math.radians(angle))
axis = 'Y'
angle = 2.54
pbone.rotation_euler.rotate_axis(axis, math.radians(angle))
axis = 'Z'
angle = 0
pbone.rotation_euler.rotate_axis(axis, math.radians(angle))
pbone.keyframe_insert(data_path="rotation_euler" ,frame=1)

#bpy.ops.object.mode_set(mode='OBJECT')
