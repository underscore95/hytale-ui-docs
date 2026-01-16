[← Back](../Types.md)

# PatchStyle

**First used at:** `Common.ui:30`

## Fields

### TexturePath
Example Values:

- `"Common/Buttons/Primary_Pressed.png"`
- `"InputBinding.png"`
- `"InputIconMouseMiddleClick.png"`
- `"Common/InputBoxSelected.png"`
- `"Common/Buttons/Disabled.png"`
- `"Common/Buttons/Primary_Square.png"`
- `"Common/InputBoxPressed.png"`
- `"Common/Buttons/Primary_Square_Hovered.png"`
- `"Common/Buttons/Primary_Square_Pressed.png"`
- `"InputIconMouseRightClick.png"`
- `"Common/InputBox.png"`
- `"Common/Buttons/Primary.png"`
- `"Common/Buttons/Primary_Hovered.png"`
- `"InputIconMouseLeftClick.png"`
- `"Common/InputBoxHovered.png"`

### VerticalBorder
Example Values:

- `[ButtonBorder](Variables/ButtonBorder.md)`

### HorizontalBorder
Example Values:

- `80`

### Border
Example Values:

- `[ButtonBorder](Variables/ButtonBorder.md)`
- `6`
- `16`

### (TexturePath: "Common/Buttons/Destructive.png", Border: @ButtonBorder), LabelStyle
Example Values:

- `[DefaultButtonLabelStyle),
  Hovered: (Background: PatchStyle(TexturePath: "Common/Buttons/Destructive_Hovered.png", Border: @ButtonBorder)](Variables/DefaultButtonLabelStyle-----Hovered---Background--PatchStyle-TexturePath---Common-Buttons-Destructive_Hovered-png---Border---ButtonBorder-.md)`

### LabelStyle
Example Values:

- `[DefaultButtonLabelStyle),
  Sounds: @ButtonsCancel,](Variables/DefaultButtonLabelStyle-----Sounds---ButtonsCancel-.md)`
- `[SmallSecondaryButtonLabelStyle)](Variables/SmallSecondaryButtonLabelStyle-.md)`
- `[SecondaryButtonLabelStyle)](Variables/SecondaryButtonLabelStyle-.md)`

### (TexturePath: "Common/Buttons/Destructive_Hovered.png", Border: @ButtonBorder), LabelStyle
Example Values:

- `[DefaultButtonLabelStyle),
  Pressed: (Background: PatchStyle(TexturePath: "Common/Buttons/Destructive_Pressed.png", Border: @ButtonBorder)](Variables/DefaultButtonLabelStyle-----Pressed---Background--PatchStyle-TexturePath---Common-Buttons-Destructive_Pressed-png---Border---ButtonBorder-.md)`

### (TexturePath: "Common/Buttons/Destructive_Pressed.png", Border: @ButtonBorder), LabelStyle
Example Values:

- `[DefaultButtonLabelStyle),
  Disabled: (Background: PatchStyle(TexturePath: "Common/Buttons/Disabled.png", Border: @ButtonBorder)](Variables/DefaultButtonLabelStyle-----Disabled---Background--PatchStyle-TexturePath---Common-Buttons-Disabled-png---Border---ButtonBorder-.md)`

### (TexturePath: "Common/Buttons/Disabled.png", Border: @ButtonBorder), LabelStyle
Example Values:

- `[DefaultButtonLabelStyle),
  Sounds: @ButtonsCancel,](Variables/DefaultButtonLabelStyle-----Sounds---ButtonsCancel-.md)`
- `[SmallSecondaryButtonLabelStyle)](Variables/SmallSecondaryButtonLabelStyle-.md)`
- `[SecondaryButtonLabelStyle)](Variables/SecondaryButtonLabelStyle-.md)`

### (TexturePath: "Common/Buttons/Destructive.png", Border: @ButtonBorder)),  Hovered: (Background
Example Values:

