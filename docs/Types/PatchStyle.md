[← Back](../Types.md)

# PatchStyle

This type has been found in Server ui files, you should be able to use it in mods.

**First used at:** `Common.ui:30`

## Fields

### TexturePath
Example Values:

- `"InputBinding.png"`
- `"Assets/OverlayAbilityErrorState.png"`
- `"Assets/BuffBackground.png"`
- `"Common/InputBox.png"`
- `"ItemListSlotUncraftable.png"`
- `"DiagramCraftingSlotInvalid.png"`
- `"StructuralCraftingSlot.png"`
- `"PartFrameSelected.png"`
- `"Assets/DisabledBackground.png"`
- `"Common/Buttons/Primary_Hovered.png"`
- `"InputIconMouseRightClick.png"`
- `"PartBackgroundSelected.png"`
- `"InputIconMouseRightClickHold.png"`
- `"DiagramCraftingTab.png"`
- `"Assets/DebuffBackground.png"`
- `"IngredientSlotValid.png"`
- `"DiagramCraftingTabActive.png"`
- `"DiagramCraftingSlot.png"`
- `"UndoIcon.png"`
- `"ItemListSlotSelectedOverlay.png"`
- `"../../../Common/SmallInputIconMouseRightClick.png"`
- `"DiagramCraftingSlotActive.png"`
- `"Common/Buttons/Primary_Square_Pressed.png"`
- `"SlotTierUpgradeLockedOverlay.png"`
- `"UndoIconDisabled.png"`
- `"../../../Common/SmallInputIconMouseLeftClick.png"`
- `"InputIconMouseMiddleClick.png"`
- `"Common/Buttons/Primary_Pressed.png"`
- `"../../../Common/SmallInputIconMouseMiddleClick.png"`
- `"../../Common/InputBox.png"`
- `"../../../Common/ContainerPatch.png"`
- `"../../Common/InputBoxHovered.png"`
- `"Assets/BackgroundAbility.png"`
- `"Common/Buttons/Primary.png"`
- `"Common/InputBoxPressed.png"`
- `"ObjectiveTaskIconComplete.png"`
- `"DiagramCraftingSlotValid.png"`
- `"../../../Common/InputIconKeyRight_White.png"`
- `"DiagramCraftingSlotLockedIcon.png"`
- `"Common/DropdownBox.png"`
- `"SecondaryButtonPressed.png"`
- `"RedoIcon.png"`
- `"Common/InputBoxSelected.png"`
- `"PauseButton.png"`
- `"Common/Buttons/Primary_Square.png"`
- `"PlayButton.png"`
- `"ItemListSlotUncraftableSelected.png"`
- `"InputIconMouseLeftClick.png"`
- `"SecondaryButtonHovered.png"`
- `"SlotDropItemIconAlt.png"`
- `"PartFrame.png"`
- `"RedoIconDisabled.png"`
- `"Common/Buttons/Disabled.png"`
- `"Common/Buttons/Primary_Square_Hovered.png"`
- `"InputIconMouseLeftClickHold.png"`
- `"../../Common/ButtonDisabled.png"`
- `"StructuralCraftingSlotSelected.png"`
- `"EmptyWorldTilePatch.png"`
- `"Common/InputBoxHovered.png"`
- `"SlotIconUnknownRecipe.png"`
- `"../../../Common/InputIconKeyUp_White.png"`
- `"ItemListSlot.png"`
- `"Assets/BackgroundSignatureAbilityReady.png"`
- `"../../../Common/InputIconKeyDown_White.png"`
- `"../../Common/InputBoxSelected.png"`
- `"ItemListSlotSelected.png"`
- `"DiagramCraftingSlotUnlockedIcon.png"`
- `"Assets/BackgroundSignatureAbilityNotReady.png"`
- `"IngredientSlot.png"`
- `"Assets/BackgroundAbilityOnUse.png"`
- `"../../../Common/InputIconKeyLeft_White.png"`
- `"ObjectiveTaskIconDefault.png"`
- `"SlotIconMemoryLocked.png"`

### VerticalBorder
Example Values:

- `[ButtonBorder](Variables/ButtonBorder.md)`
- `[ButtonBorderSize](Variables/ButtonBorderSize.md)`

### HorizontalBorder
Example Values:

- `80`

### Border
Example Values:

- `5`
- `4`
- `[ButtonBorder](Variables/ButtonBorder.md)`
- `[ButtonBorderSize](Variables/ButtonBorderSize.md)`
- `16`
- `6`
- `24`
- `8`
- `46`

