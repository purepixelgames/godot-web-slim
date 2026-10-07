# STARTER options for a new 2D web game (no 3D). Copy to profiles/<game>.py,
# then switch parts off/on for that game (see README "Choosing the options").
# Every option exists in godotengine/godot SConstruct at tag 4.6-stable.

target = "template_release"
production = "yes"
debug_symbols = "no"
optimize = "size_extra"  # 4.5+: smallest code
lto = "thin"             # official web builds use thin; "full" only on machines with 16 GB RAM
threads = "no"           # must match the export preset: variant/thread_support=false
deprecated = "no"

# Always off for a 2D game.
disable_3d = "yes"            # also turns off 3D physics, 3D navigation and XR
disable_physics_3d = "yes"
disable_navigation_3d = "yes"
disable_xr = "yes"

# Per game - switch to "yes" only if the game has none of these:
disable_physics_2d = "no"     # Area2D, CharacterBody2D, RigidBody2D, CollisionShape2D, ...
disable_navigation_2d = "no"  # NavigationAgent2D, NavigationRegion2D, AStar is NOT affected
disable_advanced_gui = "no"   # OptionButton, PopupMenu, RichTextLabel, SpinBox, Tree, TextEdit, ...

# Modules: everything off except what is listed.
modules_enabled_by_default = "no"
module_gdscript_enabled = "yes"        # game code
module_freetype_enabled = "yes"        # font rendering
module_text_server_adv_enabled = "no"  # docs: always pair adv=no with fb=yes
module_text_server_fb_enabled = "yes"  # simple text: Latin, Greek, Cyrillic (no Arabic/Hebrew/CJK shaping)
module_svg_enabled = "yes"             # SVG images (icon.svg etc.)
module_webp_enabled = "yes"            # lossless imported textures are stored as WebP
module_ogg_enabled = "yes"             # .ogg audio
module_vorbis_enabled = "yes"
module_godot_physics_2d_enabled = "yes"  # "no" together with disable_physics_2d = "yes"
module_navigation_2d_enabled = "yes"     # "no" together with disable_navigation_2d = "yes"
# Turn on when the game needs them (names from the 4.6-stable modules/ folder):
# module_mp3_enabled = "yes"           # .mp3 audio
# module_jpg_enabled = "yes"           # .jpg images
# module_regex_enabled = "yes"         # RegEx in scripts
# module_noise_enabled = "yes"         # FastNoiseLite / NoiseTexture2D
# module_msdfgen_enabled = "yes"       # fonts imported with "Multichannel Signed Distance Field"
# module_websocket_enabled = "yes"     # WebSocketPeer (online games)
# TileMapLayer / TileSet are part of the engine core in 4.6 - no module needed.
