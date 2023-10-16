# Copyright (c) 2021-2023 Robert Ryszard Paciorek <rrp@opcode.eu.org>
# 
# MIT License
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

bl_info = {
    "name": "Sync 3D view",
    "blender": (2, 80, 0),
    "category": "View",
}

import bpy

class Sync3DView(bpy.types.Operator):
    bl_idname = "view.sync"
    bl_label = "Sync 3D view"

    def execute(self, context):
        for a in bpy.context.screen.areas:
            if a.type == 'VIEW_3D':
                if a.x == 0:
                    dst = a
                else:
                    src = a

        dst.spaces.active.show_region_toolbar = False
        dst.spaces.active.show_region_ui = False
        dst.spaces.active.show_gizmo = False
        dst.spaces.active.overlay.show_overlays = False
        dst.spaces.active.shading.type = 'MATERIAL'

        dst.spaces.active.region_3d.view_matrix = src.spaces.active.region_3d.view_matrix
        dst.spaces.active.region_3d.view_distance = src.spaces.active.region_3d.view_distance
        dst.spaces.active.region_3d.view_location = src.spaces.active.region_3d.view_location
        dst.spaces.active.region_3d.view_perspective = src.spaces.active.region_3d.view_perspective
        
        return {'FINISHED'}

addon_keymaps = []

def menu_func(self, context):
    self.layout.operator(Sync3DView.bl_idname)

def register():
    bpy.utils.register_class(Sync3DView)
    bpy.types.VIEW3D_MT_object.append(menu_func)
    
    try:
        km = bpy.context.window_manager.keyconfigs.addon.keymaps.new(name='Window', space_type='EMPTY')
        kmi = km.keymap_items.new(Sync3DView.bl_idname, 'NUMPAD_ASTERIX', 'PRESS', ctrl=False, shift=False)
        addon_keymaps.append((km, kmi))
    except:
        pass

def unregister():
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()
    
    bpy.utils.unregister_class(Sync3DView)
