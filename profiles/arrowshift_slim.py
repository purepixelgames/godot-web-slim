# ArrowShift:Classic - build 4 (2026-10-12): the OFFICIAL Godot 4.6 web release build, minus only the big
# engine systems the game does not use. Nothing else changed: same optimisation, same LTO, same text server,
# same modules as the template Godot ships. 3D GAME: 3D stays ON.
# Run with options_file = profiles/arrowshift_slim.py (workflow "Build arrowshift_slim" runs on push).
#
# Why build 4: builds 1-3 used optimize="size_extra" (Godot 4.5+, smallest code) instead of the official web
# default "size", plus the simple text server and almost no modules. The owner measured the game loading SLOWER
# than with the stock template. The game does CPU work while loading (stage puzzle build, sound synthesis in
# GDScript), so smaller-but-slower engine code costs more than the smaller download saves.
# Official web settings (godotengine/godot-build-scripts build-web: OPTIONS="production=yes";
# platform/web/detect.py: optimize defaults to "size", production => lto "thin"): kept by NOT overriding them.

target = "template_release"
production = "yes"       # same as the official build (also gives lto=thin on web)
threads = "no"           # preset: variant/thread_support=false (the workflow passes it too)

# Removed: whole engine systems ArrowShift never uses (audit 2026-10-12: none of their classes is referenced
# anywhere in the exported game or addons/playgama_bridge; picking and collision are integer math).
disable_physics_3d = "yes"
disable_physics_2d = "yes"
disable_navigation_3d = "yes"
disable_navigation_2d = "yes"
disable_xr = "yes"
module_godot_physics_2d_enabled = "no"
module_godot_physics_3d_enabled = "no"
module_jolt_physics_enabled = "no"
module_navigation_2d_enabled = "no"
module_navigation_3d_enabled = "no"
module_webxr_enabled = "no"

# Everything else stays exactly as in the official template: 3D, advanced GUI, deprecated APIs, the advanced
# text server, all other modules, optimize="size", lto="thin".
