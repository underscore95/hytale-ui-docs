[← Back](../Variables.md)

# HeaderTabsStyle ⚠️

⚠️ This variable has only been found in Client ui files, you may or may not be able to use it in mods.

**Defined at:** `Client/Data/Game/Interface/Common\Container.ui:102`

## Value

```ui
TabNavigationStyle(
  TabStyle: (
    Default: @HeaderTabStyle,
    Hovered: (...@HeaderTabStyle, IconOpacity: 0.6),
    Pressed: (...@HeaderTabStyle, IconOpacity: 0.8)
  ),
  SelectedTabStyle: (
    Default: (
      ...@HeaderTabStyle,
      IconOpacity: 1,
      Background: (TexturePath: "HeaderTabSelectedBackground.png", Border: 7),
      ContentMaskTexturePath: "SelectedIconGradient.png"
    )
  ),
  TabSounds: (
    Activate: (SoundPath: $Sounds.@CreativeTab, Volume: 6)
  ))
```
