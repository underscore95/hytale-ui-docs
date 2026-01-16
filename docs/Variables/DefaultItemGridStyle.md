[← Back](../Variables.md)

# DefaultItemGridStyle ⚠️

⚠️ This variable has only been found in Client ui files, you may or may not be able to use it in mods.

**Defined at:** `Client/Data/Game/Interface/InGame\Common.ui:10`

## Value

```ui
ItemGridStyle(
  SlotSpacing: @DefaultItemSlotSpacing,
  SlotSize: @DefaultItemSlotSize,
  SlotIconSize: 64,
  SlotBackground: "Pages/Inventory/Slot.png",
  QuantityPopupSlotOverlay: "Pages/Inventory/QuantityPopupSlotOverlay.png",
  BrokenSlotBackgroundOverlay: "Pages/Inventory/SlotItemBrokenCracksOverlay.png",
  BrokenSlotIconOverlay: "Pages/Inventory/SlotItemBrokenIconOverlay.png",
  DefaultItemIcon: "Pages/Inventory/UnknownItemIcon.png",
  DurabilityBar: "Pages/Inventory/DurabilityBar.png",
  DurabilityBarBackground: "Pages/Inventory/DurabilityBarBackground.png",
  DurabilityBarAnchor: (
    Bottom: 10,
    Left: 13,
    Width: 48,
    Height: 2
  ),
  DurabilityBarColorStart: #a63232,
  DurabilityBarColorEnd: #63b649,
  CursedIconPatch: "Pages/Inventory/CursedSpiral.png",
  CursedIconAnchor: (
    Bottom: 67,
    Left: 46,
    Width: 21,
    Height: 21
  ),
  ItemStackHoveredSound: (
    SoundPath: $Sounds.@ButtonsLightHover,
    Volume: 6
  )
)
```
