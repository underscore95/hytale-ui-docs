[← Back](../Variables.md)

# DefaultCheckBoxStyle ⚠️

⚠️ This variable has only been found in Client ui files, you may or may not be able to use it in mods.

**Defined at:** `Client/Data/Game/Interface/Common.ui:326`

## Value

```ui
CheckBoxStyle(
  Unchecked: (
    DefaultBackground: (Color: #00000000),
    HoveredBackground: (Color: #00000000),
    PressedBackground: (Color: #00000000),
    DisabledBackground: (Color: #424242),
    ChangedSound: (SoundPath: $Sounds.@Untick, Volume: 6)
  ),
  Checked: (
    DefaultBackground: (TexturePath: "Common/Checkmark.png"),
    HoveredBackground: (TexturePath: "Common/Checkmark.png"),
    PressedBackground: (TexturePath: "Common/Checkmark.png"),
    ChangedSound: (SoundPath: $Sounds.@Tick, Volume: 6)
  )
)
```
