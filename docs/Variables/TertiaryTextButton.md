# TertiaryTextButton

**Defined at:** `Common.ui:284`

## Value

```ui
TextButton = TextButton {
  @Anchor = Anchor();
  @Sounds = ();
  Style: (
    ...@TertiaryTextButtonStyle,
    Sounds: (
      ...$Sounds.@ButtonsLight,
      ...@Sounds
    )
  );
  Anchor: (...@Anchor, Height: @DefaultButtonHeight);
  Padding: (Horizontal: @DefaultButtonPadding);
  Text: @Text;
}
```
