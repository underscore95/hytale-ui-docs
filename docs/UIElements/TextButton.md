[← Back](../UIElements.md)

# TextButton

This UI element has been found in Server ui files, you should be able to use it in mods.

**First used at:** `Common.ui:167`

## Fields

### Style
Example Values:

- `(...@TagTextButtonStyle,Sounds:(...$Sounds.@ButtonsLight,...@Sounds))`
- `(Default:(LabelStyle:(HorizontalAlignment:Center,VerticalAlignment:Center,RenderBold:true,FontSize:18)))`
- `(...@ServerBrowserTopTextButtonStyle,Sounds:(...$Sounds.@ButtonsLight,...@Sounds))`
- `[NavigationButtonStyle](Variables/NavigationButtonStyle.md)`
- `(...@DestructiveTextButtonStyle,Sounds:(...$Sounds.@ButtonsDestructive,...@Sounds))`
- `[TypeButtonStyle](Variables/TypeButtonStyle.md)`
- `(...@SecondaryButtonStyle,Sounds:(...$Sounds.@ButtonsMain,...@Sounds))`
- `(...@CancelTextButtonStyle,Sounds:(...$Sounds.@ButtonsCancel,...@Sounds))`
- `(...@SecondaryTextButtonStyle,Sounds:(...$Sounds.@ButtonsLight,...@Sounds))`
- `(...$Common.@DefaultTextButtonStyle,Sounds:(...$Common.@ButtonSounds,...$Sounds.@RespawnActivate))`
- `(...@ButtonStyle,Sounds:(...$Sounds.@ButtonsMain,...@Sounds))`
- `(Sounds:$Sounds.@ButtonsLight,Default:(LabelStyle:(...@CategoryButtonLabelStyle),Background:(TexturePath:"Tiles/TileDefault.png",Border:8),),Hovered:(LabelStyle:(...@CategoryButtonLabelStyle),Background:(TexturePath:"Tiles/TileHovered.png",Border:8),))`
- `(...@ButtonStyle,Sounds:(...$Sounds.@ButtonsLight,...@Sounds))`
- `(...@HeaderTextButtonStyle,Sounds:(Activate:(SoundPath:$Sounds.@Tick,Volume:6),MouseHover:(SoundPath:$Sounds.@ButtonsLightHover,Volume:6)))`
- `(Default:(LabelStyle:(VerticalAlignment:Center,FontSize:14)),Hovered:(LabelStyle:(VerticalAlignment:Center,FontSize:14),Background:#000000(0.15)),Pressed:(LabelStyle:(VerticalAlignment:Center,FontSize:14),Background:#000000(0.5)))`
- `(Default:(Background:(TexturePath:"../Dropdown.png",Border:$Common.@ButtonBorderSize),LabelStyle:$Common.@PrimaryButtonLabelStyle),Hovered:(Background:(TexturePath:"../DropdownHovered.png",Border:$Common.@ButtonBorderSize),LabelStyle:$Common.@PrimaryButtonLabelStyle),Pressed:(Background:(TexturePath:"../DropdownPressed.png",Border:$Common.@ButtonBorderSize),LabelStyle:$Common.@PrimaryButtonLabelStyle),Sounds:$Sounds.@ButtonsLight)`
- `[LabelStyle](Variables/LabelStyle.md)`
- `(Sounds:$Sounds.@ButtonsLight,Default:(LabelStyle:(Wrap:true,HorizontalAlignment:Center,VerticalAlignment:Center,),Background:(TexturePath:"Tiles/TileDefault.png",Border:8),),Hovered:(LabelStyle:(Wrap:true,HorizontalAlignment:Center,VerticalAlignment:Center,),Background:(TexturePath:"Tiles/TileHovered.png",Border:8),))`
- `(...@PrimaryTextButtonStyle,Sounds:(...$Sounds.@ButtonsLight,...@Sounds))`
- `(Default:(LabelStyle:@LabelStyle),Hovered:(LabelStyle:(...@LabelStyle,TextColor:#babec6)),Sounds:(Activate:(SoundPath:$Sounds.@Tick,Volume:6),MouseHover:(SoundPath:$Sounds.@ButtonsLightHover,Volume:6)))`
- `(...@SmallSecondaryTextButtonStyle,Sounds:(...$Sounds.@ButtonsLight,...@Sounds))`
- `$Common.@PrimaryTextButtonStyle`
- `(...@DefaultTextButtonStyle,Sounds:(...$Sounds.@ButtonsLight,...@Sounds))`
- `(Sounds:$Sounds.@ButtonsLight,Default:(LabelStyle:(Wrap:true,HorizontalAlignment:Center,VerticalAlignment:Center,),Background:(TexturePath:"Tiles/TileSelected.png",Border:8),))`
- `(...@TertiaryTextButtonStyle,Sounds:(...$Sounds.@ButtonsLight,...@Sounds))`
- `[HeaderTextButtonStyle](Variables/HeaderTextButtonStyle.md)`
- `[ButtonStyle](Variables/ButtonStyle.md)`

