[← Back](../Variables.md)

# IconOnlyTopTabsStyle ⚠️

⚠️ This variable has only been found in Client ui files, you may or may not be able to use it in mods.

**Defined at:** `Client/Data/Game/Interface/Common\Container.ui:60`

## Value

```ui
TabNavigationStyle(
  TabStyle: (
    Default: @IconOnlyTopTabStyle,
    Hovered: (...@IconOnlyTopTabStyle, Anchor: (...@IconOnlyTopTabAnchor, Bottom: -5)),
    Pressed: (...@IconOnlyTopTabStyle, Anchor: (...@IconOnlyTopTabAnchor, Bottom: -8))
  ),
  SelectedTabStyle: (
    Default: (
      ...@IconOnlyTopTabStyle,
      Anchor: (...@IconOnlyTopTabAnchor, Bottom: 0),
      IconAnchor: (Width: 44, Height: 44),
      Overlay: "TabSelectedOverlay.png"
    )
  ),
  TabSounds: $Sounds.@DefaultTabNavigation
)
```