### (TexturePath: "Common/Buttons/Destructive.png", Border: @ButtonBorder), LabelStyle
Example Values:

- `[DefaultButtonLabelStyle),
  Hovered: (Background: PatchStyle(TexturePath: "Common/Buttons/Destructive_Hovered.png", Border: @ButtonBorder)](Variables/DefaultButtonLabelStyle-----Hovered---Background--PatchStyle-TexturePath---Common-Buttons-Destructive_Hovered-png---Border---ButtonBorder-.md)`

### LabelStyle
Example Values:

- `[SecondaryButtonLabelStyle)](Variables/SecondaryButtonLabelStyle-.md)`
- `[SecondaryButtonDisabledLabelStyle)](Variables/SecondaryButtonDisabledLabelStyle-.md)`
- `[SmallSecondaryButtonLabelStyle)](Variables/SmallSecondaryButtonLabelStyle-.md)`
- `[TagTextButtonLabelStyle)](Variables/TagTextButtonLabelStyle-.md)`
- `[DefaultButtonLabelStyle),
  Sounds: @ButtonsCancel,](Variables/DefaultButtonLabelStyle-----Sounds---ButtonsCancel-.md)`
- `$Common.@SecondaryButtonLabelStyle)`
- `[PrimaryButtonLabelStyle),
  Sounds: @ButtonDestructiveSounds,](Variables/PrimaryButtonLabelStyle-----Sounds---ButtonDestructiveSounds-.md)`
- `[SmallSecondaryButtonDisabledLabelStyle)](Variables/SmallSecondaryButtonDisabledLabelStyle-.md)`

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

- `[SecondaryButtonLabelStyle)](Variables/SecondaryButtonLabelStyle-.md)`
- `[SmallSecondaryButtonLabelStyle)](Variables/SmallSecondaryButtonLabelStyle-.md)`
- `[DefaultButtonLabelStyle),
  Sounds: @ButtonsCancel,](Variables/DefaultButtonLabelStyle-----Sounds---ButtonsCancel-.md)`

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

- `[SmallSecondaryButtonLabelStyle),
  Disabled: (Background: PatchStyle(TexturePath: "Common/Buttons/Disabled.png", Border: @ButtonBorder)](Variables/SmallSecondaryButtonLabelStyle-----Disabled---Background--PatchStyle-TexturePath---Common-Buttons-Disabled-png---Border---ButtonBorder-.md)`
- `[SecondaryButtonLabelStyle),
  Disabled: (Background: PatchStyle(TexturePath: "Common/Buttons/Disabled.png", Border: @ButtonBorder)](Variables/SecondaryButtonLabelStyle-----Disabled---Background--PatchStyle-TexturePath---Common-Buttons-Disabled-png---Border---ButtonBorder-.md)`

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

### Color
Example Values:

- `#b61a82`
- `#000000e0`
- `#24282b`
- `#993628`
- `#79bd5f`
- `#ffffff(0.8)`
- `#deaa52`
- `[OverlayColor](Variables/OverlayColor.md)`
- `#000000(0.82)`
- `#ffffff`
- `#5F6161`

### (TexturePath: "Common/Buttons/Destructive.png", Border: @ButtonBorderSize), LabelStyle
Example Values:

- `[PrimaryButtonLabelStyle),
  Hovered: (Background: PatchStyle(TexturePath: "Common/Buttons/Destructive_Hovered.png", Border: @ButtonBorderSize)](Variables/PrimaryButtonLabelStyle-----Hovered---Background--PatchStyle-TexturePath---Common-Buttons-Destructive_Hovered-png---Border---ButtonBorderSize-.md)`

### (TexturePath: "Common/Buttons/Destructive_Hovered.png", Border: @ButtonBorderSize), LabelStyle
Example Values:

- `[PrimaryButtonLabelStyle),
  Pressed: (Background: PatchStyle(TexturePath: "Common/Buttons/Destructive_Pressed.png", Border: @ButtonBorderSize)](Variables/PrimaryButtonLabelStyle-----Pressed---Background--PatchStyle-TexturePath---Common-Buttons-Destructive_Pressed-png---Border---ButtonBorderSize-.md)`

### (TexturePath: "Common/Buttons/Destructive_Pressed.png", Border: @ButtonBorderSize), LabelStyle
Example Values:

- `[PrimaryButtonLabelStyle),
  Disabled: (Background: PatchStyle(TexturePath: "Common/Buttons/Disabled.png", Border: @ButtonBorderSize)](Variables/PrimaryButtonLabelStyle-----Disabled---Background--PatchStyle-TexturePath---Common-Buttons-Disabled-png---Border---ButtonBorderSize-.md)`