### Anchor
Example Values:

- `(Height:45)`
- `(Height:33)`
- `(Top:@SpacingTop,Bottom:10,Height:45)`
- `(Height:50)`
- `(...@Anchor,Height:@DefaultButtonHeight)`
- `(Height:32,Width:128,Top:@FuelSlotSize+15)`
- `(Width:220,Height:40,Left:36,Bottom:40)`
- `(...@Anchor,Height:@SmallButtonHeight)`
- `(Width:20)`
- `(Height:$Common.@PrimaryButtonHeight,Horizontal:8)`
- `(...@Anchor,Height:@PrimaryButtonHeight)`
- `(Width:32,Height:32,Left:30)`
- `(...@Anchor,Height:$Common.@PrimaryButtonHeight)`
- `(Top:10,Height:60)`
- `(Width:275,Left:8)`

### Padding
Example Values:

- `(Horizontal:10)`
- `(Horizontal:17,Right:15)`
- `(Horizontal:@DefaultButtonPadding)`
- `(Right:22,Left:15,Bottom:1)`
- `(Horizontal:12,Bottom:1)`
- `(Horizontal:$Common.@ButtonPadding)`
- `(Full:16)`
- `(Left:80,Bottom:10)`
- `(Full:6)`
- `[ButtonPadding](Variables/ButtonPadding.md)`
- `(Horizontal:16)`
- `(Bottom:10)`
- `(Horizontal:@ButtonPadding)`

### Text
Example Values:

- `""+%client.mainMenu.navigation.worlds+""`
- `""+%client.mainMenu.servers.groups.lan+""`
- `""+%client.mainMenu.navigation.settings+""`
- `"Craft"`
- `%server.customUI.respawnPage.respawn`
- `""+%client.mainMenu.servers.groups.favorite+""`
- `"x"`
- `%client.devTools.options`
- `%client.feedback.type.feedback`
- `""+%client.mainMenu.navigation.minigames+""`
- `"<"`
- `""+%client.mainMenu.navigation.avatar+""`
- `""+%client.mainMenu.navigation.shop+""`
- `">"`
- `""+%client.mainMenu.navigation.servers+""`
- `%client.feedback.type.bugreport`
- `[Text](Variables/Text.md)`

### FlexWeight
Example Values:

- `1`

### Visible
Example Values:

- `false`

### TextTooltipStyle
Example Values:

- `$C.@DefaultTextTooltipStyle`

### Disabled
Example Values:

- `true`

### //thespacefixesanartifactwithlabelmasksStyle
Example Values:

- `[NavigationButtonStyle](Variables/NavigationButtonStyle.md)`

### //thespacefixesanartifactwithlabelmasksAnchor
Example Values:

- `[ButtonSpacing](Variables/ButtonSpacing.md)`
- `(...@ButtonSpacing,Right:45)`
- `(...@ButtonSpacing,Left:0)`

### Background
Example Values:

- `(Color:#666666(0.4))`

