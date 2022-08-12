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


ob = bpy.data.objects['Reference']
bpy.context.view_layer.objects.active = ob
bpy.ops.object.mode_set(mode='POSE')

ob.pose.bones['clavicle_l'].rotation_quaternion = [0.997,0,0,0.074]
ob.pose.bones['clavicle_r'].rotation_quaternion = [0.997,0,0,0.074]
ob.pose.bones['upperarm_l'].rotation_quaternion = [0.930,0,0,0.369]
ob.pose.bones['upperarm_r'].rotation_quaternion = [0.930,0,0,0.369]
ob.pose.bones['lowerarm_l'].rotation_quaternion = [0.944,-0.330,0,0]
ob.pose.bones['lowerarm_r'].rotation_quaternion = [0.847,0.330,0,0]
ob.pose.bones['thigh_l'].rotation_quaternion = [1,0,-0.030,-0.044]
ob.pose.bones['thigh_r'].rotation_quaternion = [1,0,0.030,0.044]
