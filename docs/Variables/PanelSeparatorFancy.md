[← Back](../Variables.md)

# PanelSeparatorFancy ⚠️

⚠️ This variable has only been found in Client ui files, you may or may not be able to use it in mods.

**Defined at:** `Client/Data/Game/Interface/Common\Container.ui:226`

## Value

```ui
Group {
  @Anchor = ();

  LayoutMode: Left;
  Anchor: (...@Anchor, Height: 8);

  Group {
    FlexWeight: 1;
    Background: "ContainerPanelSeparatorFancyLine.png";
  }

  Group {
    Anchor: (Width: 11);
    Background: "ContainerPanelSeparatorFancyDecoration.png";
  }

  Group {
    FlexWeight: 1;
    Background: "ContainerPanelSeparatorFancyLine.png";
  }
}
```
