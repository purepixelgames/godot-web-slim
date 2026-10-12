# ArrowShift:Classic - AUDITED 2026-10-12 (build 3). 3D GAME: 3D rendering stays ON.
# Run with options_file = profiles/arrowshift_slim.py (workflow "Build arrowshift_slim" runs on push).
# Every option exists in godotengine/godot SConstruct at tag 4.6-stable; nothing in the engine is edited.
#
# History: build 1 used deprecated="no" and broke the web build (LocalizationManager calls
# TranslationServer.get_translation_object(), deprecated in 4.6 -> script failed to load -> no translations,
# no save, Next stage broken). Build 2 kept deprecated APIs. Build 3 = build 2 after a full audit:
#
# How the audit was done (against Godot 4.6-stable source, not from memory):
#  1. All 1023 engine classes (godot --dump-extension-api) searched in every exported file of the game
#     (.gd .tscn .tres .import .cfg .godot .gdshader .json, addons/playgama_bridge included; tests/ and tools/
#     are excluded from the export) -> 89 classes referenced.
#  2. scene/register_scene_types.cpp, servers/register_server_types.cpp, core/register_core_types.cpp parsed for
#     the #ifndef guard of every class: the 5 flags turned off below remove 129 classes (physics bodies/shapes/
#     joints/queries, navigation, XR, TouchScreenButton, PolygonPathFinder). None of the 89 is among them.
#  3. Implicit classes behind used features checked too: Translation, OptimizedTranslation, TranslationDomain
#     (CSV translations), Time, Timer, SceneTreeTimer, Tween*, AudioStream*/AudioSample (web audio),
#     World3D/Environment, ResourceLoader, Theme/ThemeDB, FontVariation: all unguarded or behind 3D (kept).
#  4. modules/*/register_types.cpp of every module: no module turned off registers a class the game uses.
#  5. Text server: fb supports variable fonts (FT_Get_MM_Var in text_server_fb.cpp), the game uppercases only
#     ASCII keys (fb casing is not locale aware: Turkish i would differ), all 9 languages are Latin/Cyrillic.
#     Fonts: Nunito covers all 9 languages; Fredoka/Orbitron lack Cyrillic, Turkish and Polish letters but every
#     theme 2/3 FontVariation has Nunito as fallback (works on both text servers).
#  6. Imports: only csv_translation, font_data_dynamic and texture (all 26 lossless = WebP); no text driver,
#     occlusion culling or VRAM / Basis textures in project.godot or *.import.

target = "template_release"
production = "yes"
debug_symbols = "no"
optimize = "size_extra"  # 4.5+: smallest code (no behaviour change)
lto = "thin"             # same as the official 4.6 web builds (production => thin)
threads = "no"           # preset: variant/thread_support=false
javascript_eval = "yes"  # Playgama bridge uses JavaScriptBridge (all modules)
deprecated = "yes"       # KEEP: the game calls deprecated 4.6 APIs (see history above)

# KEEP 3D: Camera3D, MeshInstance3D, Node3D, ArrayMesh, QuadMesh, PlaneMesh, ShaderMaterial (the cube).
disable_3d = "no"
# Off: none of the 129 classes these remove is used (audit step 2). Picking and collision are integer math.
disable_physics_3d = "yes"
disable_physics_2d = "yes"
disable_navigation_3d = "yes"
disable_navigation_2d = "yes"
disable_xr = "yes"
# KEEP advanced GUI: OptionButton (settings language picker) and its PopupMenu.
disable_advanced_gui = "no"

# Modules: everything off except what the game needs (audit step 4).
modules_enabled_by_default = "no"
module_gdscript_enabled = "yes"        # all game code
module_freetype_enabled = "yes"        # .ttf fonts (Nunito, Fredoka, Orbitron)
module_text_server_adv_enabled = "no"  # docs: always pair adv=no with fb=yes (audit step 5)
module_text_server_fb_enabled = "yes"  # languages: en ru es pt_BR de fr it tr pl (Latin + Cyrillic)
module_svg_enabled = "yes"             # SVG support (small, safe)
module_webp_enabled = "yes"            # all 26 imported textures are lossless WebP (compress/mode=0)

# Left OFF on purpose (no class or file of the game needs them, audit steps 4 and 6):
#   ogg, vorbis, mp3      - no audio files; sounds are AudioStreamWAV made in code (core)
#   jpg, bmp, tga, hdr, dds, ktx, tinyexr - no such files, nothing loads images at runtime
#   basis_universal, bcdec, etcpak, cvtt, astcenc, betsy - no VRAM / Basis compressed textures
#   msdfgen               - no font imported as MSDF
#   regex, noise, zip, jsonrpc - not used
#   mbedtls               - no Crypto / TLS / HTTPRequest; core hashing builds its own light mbedtls
#   websocket, webrtc, enet, upnp, multiplayer - no networking; Playgama talks through JavaScriptBridge
#   godot_physics_2d/3d, jolt_physics, navigation_2d/3d - physics / navigation are off
#   csg, gridmap, gltf, fbx, interactive_music, theora, camera, openxr, mobile_vr, webxr - not used
#   meshoptimizer, raycast, lightmapper_rd, xatlas_unwrap, vhacd, glslang, objectdb_profiler, mono - editor / not used
