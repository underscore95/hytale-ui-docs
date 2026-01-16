[← Back](../Variables.md)

# FileDropdownBoxStyle ⚠️

⚠️ This variable has only been found in Client ui files, you may or may not be able to use it in mods.

**Defined at:** `Client/Data/Game/Interface/Common\Settings\FileSelectorDropdownSetting.ui:3`

## Value

```ui
FileDropdownBoxStyle(
  DefaultBackground: (TexturePath: "../Dropdown.png", Border: 16),
  HoveredBackground: (TexturePath: "../DropdownHovered.png", Border: 16),
  PressedBackground: (TexturePath: "../DropdownPressed.png", Border: 16),
  DefaultArrowTexturePath: "../DefaultDropdownCaret.png",
  HoveredArrowTexturePath: "../DefaultDropdownCaret.png",
  PressedArrowTexturePath: "../PressedDropdownCaret.png",
  ArrowWidth: 13,
  ArrowHeight: 18,
  HorizontalPadding: 12,
  LabelStyle: (
    ...$Common.@DefaultDropdownBoxLabelStyle,
    FontSize: 16
  )
)
```
