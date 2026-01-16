[← Back](../Types.md)

# TabNavigationStyle

This type has been found in Server ui files, you should be able to use it in mods.

**First used at:** `Common.ui:620`

## Fields

### TabStyle
Example Values:

- `(
    Default: @IconOnlyTopTabStyle,
    Hovered: (...@IconOnlyTopTabStyle, Anchor: (...@IconOnlyTopTabAnchor, Bottom: -5)),
    Pressed: (...@IconOnlyTopTabStyle, Anchor: (...@IconOnlyTopTabAnchor, Bottom: -8))
  )`
- `(
    Default: @TextTopTabStyle,
    Hovered: (...@TextTopTabStyle, Anchor: (...@TextTopTabAnchor, Bottom: -5)),
    Pressed: (...@TextTopTabStyle, Anchor: (...@TextTopTabAnchor, Bottom: -8))
  )`
- `(
    Default: @HeaderTabStyle,
    Hovered: (...@HeaderTabStyle, IconOpacity: 0.6),
    Pressed: (...@HeaderTabStyle, IconOpacity: 0.8)
  )`
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
      ...@TextTopTabStyle,
      Anchor: (...@TextTopTabAnchor, Bottom: 0),
      IconAnchor: (Width: 44, Height: 44),
      Overlay: "TabSelectedOverlay.png",
      LabelStyle: (FontSize: 19, TextColor: #f0de7bff, RenderBold: true),
    )
  )`
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
      ...@IconOnlyTopTabStyle,
      Anchor: (...@IconOnlyTopTabAnchor, Bottom: 0),
      IconAnchor: (Width: 44, Height: 44),
      Overlay: "TabSelectedOverlay.png"
    )
  )`
- `(
    Default: (
      ...@HeaderTabStyle,
      IconOpacity: 1,
      Background: (TexturePath: "HeaderTabSelectedBackground.png", Border: 7),
      ContentMaskTexturePath: "SelectedIconGradient.png"
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

### TabSounds
Example Values:

- `$Sounds.@DefaultTabNavigation`
- `(
    Activate: (SoundPath: $Sounds.@CreativeTab, Volume: 6)
  )`

