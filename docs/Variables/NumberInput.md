[← Back](../Variables.md)

# NumberInput

This variable has been found in Server ui files, you should be able to use it in mods.

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
