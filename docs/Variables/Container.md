# Container

**Defined at:** `Common.ui:750`

## Value

```ui
Group {
  @ContentPadding = Padding(Full: @FullPaddingValue);
  @CloseButton = false;

  Group #Title {
    Anchor: (Height: @TitleHeight, Top: 0);
    Padding: (Top: 7);
    Background: (TexturePath: "Common/ContainerHeaderNoRunes.png", HorizontalBorder: 35, VerticalBorder: 0);
  }

  Group #Content {
    LayoutMode: Top;
    Padding: @ContentPadding;
    Anchor: (Top: @TitleHeight);
    Background: (TexturePath: "Common/ContainerPatch.png", Border: 23);
  }

  Button #CloseButton {
    Anchor: (Width: 32, Height: 32, Top: -8, Right: -8);
    Style: (
      Default: (Background: "Common/ContainerCloseButton.png"),
      Hovered: (Background: "Common/ContainerCloseButtonHovered.png"),
      Pressed: (Background: "Common/ContainerCloseButtonPressed.png"),
      Sounds: @ButtonsCancel
    );
    Visible: @CloseButton;
  }
}
```
