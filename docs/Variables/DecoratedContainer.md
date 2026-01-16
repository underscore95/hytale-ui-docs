[← Back](../Variables.md)

# DecoratedContainer ⚠️

⚠️ This variable has only been found in Client ui files, you may or may not be able to use it in mods.

**Defined at:** `Client/Data/Game/Interface/Common\Container.ui:270`

## Value

```ui
Group {
  @ContentPadding = Padding(Full: 9 + 8);
  @CloseButton = false;

  Group #Title {
    Anchor: (Height: @TitleHeight, Top: 0);
    Background: (TexturePath: "ContainerHeader.png", HorizontalBorder: 50, VerticalBorder: 0);
    Padding: (Top: 7);

    Group #ContainerDecorationTop {
      Anchor: (Width: 236, Height: 11, Top: -12);
      Background: "ContainerDecorationTop.png";
    }
  }

  Group #Content {
    LayoutMode: Top;
    Anchor: (Top: @TitleHeight);
    Padding: @ContentPadding;
    Background: (TexturePath: "ContainerPatch.png", Border: 23);
  }

  Group #ContainerDecorationBottom {
    Anchor: (Width: 236, Height: 11, Bottom: -6);
    Background: "ContainerDecorationBottom.png";
  }

  Button #CloseButton {
    Anchor: (Width: 32, Height: 32, Top: -8, Right: -8);
    Style: (
      Default: (Background: "ContainerCloseButton.png"),
      Hovered: (Background: "ContainerCloseButtonHovered.png"),
      Pressed: (Background: "ContainerCloseButtonPressed.png"),
      Sounds: $Sounds.@ButtonsDestructive
    );
    Visible: @CloseButton;
  }
}
```
