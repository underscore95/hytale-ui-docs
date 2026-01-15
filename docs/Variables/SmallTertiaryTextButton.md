# SmallTertiaryTextButton

**Defined at:** `Common.ui:240`

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
  Anchor: (...@Anchor, Height: @SmallButtonHeight);
  Padding: (Horizontal: 16);
  Text: @Text;
}
```
