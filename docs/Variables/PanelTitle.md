[← Back](../Variables.md)

# PanelTitle ⚠️

⚠️ This variable has only been found in Client ui files, you may or may not be able to use it in mods.

**Defined at:** `Client/Data/Game/Interface/Common\Container.ui:194`

## Value

```ui
Group {
  @Alignment = Start;
  @Text = "";

  LayoutMode: Top;

  Label #PanelTitle {
    Style: (
      RenderBold: true,
      RenderUppercase: true,
      VerticalAlignment: Center,
      FontSize: 15,
      TextColor: #cfd6e0,
      FontName: "Secondary",
      HorizontalAlignment: @Alignment,
      LetterSpacing: 0
    );
    Anchor: (Height: 35, Horizontal: 8);
    Text: @Text;
  }

  Group {
    Background: #1b2533;
    Anchor: (Height: 1);
  }
}
```