- `PatchStyle(TexturePath: "Common/Buttons/Destructive_Hovered.png", Border: @ButtonBorder)),
  Pressed: (Background: PatchStyle(TexturePath: "Common/Buttons/Destructive_Pressed.png", Border: @ButtonBorder)),
  Disabled: (Background: PatchStyle(TexturePath: "Common/Buttons/Disabled.png", Border: @ButtonBorder)),
  Sounds: @ButtonSounds,`

### (TexturePath: "Common/Buttons/Destructive_Hovered.png", Border: @ButtonBorder)),  Pressed: (Background
Example Values:

- `PatchStyle(TexturePath: "Common/Buttons/Destructive_Pressed.png", Border: @ButtonBorder)),
  Disabled: (Background: PatchStyle(TexturePath: "Common/Buttons/Disabled.png", Border: @ButtonBorder)),
  Sounds: @ButtonSounds,`

### (TexturePath: "Common/Buttons/Destructive_Pressed.png", Border: @ButtonBorder)),  Disabled: (Background
Example Values:

- `PatchStyle(TexturePath: "Common/Buttons/Disabled.png", Border: @ButtonBorder)),
  Sounds: @ButtonSounds,`

### (TexturePath: "Common/Buttons/Disabled.png", Border: @ButtonBorder)),  Sounds: @ButtonSounds,
Example Values:

- ``

### (TexturePath: "Common/Buttons/Secondary.png", Border: @ButtonBorder)),  Hovered: (Background
Example Values:

- `PatchStyle(TexturePath: "Common/Buttons/Secondary_Hovered.png", Border: @ButtonBorder)),
  Pressed: (Background: PatchStyle(TexturePath: "Common/Buttons/Secondary_Pressed.png", Border: @ButtonBorder)),
  Disabled: (Background: PatchStyle(TexturePath: "Common/Buttons/Disabled.png", Border: @ButtonBorder)),
  Sounds: @ButtonSounds,`

### (TexturePath: "Common/Buttons/Secondary_Hovered.png", Border: @ButtonBorder)),  Pressed: (Background
Example Values:

- `PatchStyle(TexturePath: "Common/Buttons/Secondary_Pressed.png", Border: @ButtonBorder)),
  Disabled: (Background: PatchStyle(TexturePath: "Common/Buttons/Disabled.png", Border: @ButtonBorder)),
  Sounds: @ButtonSounds,`

### (TexturePath: "Common/Buttons/Secondary_Pressed.png", Border: @ButtonBorder)),  Disabled: (Background
Example Values:

- `PatchStyle(TexturePath: "Common/Buttons/Disabled.png", Border: @ButtonBorder)),
  Sounds: @ButtonSounds,`

### (TexturePath: "Common/Buttons/Secondary.png", Border: @ButtonBorder), LabelStyle
Example Values:

- `[SecondaryButtonLabelStyle),
  Hovered: (Background: PatchStyle(TexturePath: "Common/Buttons/Secondary_Hovered.png", Border: @ButtonBorder)](Variables/SecondaryButtonLabelStyle-----Hovered---Background--PatchStyle-TexturePath---Common-Buttons-Secondary_Hovered-png---Border---ButtonBorder-.md)`
- `[SmallSecondaryButtonLabelStyle),
  Hovered: (Background: PatchStyle(TexturePath: "Common/Buttons/Secondary_Hovered.png", Border: @ButtonBorder)](Variables/SmallSecondaryButtonLabelStyle-----Hovered---Background--PatchStyle-TexturePath---Common-Buttons-Secondary_Hovered-png---Border---ButtonBorder-.md)`

### (TexturePath: "Common/Buttons/Secondary_Hovered.png", Border: @ButtonBorder), LabelStyle
Example Values:

- `[SecondaryButtonLabelStyle),
  Pressed: (Background: PatchStyle(TexturePath: "Common/Buttons/Secondary_Pressed.png", Border: @ButtonBorder)](Variables/SecondaryButtonLabelStyle-----Pressed---Background--PatchStyle-TexturePath---Common-Buttons-Secondary_Pressed-png---Border---ButtonBorder-.md)`
