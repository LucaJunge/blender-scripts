bl_info = {
  "name": "DSM",
  "description": "Add-On collection",
  "author": "Luca Junge",
  "version": (0, 1),
  "blender": (2, 80, 0),
  "category": "Object",
}

import bpy

class ObjectMoveX(bpy.types.Operator):
  """My Object Moving Script"""
  bl_idname = "object.move_x"
  bl_label = "Move X by One"
  bl_options = {"REGISTER", "UNDO"}

  def execute(self, context):

    # The original script
    scene = context.scene
    for obj in scene.objects:
      obj.location.x += 1.0

    return {"FINISHED"}


def menu_func(self, context):
    self.layout.operator(ObjectMoveX.bl_idname)

def register():
    bpy.utils.register_class(ObjectMoveX)
    bpy.types.VIEW3D_MT_object.append(menu_func)
  
def unregister():
    bpy.utils.unregister_class(ObjectMoveX)

if __name__ == "__main__":
  register()
