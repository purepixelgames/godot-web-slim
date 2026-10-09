# template_standard_2d - the SAFE general 2D web template (any 2D game).
# = the stock "scons platform=web target=template_release", minus everything 3D,
# plus the size options the docs list. Every 2D feature and every non-3D module
# stays IN (physics 2D, navigation 2D, advanced GUI, full text server for
# CJK/Arabic, regex, noise, mp3, jpg, websocket, ...).
# Run with options_file = profiles/template_standard_2d.py.
# Every option exists in godotengine/godot SConstruct at tag 4.6-stable.

target = "template_release"
production = "yes"
debug_symbols = "no"
optimize = "size_extra"  # 4.5+: smallest code
lto = "thin"             # same as the official web builds; "full" needs 12-16 GB RAM
threads = "no"           # export preset: variant/thread_support=false
javascript_eval = "yes"  # JavaScriptBridge (platform SDKs like Playgama need it)
# deprecated stays default ("yes"): old API names still work, nothing can break.

# Everything 3D off.
disable_3d = "yes"            # also turns off 3D physics, 3D navigation and XR
disable_physics_3d = "yes"
disable_navigation_3d = "yes"
disable_xr = "yes"

# 2D stays complete.
disable_physics_2d = "no"
disable_navigation_2d = "no"
disable_advanced_gui = "no"

# Modules: stock set (modules_enabled_by_default stays "yes"), minus the ones
# that only serve 3D / XR / 3D import. Switched off explicitly so the build does
# not depend on each module noticing disable_3d by itself.
module_csg_enabled = "no"
module_gridmap_enabled = "no"
module_godot_physics_3d_enabled = "no"
module_jolt_physics_enabled = "no"
module_navigation_3d_enabled = "no"
module_openxr_enabled = "no"
module_mobile_vr_enabled = "no"
module_webxr_enabled = "no"
module_lightmapper_rd_enabled = "no"
module_raycast_enabled = "no"        # 3D occlusion culling
module_vhacd_enabled = "no"          # 3D convex decomposition
module_xatlas_unwrap_enabled = "no"  # 3D lightmap UV unwrap
module_meshoptimizer_enabled = "no"  # 3D mesh LOD
module_gltf_enabled = "no"           # 3D scene import (glTF)
module_fbx_enabled = "no"            # 3D scene import (FBX)