- `[SmallSecondaryButtonLabelStyle),
  Pressed: (Background: PatchStyle(TexturePath: "Common/Buttons/Secondary_Pressed.png", Border: @ButtonBorder)](Variables/SmallSecondaryButtonLabelStyle-----Pressed---Background--PatchStyle-TexturePath---Common-Buttons-Secondary_Pressed-png---Border---ButtonBorder-.md)`

### (TexturePath: "Common/Buttons/Secondary_Pressed.png", Border: @ButtonBorder), LabelStyle
Example Values:

- `[SecondaryButtonLabelStyle),
  Disabled: (Background: PatchStyle(TexturePath: "Common/Buttons/Disabled.png", Border: @ButtonBorder)](Variables/SecondaryButtonLabelStyle-----Disabled---Background--PatchStyle-TexturePath---Common-Buttons-Disabled-png---Border---ButtonBorder-.md)`
- `[SmallSecondaryButtonLabelStyle),
  Disabled: (Background: PatchStyle(TexturePath: "Common/Buttons/Disabled.png", Border: @ButtonBorder)](Variables/SmallSecondaryButtonLabelStyle-----Disabled---Background--PatchStyle-TexturePath---Common-Buttons-Disabled-png---Border---ButtonBorder-.md)`

### (TexturePath: "Common/Buttons/Tertiary.png", Border: @ButtonBorder)),  Hovered: (Background
Example Values:

- `PatchStyle(TexturePath: "Common/Buttons/Tertiary_Hovered.png", Border: @ButtonBorder)),
  Pressed: (Background: PatchStyle(TexturePath: "Common/Buttons/Tertiary_Pressed.png", Border: @ButtonBorder)),
  Disabled: (Background: PatchStyle(TexturePath: "Common/Buttons/Disabled.png", Border: @ButtonBorder)),
  Sounds: @ButtonSounds,`

### (TexturePath: "Common/Buttons/Tertiary_Hovered.png", Border: @ButtonBorder)),  Pressed: (Background
Example Values:

- `PatchStyle(TexturePath: "Common/Buttons/Tertiary_Pressed.png", Border: @ButtonBorder)),
  Disabled: (Background: PatchStyle(TexturePath: "Common/Buttons/Disabled.png", Border: @ButtonBorder)),
  Sounds: @ButtonSounds,`

### (TexturePath: "Common/Buttons/Tertiary_Pressed.png", Border: @ButtonBorder)),  Disabled: (Background
Example Values:

- `PatchStyle(TexturePath: "Common/Buttons/Disabled.png", Border: @ButtonBorder)),
  Sounds: @ButtonSounds,`

### (TexturePath: "Common/Buttons/Tertiary.png", Border: @ButtonBorder), LabelStyle
Example Values:

- `[SecondaryButtonLabelStyle),
  Hovered: (Background: PatchStyle(TexturePath: "Common/Buttons/Tertiary_Hovered.png", Border: @ButtonBorder)](Variables/SecondaryButtonLabelStyle-----Hovered---Background--PatchStyle-TexturePath---Common-Buttons-Tertiary_Hovered-png---Border---ButtonBorder-.md)`

### (TexturePath: "Common/Buttons/Tertiary_Hovered.png", Border: @ButtonBorder), LabelStyle
Example Values:

- `[SecondaryButtonLabelStyle),
  Pressed: (Background: PatchStyle(TexturePath: "Common/Buttons/Tertiary_Pressed.png", Border: @ButtonBorder)](Variables/SecondaryButtonLabelStyle-----Pressed---Background--PatchStyle-TexturePath---Common-Buttons-Tertiary_Pressed-png---Border---ButtonBorder-.md)`

### (TexturePath: "Common/Buttons/Tertiary_Pressed.png", Border: @ButtonBorder), LabelStyle
Example Values:

- `[SecondaryButtonLabelStyle),
  Disabled: (Background: PatchStyle(TexturePath: "Common/Buttons/Disabled.png", Border: @ButtonBorder)](Variables/SecondaryButtonLabelStyle-----Disabled---Background--PatchStyle-TexturePath---Common-Buttons-Disabled-png---Border---ButtonBorder-.md)`

