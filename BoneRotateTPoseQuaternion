import math
import bpy
import numpy as np # Scientific computing library for Python


def print(data):
    for window in bpy.context.window_manager.windows:
        screen = window.screen
        for area in screen.areas:
            if area.type == 'CONSOLE':
                override = {'window': window, 'screen': screen, 'area': area}
                bpy.ops.console.scrollback_append(override, text=str(data), type="OUTPUT")   


ob = bpy.data.objects['root']
bpy.context.view_layer.objects.active = ob
bpy.ops.object.mode_set(mode='POSE')

ob.pose.bones['upperarm_l'].rotation_quaternion = [0.892,0.0,-0.452,0]
ob.pose.bones['upperarm_r'].rotation_quaternion = [0.892,0.0,-0.452,0]
ob.pose.bones['lowerarm_l'].rotation_quaternion = [0.953,0.014,-0.010,0.302]
ob.pose.bones['lowerarm_r'].rotation_quaternion = [0.953,0.014,-0.010,0.302]
