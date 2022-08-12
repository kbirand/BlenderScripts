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

ob.pose.bones['clavicle_l'].rotation_quaternion = [0.996,-0.088,0,0]
ob.pose.bones['upperarm_l'].rotation_quaternion = [0.932,-0.362,0,0]
ob.pose.bones['lowerarm_l'].rotation_quaternion = [0.943,-0.009,-0.025,-0.331]

ob.pose.bones['hand_l'].rotation_quaternion = [0.997,0,0.081,0]

ob.pose.bones['thumb_01_l'].rotation_quaternion = [0.965,-0.169,0.034,-0.196]
ob.pose.bones['thumb_02_l'].rotation_quaternion = [0.868,-0.078,0.488,0.044]
ob.pose.bones['thumb_03_l_l'].rotation_quaternion = [0.981,-0.196,0,0]

ob.pose.bones['index_01_l'].rotation_quaternion = [0.986,-0.104,0.130,-0.015]
ob.pose.bones['index_02_l'].rotation_quaternion = [0.990,-0.143,0,0]
ob.pose.bones['index_03_l'].rotation_quaternion = [0.997,-0.071,0,0]

ob.pose.bones['middle_01_l'].rotation_quaternion = [0.995,-0.068,0.063,0.023]
ob.pose.bones['middle_02_l'].rotation_quaternion = [0.989,-0.147,0,0]
ob.pose.bones['middle_03_l'].rotation_quaternion = [0.991,-0.134,0,0]

ob.pose.bones['ring_01_l'].rotation_quaternion = [0.992,-0.084,0.067,0.067]
ob.pose.bones['ring_02_l'].rotation_quaternion = [0.994,-0.104,0,0]
ob.pose.bones['ring_03_l'].rotation_quaternion = [0.995,-0.095,0,0]

ob.pose.bones['pinky_01_l'].rotation_quaternion = [0.979,-0.086,-0.047,0.178]
ob.pose.bones['pinky_02_l'].rotation_quaternion = [0.999,-0.050,0,0]
ob.pose.bones['pinky_03_l'].rotation_quaternion = [0.995,-0.100,0,0]


ob.pose.bones['thigh_l'].rotation_quaternion = [1,0,0.030,0.044]
