# godot-web-slim

Build a **slim Godot web engine** (2D only, no 3D) for a game, in **GitHub Actions**.
Nothing is compiled on your own PC, and the engine source is never edited: the build
downloads the official `godotengine/godot` source and only switches parts off with
documented build options.

**Why:** a Godot web game downloads the engine (`index.wasm`) before anything shows.
The stock template contains 3D, physics, navigation, XR, a heavy text shaper and many
importers. For a 2D game most of that is dead weight.

**Result for Orbital Tapper (Godot 4.6-stable, 2026-10-07):**

| | stock template | slim | saved |
|---|---|---|---|
| `godot.wasm` raw | 37.7 MB | 23.2 MB | -39 % |
| `godot.wasm` gzipped (≈ download) | 9.5 MB | 5.5 MB | -42 % |

---

## What is in this repo

| file | what it is |
|---|---|
| `.github/workflows/build.yml` | the cloud build (run by hand from the Actions tab) |
| `custom.py` | **starter** options for a new 2D game |
| `profiles/<game>.py` | the options for one game (one file per game) |
| `profiles/orbital_tapper.py` | proven options for Orbital Tapper |
| `profiles/template_standard_2d.py` | **safe general 2D template**: stock engine minus everything 3D (all 2D, GUI, text, modules kept) |
| `profiles/template_bound_v2.py` | Bound to Defend: only the parts that game uses (untested) |

The workflow:
1. downloads the official Godot source at the tag you give (e.g. `4.6-stable`),
2. installs the official Emscripten (web compiler) version you give,
3. builds `template_release` for the web, single-threaded, with your options file,
4. shows the new `.wasm` size (raw and gzip) in the run summary,
5. offers the template as a downloadable artifact.

---

## New game: step by step

### 1. Find your exact Godot version
The template **must** be built from the same version as the editor that exports the game,
or the exported game will not start.
In Godot: *Help > About* (or the window title), e.g. `4.6.stable` -> tag **`4.6-stable`**,
`4.6.2.stable` -> tag **`4.6.2-stable`**.

### 2. Find the matching Emscripten version
Godot's own build machines list it in
`https://github.com/godotengine/build-containers/blob/<branch>/Dockerfile.web`
(branch = `4.6`, `4.7`, ...), line `ENV EMSCRIPTEN_VERSION=...`.
For 4.6 it is **4.0.20**. (Minimum per the docs: 4.0.0. `lto=thin` needs 4.0.9+.)

### 3. Make the game's options file
Copy `custom.py` to `profiles/<game>.py` and go through "Choosing the options" below.
Commit it to this repo (GitHub website: *Add file > Create new file*, or git).

### 4. Run the build
GitHub: **Actions > Build slim web template > Run workflow**, fill in:
- `godot_ref`: the tag from step 1
- `emscripten_version`: from step 2
- `options_file`: `profiles/<game>.py`

It takes about 10 minutes. Green = done. The run summary shows the `.wasm` size.

### 5. Download the template
Open the finished run, scroll to the **bottom**, box **Artifacts**, click
**web-slim-<tag>-<game>**. You get a zip; extract it **once**: inside is
`web_nothreads_release.zip` - that is the template. **Do not extract that inner zip.**
(If you did: zip the 7 files `godot.wasm`, `godot.js`, `godot.html`, `godot.audio.worklet.js`,
`godot.audio.position.worklet.js`, `godot.service.worker.js`, `godot.offline.html`
back together, files at the top level of the zip, no folder.)

Keep it **outside** the Godot install, e.g. next to the game's export folder.

### 6. Use it in the game
Godot: *Project > Export > Web*:
- **Custom Template > Release** = path to `web_nothreads_release.zip`
- **Thread Support** = off (the template is single-threaded; it must match)

(Or in `export_presets.cfg`: `custom_template/release="D:/path/web_nothreads_release.zip"`.)
Close/reopen the project after editing the file by hand, or the open editor may save its
old settings over it.

Export with **"Export With Debug" unchecked** - only the release template is slim;
debug exports still use the stock template.

### 7. Test the exported game - every time
A part that was switched off but is needed breaks **only the exported web build**, never the
editor. Check: all text (every language), music and sounds, scrolling, dropdowns / popups,
buttons, saving, ads / platform SDK, every screen of the game.

Going back is one click: clear **Custom Template > Release**.

---

## Choosing the options

