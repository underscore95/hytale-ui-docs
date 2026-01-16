[← Back](../Variables.md)

# TextTopTabsStyle ⚠️

⚠️ This variable has only been found in Client ui files, you may or may not be able to use it in mods.

**Defined at:** `Client/Data/Game/Interface/Common\Container.ui:77`

## Value

```ui
TabNavigationStyle(
  TabStyle: (
    Default: @TextTopTabStyle,
    Hovered: (...@TextTopTabStyle, Anchor: (...@TextTopTabAnchor, Bottom: -5)),
    Pressed: (...@TextTopTabStyle, Anchor: (...@TextTopTabAnchor, Bottom: -8))
  ),
  SelectedTabStyle: (
    Default: (
      ...@TextTopTabStyle,
      Anchor: (...@TextTopTabAnchor, Bottom: 0),
      IconAnchor: (Width: 44, Height: 44),
      Overlay: "TabSelectedOverlay.png",
      LabelStyle: (FontSize: 19, TextColor: #f0de7bff, RenderBold: true),
    )
  ),
  TabSounds: $Sounds.@DefaultTabNavigation
)
```
