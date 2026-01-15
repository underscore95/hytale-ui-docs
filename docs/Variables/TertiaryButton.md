[← Back](../Variables.md)

# TertiaryButton

**Defined at:** `Common.ui:299`

## Value

```ui
Button = Button {
  @Anchor = Anchor();
  @Sounds = ();
  @Width = @DefaultButtonHeight;
  Style: (
    ...@TertiaryButtonStyle,
    Sounds: (
      ...$Sounds.@ButtonsLight,
      ...@Sounds
    )
  );
  Anchor: (...@Anchor, Height: @DefaultButtonHeight, Width: @Width);
}
```
