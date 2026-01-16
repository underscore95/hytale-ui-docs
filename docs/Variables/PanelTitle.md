[← Back](../Variables.md)

# PanelTitle

**Defined at:** `Common.ui:702`

## Value

```ui
Group {
  @Alignment = Start;
  @Text = "";

  LayoutMode: Top;

  Label #PanelTitle {
    Style: (RenderBold: true, VerticalAlignment: Center, FontSize: 15, TextColor: #afc2c3, HorizontalAlignment: @Alignment);
    Anchor: (Height: 35, Horizontal: 8);
    Text: @Text;
  }

  Group {
    Background: #393426(0.5);
    Anchor: (Height: 1);
  }
}
```
