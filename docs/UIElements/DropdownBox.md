[← Back](../UIElements.md)

# DropdownBox

This UI element has been found in Server ui files, you should be able to use it in mods.

**First used at:** `Common.ui:479`

## Fields

### Anchor
Example Values:

- `(Right:0,Left:4,Top:0,Height:41,Width:194)`
- `(Width:330,Left:8)`
- `(Width:180,Height:32)`
- `(Right:0,Left:4,Top:0,Height:42,Width:194)`
- `(Left:30,Right:15,Top:0,Height:32,Width:160)`
- `(Width:26,Height:34,Right:4)`
- `(Height:32,Width:55,Left:7)`
- `(Right:0,Width:100,Height:28)`
- `(...@Anchor,Width:330,Height:@DropdownBoxHeight)`
- `(Width:250,Top:10,Height:32,Left:0)`

### Style
Example Values:

- `(...$Common.@TitledDropdownBoxStyle,DefaultBackground:(Color:#00000000),HoveredBackground:(Color:#00000000),PressedBackground:(Color:#00000000),EntryHeight:29,EntryIconWidth:13,EntryIconHeight:10,SelectedEntryIconBackground:(TexturePath:"../../../Common/CheckmarkSmallPositive.png"),SelectedEntryLabelStyle:(TextColor:#b7cedd,RenderUppercase:true,RenderBold:true,VerticalAlignment:Center,FontSize:13),PanelWidth:200,PanelScrollbarStyle:(Spacing:0,Size:0),HorizontalPadding:8,Sounds:$Sounds.@DropdownBox,EntrySounds:(Activate:(SoundPath:$Sounds.@Tick,Volume:6)))`
- `DropdownBoxStyle(...$Common.@DefaultDropdownBoxStyle,LabelStyle:(...$Common.@DefaultDropdownBoxLabelStyle,FontSize:15,RenderBold:true),PanelAlign:Bottom,PanelWidth:200)`
- `[DefaultDropdownBoxStyle](Variables/DefaultDropdownBoxStyle.md)`
- `(...$Common.@TitledDropdownBoxStyle,IconTexturePath:"TagsIcon.png",IconWidth:15,IconHeight:17,EntryHeight:29,EntryIconWidth:13,EntryIconHeight:10,SelectedEntryIconBackground:(TexturePath:"../../Common/CheckmarkSmallPositive.png"),SelectedEntryLabelStyle:(TextColor:#b7cedd,RenderUppercase:true,RenderBold:true,VerticalAlignment:Center,FontSize:13),PanelWidth:200,PanelScrollbarStyle:(Spacing:0,Size:0),HorizontalPadding:8,Sounds:$Sounds.@DropdownBox)`
- `$Common.@DefaultDropdownBoxStyle`
- `DropdownBoxStyle(...$Common.@DefaultDropdownBoxStyle,LabelStyle:(...$Common.@DefaultDropdownBoxLabelStyle,FontSize:12,RenderBold:true),PanelWidth:100)`
- `(...$Common.@DefaultDropdownBoxStyle,HorizontalPadding:12,LabelStyle:(...$Common.@DefaultDropdownBoxLabelStyle,FontSize:16,RenderBold:true,))`

### PanelTitleText
Example Values:

- `%client.myAvatar.dropdown.filterBy`
- `%client.inventory.dropdown.autoSortBy`

### MaxSelection
Example Values:

- `1`
- `0`

### ShowLabel
Example Values:

- `false`

