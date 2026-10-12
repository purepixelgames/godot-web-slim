# ArrowShift:Classic - build 1 FAILED on web (deprecated=no removed an API the game uses); build 2 keeps deprecated APIs. 3D GAME: 3D rendering stays ON.
# Run with options_file = profiles/arrowshift_slim.py. Every option exists in
# godotengine/godot SConstruct at tag 4.6-stable; nothing in the engine is edited.
# Built from a scan of the game's .gd/.tscn/.tres/.import files, project.godot and
# export_presets.cfg (tests/ and tools/ are excluded from the export, so not scanned).
# Renderer: Compatibility (WebGL 2). Export preset: Thread Support off.

target = "template_release"
production = "yes"
debug_symbols = "no"
optimize = "size_extra"  # 4.5+: smallest code
lto = "thin"             # same as the official 4.6 web builds (production => thin)
threads = "no"           # preset: variant/thread_support=false
javascript_eval = "yes"  # Playgama bridge uses JavaScriptBridge (all modules)
deprecated = "yes"      # KEEP: localization_manager.gd uses TranslationServer.get_translation_object() (deprecated in 4.6); "no" broke all text on web (2026-10-12)

# KEEP 3D: the cube, camera, ArrayMesh arrows and shaders are all 3D.
disable_3d = "no"
# No physics anywhere: picking and collision are integer math (no Area3D / bodies /
# shapes / raycasts / direct_space_state in any game file).
disable_physics_3d = "yes"
disable_physics_2d = "yes"
disable_navigation_3d = "yes"  # no Navigation* nodes or servers
disable_navigation_2d = "yes"
disable_xr = "yes"
# KEEP advanced GUI: the settings language picker is an OptionButton (uses PopupMenu).
disable_advanced_gui = "no"

# Modules: everything off except what the game needs.
modules_enabled_by_default = "no"
module_gdscript_enabled = "yes"        # all game code
module_freetype_enabled = "yes"        # .ttf fonts (Nunito, Fredoka, Orbitron)
module_text_server_adv_enabled = "no"  # docs: always pair adv=no with fb=yes
module_text_server_fb_enabled = "yes"  # languages: en ru es pt_BR de fr it tr pl (Latin + Cyrillic)
module_svg_enabled = "yes"             # SVG icons (safe default, small)
module_webp_enabled = "yes"            # all 26 textures are lossless (compress/mode=0)

# Left OFF on purpose (nothing in the game uses them):
#   ogg, vorbis, mp3 - no audio files; sounds are AudioStreamWAV made in code (core)
#   jpg              - no .jpg files (.png is core)
#   msdfgen          - no font imported as MSDF
#   regex, noise     - not used in game code
#   mbedtls, websocket, webrtc - no HTTPRequest / sockets / Crypto; Playgama talks through JS
#   godot_physics_2d/3d, jolt_physics, navigation_2d/3d - no physics or navigation
#   csg, gridmap, gltf, basis_universal, bcdec, ktx - none used at runtime
# TEST AFTER EXPORT: FontVariation uses variation_opentype (variable font weights) on
#   the fallback text server; check every theme and language renders the right weight.
