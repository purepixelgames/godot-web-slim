# Slim Godot web export template (2D only) for Orbital Tapper.
# Passed to SCons with profile=custom.py. Every option below exists in
# godotengine/godot SConstruct at tag 4.6-stable; nothing in the engine is edited.

target = "template_release"
production = "yes"
debug_symbols = "no"
optimize = "size_extra"  # 4.5+: smallest code
lto = "thin"             # same as the official 4.6 web builds (production => thin)
threads = "no"           # project preset: variant/thread_support=false
deprecated = "no"

# Engine parts the game never uses.
disable_3d = "yes"            # also turns off 3D physics, 3D navigation and XR
disable_physics_3d = "yes"
disable_navigation_3d = "yes"
disable_xr = "yes"
disable_physics_2d = "yes"    # no Area2D / bodies / shapes in the game
disable_navigation_2d = "yes"
# disable_advanced_gui stays OFF: the MENU language picker is an OptionButton.

# Modules: everything off except what the game needs.
modules_enabled_by_default = "no"
module_gdscript_enabled = "yes"        # all game code
module_freetype_enabled = "yes"        # font rendering (default font)
module_text_server_fb_enabled = "yes"  # simple text server: Latin + Cyrillic, no RTL
module_svg_enabled = "yes"             # editor-imported SVG icons
module_webp_enabled = "yes"            # lossless imported textures are stored as WebP
module_ogg_enabled = "yes"             # music/solar_loop_music.ogg
module_vorbis_enabled = "yes"
