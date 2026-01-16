[← Back](../Variables.md)

# TitledDropdownBoxStyle ⚠️

⚠️ This variable has only been found in Client ui files, you may or may not be able to use it in mods.

**Defined at:** `Client/Data/Game/Interface/Common.ui:375`

## Value

```ui
DropdownBoxStyle(
  ...@DefaultDropdownBoxStyle,
  DefaultBackground: (TexturePath: "Common/DropdownAlt.png", Border: 16),
  HoveredBackground: (TexturePath: "Common/DropdownAltHovered.png", Border: 16),
  PressedBackground: (TexturePath: "Common/DropdownAltHovered.png", Border: 16),
  DefaultArrowTexturePath: "Common/AltDropdownCaretDown.png",
  HoveredArrowTexturePath: "Common/AltDropdownCaretDown.png",
  PressedArrowTexturePath: "Common/AltDropdownCaretUp.png",
  ArrowWidth: 12,
  ArrowHeight: 7,
  PanelTitleLabelStyle: LabelStyle(TextColor: #96a9be, RenderBold: true, RenderUppercase: true, VerticalAlignment: Center, FontSize: 13),
  PanelPadding: 29,
  PanelAlign: Bottom,
  PanelBackground: (TexturePath: "Common/TitledDropdownBox.png", Border: 57),
  HoveredEntryBackground: (Color: #252e48),
  PressedEntryBackground: (Color: #232b44),
  Sounds: $Sounds.@DropdownBox
)
```
