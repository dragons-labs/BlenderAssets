About this repo
===============

This repository is asset library (both models and some simple materials) for [Blender](https://www.blender.org/).
Additionally contains a [modified startup file](Configs/UI_default.blend) and several plugins and tools:

* [Sync 3D view](Configs/addons/configure_and_sync_preview.py) → add hot key (numpad asterisk) to sync first 3D view to current (useful for "UV Editing" workspace in my startup file)
* [Load startup settings into current scene](Configs/addons/load_startup_into_current.py) → allow load default file settings (workspaces and scene stuff – units, tools settings) into current file via option in "File ▸ Defaults"
* [Snap 3D Cursor Orientation](Configs/addons/snap_3d_cursor_orientation.py) → add "Snap 3D Cursor Orientation" option in snap pie menu (instead of "snap to grid"), allowing copy orientation of current selected object or mesg element to 3D cursor
* [Blender-open-gltf.py](Configs/blender-open-gltf.py) → simple script to open gltf files with Blender, can be used to opening gltf files in Blender directly from file manager


Assets
------

All files and assets in this repository (except auxiliary "Materials/TestChart.svg", which is a modification of [clipart](https://openclipart.org/detail/98815/tv-testscreen-by-firstl4rs) distributed as public domain) are made by me (Robert Paciorek) and are not derivative works (from other 3D models nor materials/textures).

### More assets

Collection of Blender assets based on CC-0 and CC-BY licensed models (created by other authors; modified and converted into Blender assets by me) are available as Google Drive: https://drive.google.com/drive/folders/1gnf0jt7Gj9Y0EsQqufOCmMPfvUXJHJo5


Licence
-------

* Primary licence for all files in this repo is [MIT/X11](LICENSE). 
* An alternative license for all resources (including all Blender files and separated asset) from this repository is [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/) for better compatibility with "art resources".
* You can choose the license (MIT or CC-BY) that suits you best.


How to use
==========

Add and use assets library to Blender
-------------------------------------
1. go to "Edit ▸ Preferences ▸ File Paths"
2. add new entry (`+` icon) in "Assets Libraries" section and select path to main dir of this repo
3. use "Asset Browser" typ window to browse assets
	1. select library in left panel
	2. select adding mode on top
	3. drag and drop asset to scene


Move and Rotate linked object
-----------------------------

1. add (linked) asset from browser to scene
2. select object in scene and use "Object ▸ Library Override ▸ Make"


Change pose for linked object
-----------------------------

1. add (linked) asset from browser to scene
2. select object in scene and use "Object ▸ Library Override ▸ Make"
3. select object armature in scene and (again) use "Object ▸ Library Override ▸ Make"
4. switch to "Pose Mode"


Use pose from asset library
---------------------------

1. switch to "Pose Mode" on destination object armature
2. select pose in asset browser
3. click Apply under "Pose Library" in left panel of asset browser


Place on surface
----------------

(after enable move and rotate - see above)

1. select "snap to face projection" and check "align rotation to target" in snap menu
2. move object to surface (wall,ceiling, etc) with [g]
3. adjust orthogonal to surface rotation of object by rotate along the local Z axis ([r] → [z] → [z])


Use linked "generators" from asset library
------------------------------------------

1. add (linked) asset from browser to scene
2. select object in scene and use "Object ▸ Library Override ▸ Make"
	* objects from collection will be unpacked as linked object with active "Library Override"
3. configure "Array" modifier and/or adjust scale of object

**Note**:
	For not linked collections in step 2 use "Object ▸ Apply (Ctrl A) ▸ Make Instances Real" to unpack objects from collection and remember to select "Parent" and "Keep Hierarchy" option!
	This can be also used for linked collections - in this case mesh and materials will be still linked, but objects will be instanced.