### (TexturePath: "Common/Buttons/Disabled.png", Border: @ButtonBorderSize), LabelStyle
Example Values:

- `[PrimaryButtonLabelStyle),
  Sounds: @ButtonDestructiveSounds,](Variables/PrimaryButtonLabelStyle-----Sounds---ButtonDestructiveSounds-.md)`
- `[SecondaryButtonLabelStyle)](Variables/SecondaryButtonLabelStyle-.md)`
- `[SecondaryButtonDisabledLabelStyle)](Variables/SecondaryButtonDisabledLabelStyle-.md)`
- `[SmallSecondaryButtonDisabledLabelStyle)](Variables/SmallSecondaryButtonDisabledLabelStyle-.md)`

### (TexturePath: "Common/Buttons/Destructive.png", Border: @ButtonBorderSize)),  Hovered: (Background
Example Values:

- `PatchStyle(TexturePath: "Common/Buttons/Destructive_Hovered.png", Border: @ButtonBorderSize)),
  Pressed: (Background: PatchStyle(TexturePath: "Common/Buttons/Destructive_Pressed.png", Border: @ButtonBorderSize)),
  Disabled: (Background: PatchStyle(TexturePath: "Common/Buttons/Disabled.png", Border: @ButtonBorderSize)),
  Sounds: @ButtonSounds,`

### (TexturePath: "Common/Buttons/Destructive_Hovered.png", Border: @ButtonBorderSize)),  Pressed: (Background
Example Values:

- `PatchStyle(TexturePath: "Common/Buttons/Destructive_Pressed.png", Border: @ButtonBorderSize)),
  Disabled: (Background: PatchStyle(TexturePath: "Common/Buttons/Disabled.png", Border: @ButtonBorderSize)),
  Sounds: @ButtonSounds,`

### (TexturePath: "Common/Buttons/Destructive_Pressed.png", Border: @ButtonBorderSize)),  Disabled: (Background
Example Values:

- `PatchStyle(TexturePath: "Common/Buttons/Disabled.png", Border: @ButtonBorderSize)),
  Sounds: @ButtonSounds,`

### (TexturePath: "Common/Buttons/Disabled.png", Border: @ButtonBorderSize)),  Sounds: @ButtonSounds,
Example Values:

- ``

### (TexturePath: "Common/Buttons/Secondary.png", Border: @ButtonBorderSize)),  Hovered: (Background
Example Values:

- `PatchStyle(TexturePath: "Common/Buttons/Secondary_Hovered.png", Border: @ButtonBorderSize)),
  Pressed: (Background: PatchStyle(TexturePath: "Common/Buttons/Secondary_Pressed.png", Border: @ButtonBorderSize)),
  Disabled: (Background: PatchStyle(TexturePath: "Common/Buttons/Disabled.png", Border: @ButtonBorderSize)),
  Sounds: @ButtonSounds,`

### (TexturePath: "Common/Buttons/Secondary_Hovered.png", Border: @ButtonBorderSize)),  Pressed: (Background
Example Values:

- `PatchStyle(TexturePath: "Common/Buttons/Secondary_Pressed.png", Border: @ButtonBorderSize)),
  Disabled: (Background: PatchStyle(TexturePath: "Common/Buttons/Disabled.png", Border: @ButtonBorderSize)),
  Sounds: @ButtonSounds,`

### (TexturePath: "Common/Buttons/Secondary_Pressed.png", Border: @ButtonBorderSize)),  Disabled: (Background
Example Values:

- `PatchStyle(TexturePath: "Common/Buttons/Disabled.png", Border: @ButtonBorderSize)),
  Sounds: @ButtonSounds,`

### (TexturePath: "Common/Buttons/Secondary.png", Border: @ButtonBorderSize), LabelStyle
Example Values:

- `[SecondaryButtonLabelStyle),
  Hovered: (Background: PatchStyle(TexturePath: "Common/Buttons/Secondary_Hovered.png", Border: @ButtonBorderSize)](Variables/SecondaryButtonLabelStyle-----Hovered---Background--PatchStyle-TexturePath---Common-Buttons-Secondary_Hovered-png---Border---ButtonBorderSize-.md)`
