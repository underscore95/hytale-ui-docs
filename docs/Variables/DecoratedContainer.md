[← Back](../Variables.md)

# DecoratedContainer

**Defined at:** `Common.ui:779`

## Value

```ui
Group {
  @ContentPadding = Padding(Full: 9 + 8);
  @CloseButton = false;

  Group #Title {
    Anchor: (Height: @TitleHeight, Top: 0);
    Background: (TexturePath: "Common/ContainerHeader.png", HorizontalBorder: 50, VerticalBorder: 0);
    Padding: (Top: 7);

    Group #ContainerDecorationTop {
      Anchor: (Width: 236, Height: 11, Top: -12);
      Background: "Common/ContainerDecorationTop.png";
    }
  }

  Group #Content {
    LayoutMode: Top;
    Anchor: (Top: @TitleHeight);
    Padding: @ContentPadding;
    Background: (TexturePath: "Common/ContainerPatch.png", Border: 23);
  }

  Group #ContainerDecorationBottom {
    Anchor: (Width: 236, Height: 11, Bottom: -6);
    Background: "Common/ContainerDecorationBottom.png";
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
