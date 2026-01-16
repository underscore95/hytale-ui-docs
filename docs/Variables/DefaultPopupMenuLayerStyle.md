[← Back](../Variables.md)

# DefaultPopupMenuLayerStyle ⚠️

⚠️ This variable has only been found in Client ui files, you may or may not be able to use it in mods.

**Defined at:** `Client/Data/Game/Interface/Common.ui:410`

## Value

```ui
PopupMenuLayerStyle(
  Background: (TexturePath: "Common/Popup.png", Border: 16),
  Padding: 2,
  BaseHeight: 5,
  MaxWidth: 200,
  TitleStyle: (RenderBold: true, RenderUppercase: true, FontSize: 13, TextColor: #ccb588),
  TitleBackground: (TexturePath: "Common/PopupTitle.png"),
  RowHeight: 25,
  ItemLabelStyle: (RenderBold: true, RenderUppercase: true, FontSize: 11, TextColor: #96a9be(0.8)),
  ItemPadding: (Vertical: 5, Horizontal: 8),
  ItemBackground: (TexturePath: "Common/PopupItem.png"),
  ItemIconSize: 16,
  HoveredItemBackground: (TexturePath: "Common/HoveredPopupItem.png"),
  PressedItemBackground: (TexturePath: "Common/PressedPopupItem.png"),
  ItemSounds: $Sounds.@ButtonsLight
)
```