- `[SmallSecondaryButtonLabelStyle),
  Hovered: (Background: PatchStyle(TexturePath: "Common/Buttons/Secondary_Hovered.png", Border: @ButtonBorderSize)](Variables/SmallSecondaryButtonLabelStyle-----Hovered---Background--PatchStyle-TexturePath---Common-Buttons-Secondary_Hovered-png---Border---ButtonBorderSize-.md)`

### (TexturePath: "Common/Buttons/Secondary_Hovered.png", Border: @ButtonBorderSize), LabelStyle
Example Values:

- `[SmallSecondaryButtonLabelStyle),
  Pressed: (Background: PatchStyle(TexturePath: "Common/Buttons/Secondary_Pressed.png", Border: @ButtonBorderSize)](Variables/SmallSecondaryButtonLabelStyle-----Pressed---Background--PatchStyle-TexturePath---Common-Buttons-Secondary_Pressed-png---Border---ButtonBorderSize-.md)`
- `[SecondaryButtonLabelStyle),
  Pressed: (Background: PatchStyle(TexturePath: "Common/Buttons/Secondary_Pressed.png", Border: @ButtonBorderSize)](Variables/SecondaryButtonLabelStyle-----Pressed---Background--PatchStyle-TexturePath---Common-Buttons-Secondary_Pressed-png---Border---ButtonBorderSize-.md)`

### (TexturePath: "Common/Buttons/Secondary_Pressed.png", Border: @ButtonBorderSize), LabelStyle
Example Values:

- `[SecondaryButtonLabelStyle),
  Disabled: (Background: PatchStyle(TexturePath: "Common/Buttons/Disabled.png", Border: @ButtonBorderSize)](Variables/SecondaryButtonLabelStyle-----Disabled---Background--PatchStyle-TexturePath---Common-Buttons-Disabled-png---Border---ButtonBorderSize-.md)`
- `[SmallSecondaryButtonLabelStyle),
  Disabled: (Background: PatchStyle(TexturePath: "Common/Buttons/Disabled.png", Border: @ButtonBorderSize)](Variables/SmallSecondaryButtonLabelStyle-----Disabled---Background--PatchStyle-TexturePath---Common-Buttons-Disabled-png---Border---ButtonBorderSize-.md)`

### (TexturePath: "Common/Buttons/Tertiary.png", Border: @ButtonBorderSize)),  Hovered: (Background
Example Values:

- `PatchStyle(TexturePath: "Common/Buttons/Tertiary_Hovered.png", Border: @ButtonBorderSize)),
  Pressed: (Background: PatchStyle(TexturePath: "Common/Buttons/Tertiary_Pressed.png", Border: @ButtonBorderSize)),
  Disabled: (Background: PatchStyle(TexturePath: "Common/Buttons/Disabled.png", Border: @ButtonBorderSize)),
  Sounds: @ButtonSounds,`

### (TexturePath: "Common/Buttons/Tertiary_Hovered.png", Border: @ButtonBorderSize)),  Pressed: (Background
Example Values:

- `PatchStyle(TexturePath: "Common/Buttons/Tertiary_Pressed.png", Border: @ButtonBorderSize)),
  Disabled: (Background: PatchStyle(TexturePath: "Common/Buttons/Disabled.png", Border: @ButtonBorderSize)),
  Sounds: @ButtonSounds,`

### (TexturePath: "Common/Buttons/Tertiary_Pressed.png", Border: @ButtonBorderSize)),  Disabled: (Background
Example Values:

- `PatchStyle(TexturePath: "Common/Buttons/Disabled.png", Border: @ButtonBorderSize)),
  Sounds: @ButtonSounds,`

### (TexturePath: "Common/Buttons/Tertiary.png", Border: @ButtonBorderSize), LabelStyle
Example Values:

- `[SecondaryButtonLabelStyle),
  Hovered: (Background: PatchStyle(TexturePath: "Common/Buttons/Tertiary_Hovered.png", Border: @ButtonBorderSize)](Variables/SecondaryButtonLabelStyle-----Hovered---Background--PatchStyle-TexturePath---Common-Buttons-Tertiary_Hovered-png---Border---ButtonBorderSize-.md)`

### (TexturePath: "Common/Buttons/Tertiary_Hovered.png", Border: @ButtonBorderSize), LabelStyle
Example Values:

- `[SecondaryButtonLabelStyle),
  Pressed: (Background: PatchStyle(TexturePath: "Common/Buttons/Tertiary_Pressed.png", Border: @ButtonBorderSize)](Variables/SecondaryButtonLabelStyle-----Pressed---Background--PatchStyle-TexturePath---Common-Buttons-Tertiary_Pressed-png---Border---ButtonBorderSize-.md)`

