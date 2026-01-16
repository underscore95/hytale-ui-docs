[← Back](../Types.md)

# TabNavigationStyle

**First used at:** `Common.ui:620`

## Fields

### TabStyle
Example Values:

- `(
    Default: @HeaderTabStyle
  )`
- `(
    Default: @TopTabStyle,
    Hovered: (...@TopTabStyle, Anchor: (...@TopTabAnchor, Bottom: -5)),
    Pressed: (...@TopTabStyle, Anchor: (...@TopTabAnchor, Bottom: -8))
  )`

### SelectedTabStyle
Example Values:

- `(
    Default: (
      ...@TopTabStyle,
      Anchor: (...@TopTabAnchor, Bottom: 4),
      IconAnchor: (Width: 44, Height: 44),
      Overlay: "Common/TabSelectedOverlay.png"
    )
  )`
- `(
    Default: (
      ...@HeaderTabStyle,
      IconOpacity: 1
    )
  )`

### SeparatorAnchor
Example Values:

- `(Width: 5, Height: 34)`

### SeparatorBackground
Example Values:

- `"Common/HeaderTabSeparator.png"`

