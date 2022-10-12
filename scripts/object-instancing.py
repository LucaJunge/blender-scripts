import bpy
from bpy import context

# Get the current scene
scene = context.scene

# Get the 3D cursor location
cursor = scene.cursor.location

# Get the active Object
obj = context.active_object

# Nor make a copy of the object
obj_new = obj.copy()

# Add the new object to the collection
scene.collection.objects.link(obj_new)

# Place the object at the cursors location
obj_new.location = cursor
