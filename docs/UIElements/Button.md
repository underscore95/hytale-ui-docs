[← Back](../UIElements.md)

# Button

This UI element has been found in Server ui files, you should be able to use it in mods.

**First used at:** `Common.ui:182`

## Fields

### Style
Example Values:

- `(...$Common.@PrimaryButtonStyle,Sounds:$Sounds.@ButtonsLight)`
- `(...@CancelButtonStyle,Sounds:(...$Sounds.@ButtonsLight,...@Sounds))`
- `[RightSideButtonDefaultStyle](Variables/RightSideButtonDefaultStyle.md)`
- `(...@SecondaryButtonStyle,Sounds:(...$Sounds.@ButtonsLight,...@Sounds))`
- `(Default:(Background:"ContainerCloseButton.png"),Hovered:(Background:"ContainerCloseButtonHovered.png"),Pressed:(Background:"ContainerCloseButtonPressed.png"),Sounds:$Sounds.@ButtonsDestructive)`
- `(Sounds:$Sounds.@ButtonsSmall)`
- `ButtonStyle(Default:(Background:(Color:#00000000)),Hovered:(Background:(Color:#ffffff10)),Pressed:(Background:(Color:#ffffff08)),Sounds:(Activate:(SoundPath:$Sounds.@Tick,Volume:6)))`
- `(Hovered:(Background:#000000(0.2),))`
- `(Default:(Background:"Common/ContainerCloseButton.png"),Hovered:(Background:"Common/ContainerCloseButtonHovered.png"),Pressed:(Background:"Common/ContainerCloseButtonPressed.png"),Sounds:@ButtonsCancel)`
- `(Default:(Background:(TexturePath:"../../Common/BugReportIcon.png")),Hovered:(Background:(TexturePath:"../../Common/BugReportIcon.png",Color:#ffffff(0.8))),Pressed:(Background:(TexturePath:"../../Common/BugReportIcon.png",Color:#ffffff(0.6))),Sounds:(...$Sounds.@ButtonsLight))`
- `[DefaultStyle](Variables/DefaultStyle.md)`
- `(Default:(Background:"WorldTileOverlay.png"),Hovered:(Background:"WorldTileOverlayHovered.png"),Pressed:(Background:(TexturePath:"WorldTileOverlayHovered.png",Color:#ffffff(0.9))),Sounds:$Sounds.@EnterWorld)`
- `[Style](Variables/Style.md)`
- `(Default:(Background:PatchStyle(TexturePath:"../Common/Buttons/Secondary.png",Border:$Common.@ButtonBorderSize,Color:#ffffff(0.5))),Hovered:(Background:PatchStyle(TexturePath:"../Common/Buttons/Secondary_Hovered.png",Border:$Common.@ButtonBorderSize,Color:#ffffff(0.6))),Pressed:(Background:PatchStyle(TexturePath:"../Common/Buttons/Secondary_Pressed.png",Border:$Common.@ButtonBorderSize,Color:#ffffff(0.7))),Disabled:(Background:PatchStyle(TexturePath:"../Common/Buttons/Disabled.png",Border:$Common.@ButtonBorderSize,Color:#ffffff(0.07))),Sounds:(...$Sounds.@ButtonsLight))`
- `(...@PrimarySquareButtonStyle,Sounds:(...$Sounds.@ButtonsLight,...@Sounds))`
- `(...@DestructiveButtonStyle,Sounds:(...$Sounds.@ButtonsLight,...@Sounds))`
- `[RandomizationUnlockedButtonStyle](Variables/RandomizationUnlockedButtonStyle.md)`
- `(Default:(Background:"BlockSelectorIconClear.png"),Hovered:(Background:"BlockSelectorIconClearHovered.png"))`
- `(Default:(Background:"Logo.png"),Hovered:(Background:"LogoHovered.png"),Pressed:(Background:"LogoPressed.png"),Sounds:(MouseHover:(SoundPath:$Sounds.@HButtonHover,Volume:6)))`
- `(Default:(Background:"RecipesIcon.png"),Hovered:(Background:(TexturePath:"RecipesIcon.png",Color:#ffffff(0.8))),Pressed:(Background:(TexturePath:"RecipesIcon.png",Color:#ffffff(0.6))),)`
- `(Default:(Background:(TexturePath:"../Dropdown.png",Border:$Common.@ButtonBorderSize)),Hovered:(Background:(TexturePath:"../DropdownHovered.png",Border:$Common.@ButtonBorderSize)),Pressed:(Background:(TexturePath:"../DropdownPressed.png",Border:$Common.@ButtonBorderSize)),Sounds:$Sounds.@ButtonsLight)`
- `(Default:(Background:(Color:$MyAvatarPage.@PartPreviewBackgroundColor)),Hovered:(Background:(Color:$MyAvatarPage.@PartPreviewBackgroundColorHovered)),Sounds:(Activate:(SoundPath:$Sounds.@Untick,Volume:6),MouseHover:(SoundPath:$Sounds.@ButtonsLightHover,Volume:6)))`
- `(Default:(Background:"Common/ContainerCloseButton.png"),Hovered:(Background:"Common/ContainerCloseButtonHovered.png"),Pressed:(Background:"Common/ContainerCloseButtonPressed.png"),)`
- `[BodyTypeButtonStyle](Variables/BodyTypeButtonStyle.md)`
- `(...@TertiaryButtonStyle,Sounds:(...$Sounds.@ButtonsLight,...@Sounds))`
- `(Hovered:(Background:#ffffff(0.05)))`
- `(Sounds:($Sounds.@Shuffle))`
- `(Default:(Background:"../IconMaskClear.png"),Hovered:(Background:"../IconMaskClearHovered.png"))`
- `(Default:(Background:#ffffff(0)),Hovered:(Background:(TexturePath:"GoldenBorder_Hover.png",Border:7)))`
- `(...@DefaultSquareButtonStyle,Sounds:(...$Sounds.@ButtonsLight,...@Sounds))`
- `(...$Common.@SecondaryButtonStyle,Sounds:$Sounds.@ButtonsLight)`
- `[MatchHairColorsOnButtonStyle](Variables/MatchHairColorsOnButtonStyle.md)`
- `[ButtonStyle](Variables/ButtonStyle.md)`

