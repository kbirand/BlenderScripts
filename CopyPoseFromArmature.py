import bpy

def print(data):
    for window in bpy.context.window_manager.windows:
        screen = window.screen
        for area in screen.areas:
            if area.type == 'CONSOLE':
                override = {'window': window, 'screen': screen, 'area': area}
                bpy.ops.console.scrollback_append(override, text=str(data), type="OUTPUT")   


originalArmature = bpy.data.objects['originalArmature']
selectedObj = bpy.context.selected_objects
print(selectedObj)



#Set Owner Rig
ownerBoneList = selectedObj[0].pose.bones
#Set Target Rig
targetBoneList = originalArmature.pose.bones

for i in range(len(ownerBoneList)):
    ownerBone = ownerBoneList[i]
    targetBone = targetBoneList.get(ownerBone.name)
    if targetBone == None:
      continue
    cons = ownerBone.constraints.new('COPY_TRANSFORMS')
    cons.target = originalArmature
    cons.subtarget = targetBone.name
    cons.target_space = 'POSE'
    cons.owner_space = 'POSE'
    
    
##### Delete Constarints

#name = 'Copy Transforms'

#for i in range(len(ownerBoneList)):
#    ownerBone = ownerBoneList[i]

#    for c in ownerBone.constraints:
#        if 'Copy Transforms' in c.name:
#            ownerBone.constraints.remove(c)  # Remove constraint
