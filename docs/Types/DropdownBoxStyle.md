[← Back](../Types.md)

# DropdownBoxStyle

**First used at:** `Common.ui:447`

## Fields

### DefaultBackground

- `(TexturePath: "Common/Dropdown.png", Border: 16)`

### HoveredBackground

- `(TexturePath: "Common/DropdownHovered.png", Border: 16)`

### PressedBackground

- `(TexturePath: "Common/DropdownPressed.png", Border: 16)`

### DefaultArrowTexturePath

- `"Common/DropdownCaret.png"`

### HoveredArrowTexturePath

- `"Common/DropdownCaret.png"`

### PressedArrowTexturePath

- `"Common/DropdownPressedCaret.png"`

### ArrowWidth

- `9`
- `13`

### ArrowHeight

- `18`

### LabelStyle

- `[DefaultDropdownBoxLabelStyle](Variables/DefaultDropdownBoxLabelStyle.md)`
- `(TextColor: #96a9be, RenderBold: true, VerticalAlignment: Center, FontSize: 18)`

### EntryLabelStyle

- `[DefaultDropdownBoxEntryLabelStyle](Variables/DefaultDropdownBoxEntryLabelStyle.md)`

### NoItemsLabelStyle

- `(...@DefaultDropdownBoxEntryLabelStyle, TextColor: #b7cedd(0.5))`

### SelectedEntryLabelStyle

- `(...@DefaultDropdownBoxEntryLabelStyle, RenderBold: true)`

### HorizontalPadding

- `14`
- `8`

### PanelScrollbarStyle

- `[DefaultScrollbarStyle](Variables/DefaultScrollbarStyle.md)`

### PanelBackground

- `(TexturePath: "Common/DropdownBox.png", Border: 16)`

### PanelPadding

- `6`

### PanelAlign

- `Bottom`
- `Right`

### PanelOffset

- `7`

### EntryHeight

- `31`

### EntriesInViewport

- `10`

### HorizontalEntryPadding

- `7`

### HoveredEntryBackground

- `(Color: #0a0f17)`

### PressedEntryBackground

- `(Color: #0f1621)`

### Sounds

- `$Sounds.@DropdownBox`

### EntrySounds

- `$Sounds.@ButtonsLight`

### FocusOutlineSize

- `1`

### FocusOutlineColor

- `#ffffff(0.4)`

### //   ...@DefaultDropdownBoxStyle,//   DefaultBackground

- `(TexturePath: "Common/DropdownAlt.png", Border: 16)`

### //   HoveredBackground

- `(TexturePath: "Common/DropdownAltHovered.png", Border: 16)`

### //   PressedBackground

- `(TexturePath: "Common/DropdownAltHovered.png", Border: 16)`

### //   DefaultArrowTexturePath

- `"Common/AltDropdownCaretDown.png"`

### //   HoveredArrowTexturePath

- `"Common/AltDropdownCaretDown.png"`

### //   PressedArrowTexturePath

- `"Common/AltDropdownCaretUp.png"`

### //   ArrowWidth

- `12`

### //   ArrowHeight

- `7`

### //   PanelTitleLabelStyle

- `LabelStyle(TextColor: #96a9be, RenderBold: true, RenderUppercase: true, VerticalAlignment: Center, FontSize: 13)`

### //   PanelPadding

- `29`

### //   PanelAlign

- `Bottom`

### //   PanelBackground

- `(TexturePath: "Common/TitledDropdownBox.png", Border: 57)`

### //   HoveredEntryBackground

- `(Color: #252e48)`

### //   PressedEntryBackground

- `(Color: #232b44)`

### //   Sounds

- `$Sounds.@DropdownBox
// );

@DefaultFileDropdownBoxStyle = FileDropdownBoxStyle(
  DefaultBackground: (TexturePath: "Common/Dropdown.png", Border: 16)`

