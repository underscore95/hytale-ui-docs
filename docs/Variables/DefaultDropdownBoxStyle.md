[← Back](../Variables.md)

# DefaultDropdownBoxStyle ⚠️

⚠️ This variable has only been found in Client ui files, you may or may not be able to use it in mods.

**Defined at:** `Client/Data/Game/Interface/Common.ui:345`

## Value

```ui
DropdownBoxStyle(
  DefaultBackground: (TexturePath: "Common/Dropdown.png", Border: 16),
  HoveredBackground: (TexturePath: "Common/DropdownHovered.png", Border: 16),
  PressedBackground: (TexturePath: "Common/DropdownPressed.png", Border: 16),
  DefaultArrowTexturePath: "Common/DefaultDropdownCaret.png",
  HoveredArrowTexturePath: "Common/DefaultDropdownCaret.png",
  PressedArrowTexturePath: "Common/PressedDropdownCaret.png",
  ArrowWidth: 13,
  ArrowHeight: 18,
  LabelStyle: @DefaultDropdownBoxLabelStyle,
  EntryLabelStyle: @DefaultDropdownBoxEntryLabelStyle,
  NoItemsLabelStyle: (...@DefaultDropdownBoxEntryLabelStyle, TextColor: #b7cedd(0.5)),
  SelectedEntryLabelStyle: (...@DefaultDropdownBoxEntryLabelStyle, RenderBold: true),
  HorizontalPadding: 8,
  PanelScrollbarStyle: @DefaultScrollbarStyle,
  PanelBackground: (TexturePath: "Common/DropdownBox.png", Border: 16),
  PanelPadding: 6,
  PanelAlign: Right,
  PanelOffset: 7,
  EntryHeight: 31,
  EntriesInViewport: 10,
  HorizontalEntryPadding: 7,
  HoveredEntryBackground: (Color: #0a0f17),
  PressedEntryBackground: (Color: #0f1621),
  Sounds: $Sounds.@DropdownBox,
  EntrySounds: $Sounds.@ButtonsLight,
  FocusOutlineSize: 1,
  FocusOutlineColor: #ffffff(0.4)
)
```
