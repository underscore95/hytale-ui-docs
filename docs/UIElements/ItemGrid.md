[← Back](../UIElements.md)

# ItemGrid

This UI element has been found in Server ui files, you should be able to use it in mods.

**First used at:** `Pages\EntitySpawnPage.ui:86`

## Fields

### Anchor
Example Values:

- `(Height:@FuelSlotSize,Top:0)`
- `(Width:$InGame.@DefaultItemSlotSize+4,Height:@ItemGridHeight,Left:0,Top:@ItemGridY)`
- `(Width:($InGame.@DefaultItemSlotSize*9)+($InGame.@DefaultItemSlotSpacing*8)+($InGame.@DefaultItemGridPadding))`
- `(Width:@MaterialSlotSize,Height:@MaterialSlotSize,Horizontal:0,Vertical:0)`
- `(Width:@ItemGridSpecialSlotWidth,Height:@ItemGridSpecialSlotHeight,Left:@ItemGridSpecialSlotLeftPos,Bottom:0)`
- `(Width:$InGame.@DefaultItemSlotSize*3+$InGame.@DefaultItemSlotSpacing*2+$InGame.@PanelPadding,Right:$Container.@InnerPaddingValue,Height:350)`

### SlotsPerRow
Example Values:

- `$InGame.@DefaultItemSlotsPerRow`
- `10`
- `3`
- `1`
- `8`
- `2`

### Style
Example Values:

- `$InGame.@DefaultItemGridStyle`
- `(SlotSize:64,SlotSpacing:0,SlotIconSize:64)`
- `(...$InGame.@DefaultItemGridStyle,SlotSpacing:18,SlotBackground:@SlotPatch)`
- `(...$InGame.@DefaultItemGridStyle,SlotSize:@FuelSlotSize,SlotSpacing:0,SlotIconSize:@FuelSlotIconSize,SlotBackground:"ProcessingFuelSlot.png")`
- `(...$InGame.@DefaultItemGridStyle,SlotSpacing:@HotbarSlotSpacingHud)`
- `(SlotSize:@MaterialSlotSize,SlotIconSize:@MaterialSlotSize,SlotSpacing:0,SlotBackground:"../Common/BlockSelectorSlotBackground.png")`
- `[ItemGridStyle](Variables/ItemGridStyle.md)`
- `[SpecialItemGridStyle](Variables/SpecialItemGridStyle.md)`

### RenderItemQualityBackground
Example Values:

- `true`
- `false`

### AreItemsDraggable
Example Values:

- `false`

### Background
Example Values:

- `(Color:$InGame.@DefaultItemGridBackground,Anchor:(Right:8))`
- `#000000(0)`
- `$InGame.@DefaultItemGridBackground`

### Padding
Example Values:

- `(Left:$InGame.@DefaultItemGridPadding,Top:$InGame.@DefaultItemGridPadding,Right:0,Bottom:$InGame.@DefaultItemGridPadding)`
- `$InGame.@DefaultItemGridPadding`
- `(Left:5)`

### //Anchor
Example Values:

- `(Top:10,Height:46)`

### //Style
Example Values:

- `(//...$InGame.@DefaultItemGridStyle,//SlotSize:46,//SlotIconSize:44,//SlotBackground:"../../Pages/Inventory/BuilderTools/Input/BlockSelectorSlotBackground.png",//)`

### //RenderItemQualityBackground
Example Values:

- `false`

### //AreItemsDraggable
Example Values:

- `false`

### //SlotsPerRow
Example Values:

- `1`

### ScrollbarStyle
Example Values:

- `$Common.@DefaultScrollbarStyle`
- `$Common.@TranslucentScrollbarStyle`

### ShowScrollbar
Example Values:

- `true`

### KeepScrollPosition
Example Values:

- `true`

### InfoDisplay
Example Values:

- `None`

