# TopTabsStyle

**Defined at:** `Common.ui:620`

## Value

```ui
TabNavigationStyle(
  TabStyle: (
    Default: @TopTabStyle,
    Hovered: (...@TopTabStyle, Anchor: (...@TopTabAnchor, Bottom: -5)),
    Pressed: (...@TopTabStyle, Anchor: (...@TopTabAnchor, Bottom: -8))
  ),
  SelectedTabStyle: (
    Default: (
      ...@TopTabStyle,
      Anchor: (...@TopTabAnchor, Bottom: 4),
      IconAnchor: (Width: 44, Height: 44),
      Overlay: "Common/TabSelectedOverlay.png"
    )
  ))
```
