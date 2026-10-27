# ArrowShift:Classic - build 5 (2026-10-27): the official Godot 4.6 web release build with every engine feature
# the game does NOT use taken out, and every feature it DOES use left exactly as the official template has it.
# Classes: profiles/arrowshift_slim_v5.gdbuild (passed as build_profile by the workflow).
# Build 4 (profiles/arrowshift_slim.py) stays as the fallback.
#
# Speed rule (builds 1-3 loaded slower): the official speed settings are NOT touched. optimize stays "size"
# (platform/web/detect.py: -Oz saves ~100 KiB but hurts run time), lto stays "thin" (production default),
# wasm_simd stays on, deprecated APIs stay on (localization_manager.gd needs them). Taking out code the game
# never runs does not make the code it does run slower.
#
# Audit 2026-10-27 (Godot 4.6-stable source + --dump-extension-api of the owner's editor): every exported file
# (scripts, scenes, resources, imports, shaders, project.godot, addons/playgama_bridge; tests/ tools/ excluded)
# was searched for every engine class. Used: 3D (Camera3D, MeshInstance3D, ArrayMesh, Plane/QuadMesh,
# ShaderMaterial), Control GUI incl. OptionButton / PopupMenu (advanced GUI), Tweens, Timers, AudioStreamWAV
# made in code + AudioBusLayout, CompressedTexture2D (lossless WebP), FontFile (.ttf), compressed CSV
# translations (OptimizedTranslation), a .gdshaderinc (ShaderInclude), JavaScriptBridge (+ eval), JSON.

target = "template_release"
production = "yes"       # same as the official build (lto=thin, no debug symbols)
threads = "no"           # preset: variant/thread_support=false (the workflow passes it too)

# Whole engine systems the game never uses (same as build 4).
disable_physics_3d = "yes"
disable_physics_2d = "yes"
disable_navigation_3d = "yes"
disable_navigation_2d = "yes"
disable_xr = "yes"
# KEEP: disable_3d (the cube is 3D), disable_advanced_gui (OptionButton / PopupMenu live behind it).

# Modules: only the ones the game uses are built.
modules_enabled_by_default = "no"
module_gdscript_enabled = "yes"          # all game code
module_text_server_adv_enabled = "yes"   # the official text server (same shaping and line breaking as build 4)
module_freetype_enabled = "yes"          # the 3 .ttf fonts (Nunito, Fredoka, Orbitron)
module_svg_enabled = "yes"               # default theme icons are SVG drawn at run time (slider grabbers,
                                         #   popup radio marks); also OT-SVG glyph support for the text server
module_webp_enabled = "yes"              # all 26 imported textures are lossless (compress/mode=0) = WebP in the pck
graphite = "no"                          # SIL Graphite smart fonts: none of the 3 fonts is a Graphite font
brotli = "no"                            # only for WOFF2 fonts and Brotli decompress: fonts are .ttf, no decompress
minizip = "no"                           # ZIP packs / ZIPReader: the web export loads a .pck

# Left OFF (nothing in the game or the Playgama addon uses them):
#   text_server_fb (fallback text server, only used if adv is missing)
#   ogg, vorbis, mp3 (no audio files: every sound is an AudioStreamWAV built in code), theora (no video)
#   jpg, bmp, tga, dds, hdr, ktx, tinyexr (no such images), basis_universal, bcdec (no VRAM-compressed textures)
#   msdfgen (no MSDF fonts, no Label3D), gltf, fbx, csg, gridmap, noise, regex, mbedtls (no Crypto / TLS / HTTP),
#   websocket, webrtc, enet, multiplayer, jsonrpc, upnp, zip, interactive_music, camera, mobile_vr,
#   godot_physics_2d / 3d, jolt_physics, navigation_2d / 3d, webxr, openxr
#   (editor-only modules are never in a template anyway)