### (TexturePath: "Common/Buttons/Tertiary_Pressed.png", Border: @ButtonBorderSize), LabelStyle
Example Values:

- `[SecondaryButtonLabelStyle),
  Disabled: (Background: PatchStyle(TexturePath: "Common/Buttons/Disabled.png", Border: @ButtonBorderSize)](Variables/SecondaryButtonLabelStyle-----Disabled---Background--PatchStyle-TexturePath---Common-Buttons-Disabled-png---Border---ButtonBorderSize-.md)`

### (TexturePath: "ProcessingOnButton.png", Border: $Common.@ButtonBorderSize), LabelStyle
Example Values:

- `$Common.@SecondaryButtonLabelStyle),
  Hovered: (Background: PatchStyle(TexturePath: "ProcessingOnButtonHovered.png", Border: $Common.@ButtonBorderSize)`

### (TexturePath: "ProcessingOnButtonHovered.png", Border: $Common.@ButtonBorderSize), LabelStyle
Example Values:

- `$Common.@SecondaryButtonLabelStyle),
  Pressed: (Background: PatchStyle(TexturePath: "ProcessingOnButtonPressed.png", Border: $Common.@ButtonBorderSize)`

### (TexturePath: "ProcessingOnButtonPressed.png", Border: $Common.@ButtonBorderSize), LabelStyle
Example Values:

- `$Common.@SecondaryButtonLabelStyle)`

### (TexturePath: "../Common/Buttons/Secondary.png", Border: $Common.@ButtonBorderSize, Color: #ffffff(0.5))),      Hovered: (Background
Example Values:

- `PatchStyle(TexturePath: "../Common/Buttons/Secondary_Hovered.png", Border: $Common.@ButtonBorderSize, Color: #ffffff(0.6))),
      Pressed: (Background: PatchStyle(TexturePath: "../Common/Buttons/Secondary_Pressed.png", Border: $Common.@ButtonBorderSize, Color: #ffffff(0.7))),
      Disabled: (Background: PatchStyle(TexturePath: "../Common/Buttons/Disabled.png", Border: $Common.@ButtonBorderSize, Color: #ffffff(0.07))),
      Sounds: (
        ...$Sounds.@ButtonsLight
      )`

### (TexturePath: "../Common/Buttons/Secondary_Hovered.png", Border: $Common.@ButtonBorderSize, Color: #ffffff(0.6))),      Pressed: (Background
Example Values:

- `PatchStyle(TexturePath: "../Common/Buttons/Secondary_Pressed.png", Border: $Common.@ButtonBorderSize, Color: #ffffff(0.7))),
      Disabled: (Background: PatchStyle(TexturePath: "../Common/Buttons/Disabled.png", Border: $Common.@ButtonBorderSize, Color: #ffffff(0.07))),
      Sounds: (
        ...$Sounds.@ButtonsLight
      )`

### (TexturePath: "../Common/Buttons/Secondary_Pressed.png", Border: $Common.@ButtonBorderSize, Color: #ffffff(0.7))),      Disabled: (Background
Example Values:

- `PatchStyle(TexturePath: "../Common/Buttons/Disabled.png", Border: $Common.@ButtonBorderSize, Color: #ffffff(0.07))),
      Sounds: (
        ...$Sounds.@ButtonsLight
      )`

### (TexturePath: "../Common/Buttons/Disabled.png", Border: $Common.@ButtonBorderSize, Color: #ffffff(0.07))),      Sounds: (        ...$Sounds.@ButtonsLight      )
Example Values:

- ``

### (Color: #222222(0.3)), LabelStyle
Example Values:

- `[TagTextButtonLabelStyle),
  Hovered: (Background: PatchStyle(Color: #222222(0.5))](Variables/TagTextButtonLabelStyle-----Hovered---Background--PatchStyle-Color---222222-0-5--.md)`

### (Color: #222222(0.5)), LabelStyle
Example Values:

- `[TagTextButtonLabelStyle),
  Pressed: (Background: PatchStyle(Color: #222222(0.5))](Variables/TagTextButtonLabelStyle-----Pressed---Background--PatchStyle-Color---222222-0-5--.md)`
- `[TagTextButtonLabelStyle),
  Disabled: (Background: PatchStyle(Color: #222222(0.5))](Variables/TagTextButtonLabelStyle-----Disabled---Background--PatchStyle-Color---222222-0-5--.md)`
- `[TagTextButtonLabelStyle)](Variables/TagTextButtonLabelStyle-.md)`

