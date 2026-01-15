# SecondaryTextButton

**Defined at:** `Common.ui:255`

## Value

```ui
TextButton = TextButton {
  @Anchor = Anchor();
  @Sounds = ();
  Style: (
    ...@SecondaryTextButtonStyle,
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
