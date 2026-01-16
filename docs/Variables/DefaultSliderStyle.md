[← Back](../Variables.md)

# DefaultSliderStyle ⚠️

⚠️ This variable has only been found in Client ui files, you may or may not be able to use it in mods.

**Defined at:** `Client/Data/Game/Interface/Common.ui:315`

## Value

```ui
SliderStyle(
  Background: (TexturePath: "Common/SliderBackground.png", Border: 2),
  Handle: "Common/SliderHandle.png",
  HandleWidth: 16,
  HandleHeight: 16,
  Sounds: (
    Activate: $Sounds.@SliderRelease,
    MouseHover: (SoundPath: $Sounds.@ButtonsLightHover, Volume: 6)
  )
)
```
