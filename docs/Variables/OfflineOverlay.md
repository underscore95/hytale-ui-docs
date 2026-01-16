[← Back](../Variables.md)

# OfflineOverlay ⚠️

⚠️ This variable has only been found in Client ui files, you may or may not be able to use it in mods.

**Defined at:** `Client/Data/Game/Interface/MainMenu\Common.ui:43`

## Value

```ui
Group {
  Visible: false;
  HitTestVisible: true;
  Background: #0a0c10(0.92);
  LayoutMode: Middle;

  Group {
    LayoutMode: Top;
    Anchor: (Width: @Width);

    Label {
      Text: @Title;
      Style: (
        HorizontalAlignment: Center,
        TextColor: #d3dee3,
        FontSize: 32,
        RenderBold: true,
        RenderUppercase: true
      );
    }

    Label #DescriptionLabel {
      Anchor: (Top: 20);
      Text: @Description;
      Style: (
        HorizontalAlignment: Center,
        TextColor: #6c7886,
        FontSize: 18,
        Wrap: true
      );
    }
  }
}
```
