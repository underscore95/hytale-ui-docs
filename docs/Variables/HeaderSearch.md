[← Back](../Variables.md)

# HeaderSearch ⚠️

⚠️ This variable has only been found in Client ui files, you may or may not be able to use it in mods.

**Defined at:** `Client/Data/Game/Interface/Common\Container.ui:130`

## Value

```ui
Group {
  @MarginRight = 10;

  Anchor: (Width: 200);

  CompactTextField #SearchField {
    Anchor: (Height: 30, Right: @MarginRight);
    CollapsedWidth: 34;
    ExpandedWidth: 200;
    PlaceholderText: %client.general.searchField.placeholder;
    Style: (FontSize: 16);
    PlaceholderStyle: (TextColor: #3d5a85, RenderUppercase: true, FontSize: 14);
    Padding: (Horizontal: 12, Left: 34);
    Decoration: (
      Default: (
        Icon: (Texture: "SearchIcon.png", Width: 16, Height: 16, Offset: 9),
        ClearButtonStyle: @ClearButtonStyle
      )
    );
    ExpandSound: (SoundPath: "../Sounds/SearchFieldExpand.ogg", Volume: 6);
    CollapseSound: (
      SoundPath: "../Sounds/SearchFieldCollapse.ogg",
      Volume: 5
    );
  }
}
```