### Anchor
Example Values:

- `(Width:@ActionButtonWidth,Right:4)`
- `(Width:24,Height:24)`
- `(Width:38,Height:38,Bottom:7)`
- `(Width:38,Height:38,Top:7)`
- `(Height:50,Right:20)`
- `(Height:@ButtonHeight,Bottom:@ButtonSpacing)`
- `(Height:50)`
- `(Width:24,Height:24,Top:0,Right:0)`
- `(Top:7,Height:6)`
- `(Width:@ActionButtonWidth,Right:7)`
- `(...@Anchor,Height:@PrimaryButtonHeight,Width:@PrimaryButtonHeight)`
- `(Bottom:10)`
- `(...@Anchor,Height:@PrimaryButtonHeight,Width:@Width)`
- `(Width:34,Right:10)`
- `(Width:25,Height:25,Bottom:8)`
- `(Top:8,Height:64)`
- `(Width:48,Height:48,Top:7)`
- `(Height:44)`
- `(Width:45,Left:8)`
- `(...@Anchor,Height:@DefaultButtonHeight,Width:@DefaultButtonHeight)`
- `(Width:48,Right:4)`
- `(Width:@ActionButtonWidth)`
- `(Height:28)`
- `(Width:431,Height:485)`
- `(Width:48,Height:48,Bottom:7)`
- `(Width:$MinigamesPage.@FrameWidth,Height:$MinigamesPage.@FrameHeight,Top:0,Left:0)`
- `(Width:140,Height:140)`
- `(Top:-16,Right:-16,Width:32,Height:32)`
- `(Width:32,Height:32,Top:-8,Right:-8)`
- `(Width:@TileWidth,Height:@TileHeight)`
- `(Height:32)`
- `(Width:24,Height:24,Left:10)`
- `(Left:35,Top:4,Width:60,Height:86,Right:5)`
- `(Left:10,Right:10)`
- `Anchor(Width:66,Height:50)`
- `(Width:@ButtonWidth,Height:$Common.@PrimaryButtonHeight)`
- `(Width:30,Height:30,Bottom:8)`
- `(Height:50,Bottom:4)`
- `(...@Anchor,Height:@DefaultButtonHeight,Width:@Width)`
- `(Height:$Common.@PrimaryButtonHeight,MinWidth:75)`

### Padding
Example Values:

- `10`
- `(Horizontal:@DefaultButtonPadding)`
- `(Horizontal:9)`
- `(Full:6)`
- `(Left:20,Right:20,Top:17,Bottom:20)`
- `(Right:25,Left:25)`
- `(Horizontal:@ButtonPadding)`

### Visible
Example Values:

- `[CloseButton](Variables/CloseButton.md)`
- `false`

### LayoutMode
Example Values:

- `Middle`
- `Left`
- `Center`

### FlexWeight
Example Values:

- `1`

### TooltipText
Example Values:

- `%client.inventory.character.tooltip.lockedMemories`
- `%client.inventory.chest.tooltip.takeAll`
- `%client.inventory.button.autoSort.tooltip`
- `%client.myAvatar.synchronizeHairColor.disable`
- `%client.inventory.character.tooltip.togglePocketCrafting`
- `%client.inventory.recipesButton`
- `%client.inventory.character.tooltip.pocketCraftingDisabled`
- `%client.inventory.chest.tooltip.putAll`
- `%client.inventory.chest.tooltip.quickStack`
- `%client.inventory.character.tooltip.toggleMemories`
- `%client.myAvatar.lockProperty`
- `%client.builderTools.panel.clearSelection`
- `%client.inventory.character.tooltip.toggleBackpack`
- `%client.bugReportButton.tooltip`
- `"Removematerial"`
- `%client.mainMenu.discord.button.tooltip`
- `%client.inventory.character.tooltip.lockedBackpack`

### TextTooltipStyle
Example Values:

- `(...$Common.@ButtonTextTooltipStyle,Alignment:TopLeft)`
- `$Common.@ButtonTextTooltipStyle`

### Background
Example Values:

- `#ffffff(0.08)`
- `"InfoIcon.png"`
- `"StopButton.png"`
- `[PlayButtonBackground](Variables/PlayButtonBackground.md)`

### MaskTexturePath
Example Values:

- `"PartMask.png"`

