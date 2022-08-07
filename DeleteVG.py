import bpy
context = bpy.context

ob = context.object
vgs = [vg for vg in ob.vertex_groups
       if vg.name.find("FACIAL") != -1]

while(vgs):
    ob.vertex_groups.remove(vgs.pop())
