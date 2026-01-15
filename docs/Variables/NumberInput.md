[← Back](../Variables.md)

# NumberInput

**Defined at:** `Pages\PrefabEditorSettings.ui:10`

## Value

```ui
Group {
  @Visible = false;
  @Left = 32;
  LayoutMode: Left;
  Anchor: (Left: @Left, Top: 6);
  Visible: @Visible;

  @InputLabel {
    Text: @Label;
  }

  $C.@NumberField #Input {
    @Anchor = (Width: 60, Left: 0, Right: 16);

    Format: (
      MaxDecimalPlaces: 0,
      Step: 1
    );
  }
}
```
