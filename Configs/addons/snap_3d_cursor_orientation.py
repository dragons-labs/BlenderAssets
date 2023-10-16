# Copyright (c) 2023 Robert Ryszard Paciorek <rrp@opcode.eu.org>
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
    "name": "Snap 3D Cursor Orientation",
    "blender": (2, 80, 0),
    "category": "View",
}

import bpy

class Snap3DCursorOrientation(bpy.types.Operator):
    bl_idname = "cursor.snap_orientation"
    bl_label = "Snap 3D Cursor Orientation"

    def execute(self, context):
        # create custom transform orientation
        bpy.ops.transform.create_orientation(name='tmp_RRP_tmp', use_view=False, overwrite=True)
        bpy.context.scene.transform_orientation_slots[0].type = 'tmp_RRP_tmp'

        # copy rotation from custom transform orientation to cursor 3d
        bpy.context.scene.cursor.rotation_mode = 'QUATERNION'
        bpy.context.scene.cursor.rotation_quaternion = bpy.context.scene.transform_orientation_slots[0].custom_orientation.matrix.to_quaternion()

        # remove custom transform orientation
        bpy.ops.transform.delete_orientation()
        
        return {'FINISHED'}

def menu_func_draw(self, context):
    self.layout.menu_pie().operator('view3d.snap_cursor_to_active', icon = 'CURSOR')  # view3d.snap_cursor_to_grid
    self.layout.menu_pie().operator('view3d.snap_selected_to_grid', icon = 'RESTRICT_SELECT_OFF')
    self.layout.menu_pie().operator('view3d.snap_cursor_to_selected', icon = 'CURSOR')
    a = self.layout.menu_pie().operator('view3d.snap_selected_to_cursor', icon = 'RESTRICT_SELECT_OFF')
    a.use_offset=False
    a = self.layout.menu_pie().operator('view3d.snap_selected_to_cursor', text='Selection to Cursor (Keep Offset)', icon = 'RESTRICT_SELECT_OFF')
    a.use_offset=True
    self.layout.menu_pie().operator('view3d.snap_selected_to_active', icon = 'RESTRICT_SELECT_OFF')
    self.layout.menu_pie().operator('view3d.snap_cursor_to_center', icon = 'CURSOR')
    self.layout.menu_pie().operator(Snap3DCursorOrientation.bl_idname, icon = 'CURSOR') # view3d.snap_cursor_to_active

def menu_func(self, context):
    self.layout.menu_pie().operator(Snap3DCursorOrientation.bl_idname, icon = 'CURSOR')

def register():
    bpy.utils.register_class(Snap3DCursorOrientation)
    #bpy.types.VIEW3D_MT_snap_pie.append(menu_func)
    bpy.types.VIEW3D_MT_snap_pie.draw = menu_func_draw

def unregister():
    bpy.utils.unregister_class(Snap3DCursorOrientation)
