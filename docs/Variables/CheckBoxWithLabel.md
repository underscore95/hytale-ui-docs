[← Back](../Variables.md)

# CheckBoxWithLabel

**Defined at:** `Common.ui:397`

## Value

```ui
Group {
  @Checked = false;

  LayoutMode: Left;

  @CheckBox #CheckBox {
    Value: @Checked;
  }

  Label {
    Text: @Text;
    Anchor: (Right: 30, Left: 11);
    Style: (
      ...@DefaultLabelStyle,
      VerticalAlignment: Center
    );
  }
}
```
