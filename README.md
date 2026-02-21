# Harran Virus Evolved (Dying Light 1 Mod Kit)

This repository now contains a **ready-to-tune mod kit** for a Dying Light 1 overhaul where infected behave like:

- **28 Days Later infected** (fast, relentless, aggressive pursuit), plus
- **Death Angel-style traits** from *A Quiet Place* (noise hunting, armored plates, burst dash behavior).

> This is a source mod project (editable values + generated override files), intended to be merged into your Dying Light `Data3.pak` workflow using standard DL1 modding tools.

## What is included

- `mods/HarranVirusEvolved/profiles/default.profile.json`
  - Main balance profile for movement, aggression, armor, and spawn logic.
- `mods/HarranVirusEvolved/data/templates/*.xml.tpl`
  - Parameterized templates for zombie stats, special abilities, and spawn rules.
- `tools/build_mod.py`
  - Build script that converts profile values into generated XML overrides.
- `mods/HarranVirusEvolved/generated/*.xml`
  - Output files created by the build script (safe to regenerate anytime).

## Quick start

1. Build generated files:

   ```bash
   python3 tools/build_mod.py
   ```

2. Copy generated XML files into your unpacked Dying Light data override structure.
3. Repack as `Data3.pak` and load in game.

## Gameplay vision implemented

### 28 Days Later behaviors

- Higher infected movement speed and longer sprint uptime.
- Lower reaction time for more immediate threat response.
- Bigger leap range to collapse distance quickly.
- Increased night aggression.

### Death Angel-inspired abilities

- **Echolocation sweep:** loud actions trigger fast regroup/investigation behavior.
- **Armor plating:** heavy frontal mitigation except when “plate-open” window occurs.
- **Hyper dash:** cooldown-based burst rush to rapidly close gaps.

## Tuning guide

Edit `mods/HarranVirusEvolved/profiles/default.profile.json`:

- `zombie.runner.move_speed_multiplier`
- `death_angel_abilities.echolocation.noise_trigger_distance_meters`
- `death_angel_abilities.armor_plating.frontal_damage_reduction`
- `death_angel_abilities.hyper_dash.*`
- `spawn.*`

Rebuild after each change:

```bash
python3 tools/build_mod.py
```

## Notes

- This project gives you a reproducible balancing pipeline and drop-in override files.
- Final in-game behavior still depends on your exact Dying Light data tables and merge points.
- The linked Dying Light modding wiki is a good reference for mapping generated XML keys to your preferred game data files.
