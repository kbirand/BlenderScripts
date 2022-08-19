import bpy

def print(data):
    for window in bpy.context.window_manager.windows:
        screen = window.screen
        for area in screen.areas:
            if area.type == 'CONSOLE':
                override = {'window': window, 'screen': screen, 'area': area}
                bpy.ops.console.scrollback_append(override, text=str(data), type="OUTPUT")  

for o in ("Body.001", "Face.001"):
    obj = bpy.context.scene.objects.get(o)
    if obj:
        obj.select_set(True)
        obj.parent_type = 'ARMATURE'
        obj.parent_type = 'OBJECT'

ob = bpy.data.objects['root.001']
bpy.context.view_layer.objects.active = ob
bpy.ops.object.mode_set(mode='POSE')

ob.pose.bones['pelvis'].rotation_quaternion = [0.656,-0.755,-0.027,0]
ob.pose.bones['upperarm_l'].rotation_quaternion = [0.865,0.0,-0.5,0]
ob.pose.bones['upperarm_r'].rotation_quaternion = [0.865,0.0,-0.5,0]
ob.pose.bones['lowerarm_l'].rotation_quaternion = [0.953,0.014,-0.010,0.302]
ob.pose.bones['lowerarm_r'].rotation_quaternion = [0.953,0.014,-0.010,0.302]
ob.pose.bones['thigh_r'].rotation_quaternion = [0.998,-0.065,0.023,0]
ob.pose.bones['thigh_l'].rotation_quaternion = [0.998,-0.065,0.023,0]
ob.pose.bones['foot_r'].rotation_quaternion = [1,0,-0.017,0]
ob.pose.bones['foot_l'].rotation_quaternion = [1,0,-0.017,0]
ob.pose.bones['calf_l'].rotation_quaternion = [1,-0.048,-0.0,-0.037]
ob.pose.bones['calf_r'].rotation_quaternion = [1,-0.048,-0.0,-0.037]


bpy.ops.object.mode_set(mode='OBJECT')
ob = bpy.data.objects['root']
bpy.context.view_layer.objects.active = ob
bpy.ops.object.mode_set(mode='POSE')

ob.pose.bones['pelvis'].rotation_quaternion = [0.656,-0.755,-0.027,0]
ob.pose.bones['upperarm_l'].rotation_quaternion = [0.865,0.0,-0.5,0]
ob.pose.bones['upperarm_r'].rotation_quaternion = [0.865,0.0,-0.5,0]
