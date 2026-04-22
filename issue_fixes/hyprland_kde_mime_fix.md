# Hyprland + Dolphin (KDE apps) — MIME / Open With Fix

## Problem

In Hyprland:

- Dolphin “Open With” shows only history
- No applications listed for `.pdf`, `.txt`, etc.
- `kioclient exec <file>` opens empty chooser

## Root Cause

Hyprland session is missing required XDG environment variables for KDE.

Result:

- KDE cannot resolve MIME → application
- Dolphin shows empty app list

## Fix

### 1. Add environment variables

Edit:

```bash
~/.config/hypr/hyprland.conf
```

Add:

```ini
env = XDG_DATA_DIRS,/usr/local/share:/usr/share
env = XDG_CONFIG_DIRS,/home/<user>/.config/kdedefaults:/etc/xdg
env = XDG_MENU_PREFIX,plasma-

env = XDG_CURRENT_DESKTOP,Hyprland
env = XDG_SESSION_DESKTOP,Hyprland
env = XDG_SESSION_TYPE,wayland
```

Replace `<user>` with your username.

______________________________________________________________________

### 2. Restart session

Fully logout and login again
(do NOT use `hyprctl reload`)

______________________________________________________________________

### 3. Rebuild KDE cache

```bash
kbuildsycoca6 --noincremental
```

______________________________________________________________________

## Verification

```bash
xdg-open test.pdf
xdg-open test.txt
```

Expected:

- PDF → opens in Okular
- TXT → opens in Kate (or your chosen editor)

In Dolphin:

- Right click → Open With → apps are listed

______________________________________________________________________

## Notes

- No need to modify `.desktop` files
- No need to manually tweak MIME mappings
- Works with:
  - Dolphin
  - Okular
  - Kate

______________________________________________________________________

## Recovery (if it breaks again)

```bash
kbuildsycoca6 --noincremental
```

______________________________________________________________________

## Takeaway

Using KDE apps inside Hyprland requires minimal XDG environment glue.

Without it → MIME resolution breaks.
