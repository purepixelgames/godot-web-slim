# template_bound_v2 - Bound to Defend only. UNTESTED (2026-10-09).
# Built from a scan of the game's .gd/.tscn/.tres/.import files and project.godot.
# Run with options_file = profiles/template_bound_v2.py.
# Every option exists in godotengine/godot SConstruct at tag 4.6-stable.

target = "template_release"
production = "yes"
debug_symbols = "no"
optimize = "size_extra"  # 4.5+: smallest code
lto = "thin"             # same as the official web builds
threads = "no"           # both Web presets: variant/thread_support=false
javascript_eval = "yes"  # Playgama bridge + GlobalSignals use JavaScriptBridge
deprecated = "no"        # removes old API names - test SilentWolf + Playgama after export

# Engine parts the game never uses.
disable_3d = "yes"            # also turns off 3D physics, 3D navigation and XR
disable_physics_3d = "yes"
disable_navigation_3d = "yes"
disable_xr = "yes"
disable_navigation_2d = "yes" # no NavigationAgent2D / Region2D / Server2D, no nav layers in tilesets
# KEEP physics 2D: Area2D (32 files), CollisionShape2D, CharacterBody2D, StaticBody2D,
#   RayCast2D, PhysicsServer2D + intersect_* queries.
disable_physics_2d = "no"
# KEEP advanced GUI: OptionButton (15 files), PopupMenu, MenuButton, RichTextLabel.
disable_advanced_gui = "no"

# Modules: everything off except what the game needs.
modules_enabled_by_default = "no"
module_gdscript_enabled = "yes"          # all game code
module_freetype_enabled = "yes"          # .ttf fonts (Noto SC/JP, Oswald, SquadaOne, Comfortaa)
module_text_server_adv_enabled = "yes"   # KEEP: zh_CN + ja translations need CJK line breaking,
module_text_server_fb_enabled = "no"     #   and the fonts are variable (wght) fonts
graphite = "no"                          # SIL Graphite smart fonts (text_server_adv extra) - none used
module_godot_physics_2d_enabled = "yes"  # the 2D physics engine
module_svg_enabled = "yes"               # icon.svg
module_webp_enabled = "yes"              # lossless imported textures (compress/mode=0)
module_basis_universal_enabled = "yes"   # 87 textures imported as Basis Universal (compress/mode=4)
module_bcdec_enabled = "yes"             # tiny; decompresses BC textures if a GPU lacks them
module_ogg_enabled = "yes"               # all 27 audio files are .ogg
module_vorbis_enabled = "yes"
module_mbedtls_enabled = "yes"           # Crypto.hmac_digest signs save.sav (save integrity)
module_noise_enabled = "yes"             # FastNoiseLite / NoiseTexture2D in shaders/vfx/*_noise.tres

# Left OFF on purpose (nothing in the game uses them):
#   regex       - only tools/validation/tests (dev-only, never loaded in a run)
#   websocket   - SilentWolf WSClient has its WebSocket code commented out
#   mp3, jpg, tga, bmp, dds, hdr, ktx, tinyexr - no such files
#   msdfgen     - no font is imported as MSDF
#   multiplayer, enet, webrtc, jsonrpc, upnp, zip, interactive_music, camera, theora
