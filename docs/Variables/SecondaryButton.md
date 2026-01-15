[← Back](../Variables.md)

# SecondaryButton

**Defined at:** `Common.ui:270`

## Value

```ui
Button = Button {
  @Anchor = Anchor();
  @Sounds = ();
  @Width = @DefaultButtonHeight;
  Style: (
    ...@SecondaryButtonStyle,
    Sounds: (
      ...$Sounds.@ButtonsLight,
      ...@Sounds
    )
  );
  Anchor: (...@Anchor, Height: @DefaultButtonHeight, Width: @Width);
}
```
