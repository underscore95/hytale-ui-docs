[← Back](../Variables.md)

# HeaderEndTextButton ⚠️

⚠️ This variable has only been found in Client ui files, you may or may not be able to use it in mods.

**Defined at:** `Client/Data/Game/Interface/Common\Container.ui:165`

## Value

```ui
TextButton = TextButton {
  @Sounds = ();
  Style: (
    ...@HeaderTextButtonStyle,
    Sounds: (
      Activate: (SoundPath: $Sounds.@Tick, Volume: 6),
      MouseHover: (SoundPath: $Sounds.@ButtonsLightHover, Volume: 6)
    )
  );
  Padding: (Right: 22, Left: 15, Bottom: 1);
}
```
