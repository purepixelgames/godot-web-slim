# godot-web-slim

Builds a slim Godot **web** export template (2D only, no threads) in GitHub Actions,
from the unmodified official source `godotengine/godot`. Nothing is built locally.

- Options: `custom.py` (3D, physics, navigation, XR and unused modules off).
- Optional: put a `build_profile.gdbuild` (Godot editor: Project > Tools > Engine
  Compilation Configuration > Detect from Project) in the repo root to strip unused
  classes as well. Test the export carefully - detection can be too aggressive.

## Use

1. Actions -> **Build slim web template** -> Run workflow. Keep `godot_ref` equal to the
   editor version that exports the game (`4.6-stable` today).
2. Download the artifact `web-slim-<ref>` -> `web_nothreads_release.zip`.
3. In the game's Web export preset set **Custom Template > Release** to that zip
   (thread support stays off). Clear the field to go back to the stock template.

Only the release template is slim; debug exports use the stock template.
