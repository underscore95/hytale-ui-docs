[← Back](../Variables.md)

# Container ⚠️

⚠️ This variable has only been found in Client ui files, you may or may not be able to use it in mods.

**Defined at:** `Client/Data/Game/Interface/InGame\Hud\Abilities\InputBinding.ui:4`

## Value

```ui
Group {
  @LabelPosition = -40;
  @MouseIconPosition = -40;

  Group #MouseLeft {
    LayoutMode: Middle;
    Anchor: (Width: @IconSize, Height: @IconSize, Bottom: @MouseIconPosition);
    Background: "Assets/Icons/IconLeftClick.png";
    Visible: false;
  }

  Group #MouseRight {
    LayoutMode: Middle;
    Anchor: (Width: @IconSize, Height: @IconSize, Bottom: @MouseIconPosition);
    Background: "Assets/Icons/IconRightClick.png";
    Visible: false;
  }

  Group #MouseMiddle {
    LayoutMode: Middle;
    Anchor: (Width: @IconSize, Height: @IconSize, Bottom: @MouseIconPosition);
    Background: "Assets/Icons/IconMiddleClick.png";
    Visible: false;
  }

  Group {
    Anchor: (Height: @IconSize, Bottom: @LabelPosition);
    LayoutMode: Center;

    Label #InputBinding {
      Background: (TexturePath: "../../Pages/Inventory/SlotInputBindingBackground.png", Border: 6);
      Anchor: (MinWidth: 32);
      Padding: (Top: 1, Horizontal: 4);
      Style: (RenderBold: true, Alignment: Center, TextColor: #ffffe6, FontName: "Secondary", FontSize: 12, Wrap: true);
      Visible: false;
    }
  }
}
```
