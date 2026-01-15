[← Back](../Variables.md)

# Button

**Defined at:** `Common.ui:182`

## Value

```ui
Button = Button {
  @Anchor = Anchor();
  @Sounds = ();
  Style: (
    ...@DefaultSquareButtonStyle,
    Sounds: (
      ...$Sounds.@ButtonsLight,
      ...@Sounds
    )
  );
  Anchor: (...@Anchor, Height: @DefaultButtonHeight, Width: @DefaultButtonHeight);
  Padding: (Horizontal: @DefaultButtonPadding);
}
```
