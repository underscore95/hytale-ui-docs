[← Back](../Types.md)

# DropdownBoxStyle

**First used at:** `Common.ui:447`

## Fields

### DefaultBackground

Example Values:
- `(TexturePath: "Common/Dropdown.png", Border: 16)`

### HoveredBackground

Example Values:
- `(TexturePath: "Common/DropdownHovered.png", Border: 16)`

### PressedBackground

Example Values:
- `(TexturePath: "Common/DropdownPressed.png", Border: 16)`

### DefaultArrowTexturePath

Example Values:
- `"Common/DropdownCaret.png"`

### HoveredArrowTexturePath

Example Values:
- `"Common/DropdownCaret.png"`

### PressedArrowTexturePath

Example Values:
- `"Common/DropdownPressedCaret.png"`

### ArrowWidth

Example Values:
- `13`
- `9`

### ArrowHeight

Example Values:
- `18`

### LabelStyle

Example Values:
- `(TextColor: #96a9be, RenderBold: true, VerticalAlignment: Center, FontSize: 18)`
- `[DefaultDropdownBoxLabelStyle](Variables/DefaultDropdownBoxLabelStyle.md)`

### EntryLabelStyle

Example Values:
- `[DefaultDropdownBoxEntryLabelStyle](Variables/DefaultDropdownBoxEntryLabelStyle.md)`

### NoItemsLabelStyle

Example Values:
- `(...@DefaultDropdownBoxEntryLabelStyle, TextColor: #b7cedd(0.5))`

### SelectedEntryLabelStyle

Example Values:
- `(...@DefaultDropdownBoxEntryLabelStyle, RenderBold: true)`

### HorizontalPadding

Example Values:
- `8`
- `14`

### PanelScrollbarStyle

Example Values:
- `[DefaultScrollbarStyle](Variables/DefaultScrollbarStyle.md)`

### PanelBackground

Example Values:
- `(TexturePath: "Common/DropdownBox.png", Border: 16)`

### PanelPadding

Example Values:
- `6`

### PanelAlign

Example Values:
- `Right`
- `Bottom`

### PanelOffset

Example Values:
- `7`

### EntryHeight

Example Values:
- `31`

### EntriesInViewport

Example Values:
- `10`

### HorizontalEntryPadding

Example Values:
- `7`

### HoveredEntryBackground

Example Values:
- `(Color: #0a0f17)`

### PressedEntryBackground

Example Values:
- `(Color: #0f1621)`

### Sounds

Example Values:
- `$Sounds.@DropdownBox`

### EntrySounds

Example Values:
- `$Sounds.@ButtonsLight`

### FocusOutlineSize

Example Values:
- `1`

### FocusOutlineColor

Example Values:
- `#ffffff(0.4)`

### //   ...@DefaultDropdownBoxStyle,//   DefaultBackground

Example Values:
- `(TexturePath: "Common/DropdownAlt.png", Border: 16)`

### //   HoveredBackground

Example Values:
- `(TexturePath: "Common/DropdownAltHovered.png", Border: 16)`

### //   PressedBackground

Example Values:
- `(TexturePath: "Common/DropdownAltHovered.png", Border: 16)`

### //   DefaultArrowTexturePath

Example Values:
- `"Common/AltDropdownCaretDown.png"`

### //   HoveredArrowTexturePath

Example Values:
- `"Common/AltDropdownCaretDown.png"`

### //   PressedArrowTexturePath

Example Values:
- `"Common/AltDropdownCaretUp.png"`

### //   ArrowWidth

Example Values:
- `12`

### //   ArrowHeight

Example Values:
- `7`

### //   PanelTitleLabelStyle

Example Values:
- `LabelStyle(TextColor: #96a9be, RenderBold: true, RenderUppercase: true, VerticalAlignment: Center, FontSize: 13)`

### //   PanelPadding

Example Values:
- `29`

### //   PanelAlign

Example Values:
- `Bottom`

### //   PanelBackground

Example Values:
- `(TexturePath: "Common/TitledDropdownBox.png", Border: 57)`

### //   HoveredEntryBackground

Example Values:
- `(Color: #252e48)`

### //   PressedEntryBackground

Example Values:
- `(Color: #232b44)`

### //   Sounds

Example Values:
- `$Sounds.@DropdownBox
// );

@DefaultFileDropdownBoxStyle = FileDropdownBoxStyle(
  DefaultBackground: (TexturePath: "Common/Dropdown.png", Border: 16)`

