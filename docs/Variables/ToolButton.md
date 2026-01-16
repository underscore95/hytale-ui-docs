[← Back](../Variables.md)

# ToolButton ⚠️

⚠️ This variable has only been found in Client ui files, you may or may not be able to use it in mods.

**Defined at:** `Client/Data/Game/Interface/InGame\ContentCreationNavigation.ui:4`

## Value

```ui
MenuItem {
  Padding: (Horizontal: 30);
  TextTooltipStyle: $Common.@ButtonTextTooltipStyle;
  PopupStyle: (
    Background: #121a26,
    ButtonPadding: (Left: 30, Top: 7, Bottom: 7, Right: 20),
    Padding: (Bottom: 10),
    TooltipStyle: $Common.@ButtonTextTooltipStyle,
    ButtonStyle: (
      Default: (
        LabelStyle: (FontSize: 13, TextColor: #7c8b99),
        BindingLabelStyle: (FontSize: 13, TextColor: #ffffff(0.2))
      ),
      Hovered: (
        Background: #000000(0.2),
        LabelStyle: (FontSize: 13, TextColor: #7c8b99),
        BindingLabelStyle: (FontSize: 13, TextColor: #ffffff(0.2))
      )
    ),
    SelectedButtonStyle: (
      Default: (
        LabelStyle: (FontSize: 13, TextColor: #ffffff, RenderBold: true),
        BindingLabelStyle: (FontSize: 13, TextColor: #ffffff(0.2))
      ),
      Hovered: (
        Background: #000000(0.2),
        LabelStyle: (FontSize: 13, TextColor: #ffffff, RenderBold: true),
        BindingLabelStyle: (FontSize: 13, TextColor: #ffffff(0.2))
      )
    )
  );
  Style: (
    Default: (
      LabelStyle: (FontSize: 15, TextColor: #7c8b99, VerticalAlignment: Center, RenderUppercase: true, RenderBold: true)
    ),
    Hovered: (
      Background: #121a26,
      LabelStyle: (FontSize: 15, TextColor: #7c8b99, VerticalAlignment: Center, RenderUppercase: true, RenderBold: true)
    )
  );
  SelectedStyle: (
    Default: (
      LabelStyle: (FontSize: 15, TextColor: #ffffff, VerticalAlignment: Center, RenderUppercase: true, RenderBold: true)
    ),
    Hovered: (
      Background: #121a26,
      LabelStyle: (FontSize: 15, TextColor: #ffffff, VerticalAlignment: Center, RenderUppercase: true, RenderBold: true)
    )
  );
}
```
