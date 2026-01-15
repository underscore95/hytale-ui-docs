# CancelButton

**Defined at:** `Common.ui:211`

## Value

```ui
Button = Button {
  @Anchor = Anchor();
  @Sounds = ();
  @Width = @DefaultButtonHeight;
  Style: (
    ...@CancelButtonStyle,
    Sounds: (
      ...$Sounds.@ButtonsLight,
      ...@Sounds
    )
  );
  Anchor: (...@Anchor, Height: @DefaultButtonHeight, Width: @Width);
}
```
