# HeaderSearch

**Defined at:** `Common.ui:662`

## Value

```ui
Group {
  @MarginRight = 10;

  Anchor: (Width: 200, Right: 0);

  CompactTextField #SearchInput {
    Anchor: (Height: 30, Right: @MarginRight);
    CollapsedWidth: 34;
    ExpandedWidth: 200;
    PlaceholderText: %server.customUI.searchPlaceholder;
    Style: (FontSize: 16);
    PlaceholderStyle: (TextColor: #3d5a85, RenderUppercase: true, FontSize: 14);
    Padding: (Horizontal: 12, Left: 34);
    Decoration: (
      Default: (
        Icon: (Texture: "Common/SearchIcon.png", Width: 16, Height: 16, Offset: 9),
        ClearButtonStyle: @ClearButtonStyle
      )
    );
  }
}
```