The Godot docs page this follows:
<https://docs.godotengine.org/en/latest/engine_details/development/compiling/optimizing_for_size.html>

**Always safe for a 2D web game** (already in `custom.py`):
`optimize=size_extra`, `lto=thin`, `debug_symbols=no`, `production=yes`, `deprecated=no`,
`disable_3d`, `disable_physics_3d`, `disable_navigation_3d`, `disable_xr`.

**Decide per game** - search the game's `.tscn`, `.tres` and `.gd` files:

| option | set to "yes" (= remove) only if the game has none of |
|---|---|
| `disable_physics_2d` (+ `module_godot_physics_2d_enabled = "no"`) | Area2D, StaticBody2D, CharacterBody2D, RigidBody2D, CollisionShape2D, RayCast2D, physics queries |
| `disable_navigation_2d` (+ `module_navigation_2d_enabled = "no"`) | NavigationAgent2D, NavigationRegion2D, NavigationServer2D |
| `disable_advanced_gui` | (docs list) AcceptDialog, ConfirmationDialog, FileDialog, CodeEdit, TextEdit, CodeHighlighter, SyntaxHighlighter, ColorPicker, ColorPickerButton, FoldableContainer, GraphEdit / GraphNode, MenuBar, MenuButton, **OptionButton**, **PopupMenu** (also LineEdit's right-click menu), RichTextLabel, RichTextEffect, SpinBox, SplitContainer (H/V), SubViewportContainer, Tree |
| `module_text_server_adv_enabled = "no"` + `fb = "yes"` | Arabic, Hebrew, Hindi, Thai, CJK shaping, font ligatures / OpenType features. Latin, Greek, Cyrillic are fine. |

**Modules** (`modules_enabled_by_default = "no"` turns all off, then list the ones needed):
- always: `gdscript`, `freetype`, `text_server_fb`, `svg`, `webp`
- `.ogg` audio: `ogg` + `vorbis`; `.mp3`: `mp3`; `.jpg` images: `jpg`
- `RegEx`: `regex`; `FastNoiseLite` / `NoiseTexture2D`: `noise`
- MSDF fonts: `msdfgen`; WebSocketPeer: `websocket`; WebRTC: `webrtc`
- Module names = folders in `modules/` of the Godot source at your tag
  (`https://github.com/godotengine/godot/tree/<tag>/modules`).

Note: `.png` and `.wav` are core (no module). TileMapLayer / TileSet are core in 4.6.

### Do NOT use the editor's "Detect from Project" profile unedited
*Project > Tools > Engine Compilation Configuration Editor > Detect from Project* makes a
`.gdbuild` file. For Orbital Tapper it removed things the game needs **indirectly**
(it only looks for class names written in the game files): `FontFile` / `TextServer`
(all text), `AudioStreamPlayback` / `OggPacketSequencePlayback` / `AudioSample` (all sound
on web), `ScrollBar` (every ScrollContainer), `Popup` (OptionButton's menu), `SceneState`,
`ResourceLoader`, `World2D`, `GDScriptNativeClass` (engine internals). The game would have
broken. If you ever want one: start from the detected file, remove every engine-internal or
parent class from `disabled_classes`, save it as `build_profile.gdbuild` in this repo
(the workflow then uses it automatically), and test the export very carefully.
The options-file approach above already gives most of the saving.

---

## Things we learned (avoid these)

- **No heavy builds on the home PC.** `lto=full` needs 12-16 GB RAM; on an 8 GB PC the link
  step died silently after 29 minutes. That is why the build runs on GitHub.
- **Tag = editor version, exactly.** 4.6-stable template for a 4.6-stable editor.
- **Thread setting must match.** `threads=no` here and *Thread Support* off in the preset.
  The workflow passes `threads=no` on the command line as well as in the options file.
- **Output name** in `bin/` is `godot.web.template_release.wasm32.nothreads.zip`; the workflow
  finds it and renames it to `web_nothreads_release.zip`.
- **Artifacts expire** after 90 days (GitHub default) - keep the downloaded zip with the game.
- **New Godot version = rebuild** with the new tag and its Emscripten version.

## Also worth checking (no rebuild needed)
Does the hosting serve the `.wasm` compressed? Browser DevTools > Network > `index.wasm`
> Response headers: `content-encoding: gzip` or `br`. Without it, players download the raw
size (23 MB instead of 5.5 MB).
