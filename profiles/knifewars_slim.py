# Knife Wars 1 - build 1 (2026-11-08): the official Godot 4.6 web release build with every engine feature the game
# does NOT use taken out, and every feature it DOES use left exactly as the official template has it.
# Classes: profiles/knifewars_slim.gdbuild (passed as build_profile by the workflow).
# Workflow: .github/workflows/build_knifewars_slim.yml ("Build knifewars_slim").
#
# Speed rule (learned on ArrowShift): the official speed settings are NOT touched. optimize stays "size",
# lto stays "thin" (production default), wasm_simd stays on, deprecated APIs stay on (localization_manager.gd
# calls TranslationServer.get_translation_object()). Taking out code the game never runs does not slow the rest.
#
# Audit 2026-11-08 (Godot 4.6-stable source + --dump-extension-api of the owner's editor): every exported text
# file (scripts, scenes, resources, imports, shaders, project.godot, addons/playgama_bridge; tests/ tools/
# documents_new/ excluded) was searched for every engine class as a whole word. The game is pure 2D:
# Node2D, Sprite2D, CPUParticles2D, MultiMeshInstance2D + MultiMesh + ArrayMesh (confetti), ShaderMaterial
# (4 .gdshader), Control GUI incl. OptionButton / PopupMenu / HSlider / CheckButton / ScrollContainer, Tweens,
# Timers, AudioStreamPlayer + 14 .ogg (AudioStreamOggVorbis), CompressedTexture2D (127 lossless = WebP),
# AtlasTexture, GradientTexture2D, Curve, 2 .ttf FontFile, CSV translations (en ru es pt_BR de fr it tr pl:
# Latin + Cyrillic), JavaScriptBridge, JSON. NOT used: any 3D node, physics bodies / shapes, navigation,
# TileMap / TileMapLayer / TileSet, AnimationPlayer, GPU particles, RichTextLabel, video, networking, RegEx.

target = "template_release"
production = "yes"       # same as the official build (lto=thin, no debug symbols)
threads = "no"           # preset: variant/thread_support=false (the workflow passes it too)

# Whole engine systems the game never uses.
disable_3d = "yes"              # no 3D node or resource anywhere (MultiMesh / ArrayMesh / Mesh stay: 2D code)
disable_physics_3d = "yes"
disable_physics_2d = "yes"      # hits are angle math only; no Area2D / bodies / shapes / raycasts
disable_navigation_3d = "yes"
disable_navigation_2d = "yes"
disable_xr = "yes"
# KEEP: disable_advanced_gui (OptionButton / PopupMenu in the settings menu live behind it).

# Modules: only the ones the game uses are built.
modules_enabled_by_default = "no"
module_gdscript_enabled = "yes"          # all game code
module_text_server_adv_enabled = "yes"   # the official text server (same shaping and line breaking as stock)
module_freetype_enabled = "yes"          # the 2 .ttf fonts (Nunito, Orbitron)
module_svg_enabled = "yes"               # default theme icons are SVG drawn at run time (slider grabbers,
										#   popup radio marks); also OT-SVG glyph support for the text server
module_webp_enabled = "yes"              # all 127 imported textures are lossless (compress/mode=0) = WebP in the pck
module_ogg_enabled = "yes"               # 14 .ogg music / sound files
module_vorbis_enabled = "yes"            #   (AudioStreamOggVorbis needs ogg + vorbis)
graphite = "no"                          # SIL Graphite smart fonts: neither font is a Graphite font
brotli = "no"                            # only for WOFF2 fonts and Brotli decompress: fonts are .ttf
minizip = "no"                           # ZIP packs / ZIPReader: the web export loads a .pck

# Left OFF (nothing in the game or the Playgama addon uses them):
#   text_server_fb (fallback text server, only used if adv is missing)
#   mp3 (no .mp3), theora (no video), jpg, bmp, tga, dds, hdr, ktx, tinyexr (no such images),
#   basis_universal, bcdec, etcpak, astcenc (no VRAM-compressed textures), msdfgen (no MSDF fonts),
#   gltf, fbx, csg, gridmap, noise, regex, mbedtls (no Crypto / TLS / HTTP), websocket, webrtc, enet,
#   multiplayer, jsonrpc, upnp, zip, interactive_music, camera, mobile_vr, godot_physics_2d / 3d,
#   jolt_physics, navigation_2d / 3d, webxr, openxr (editor-only modules are never in a template anyway)
