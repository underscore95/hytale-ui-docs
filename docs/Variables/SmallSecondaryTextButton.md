[← Back](../Variables.md)

# SmallSecondaryTextButton

**Defined at:** `Common.ui:225`

## Value

```ui
TextButton = TextButton {
  @Anchor = Anchor();
  @Sounds = ();
  Style: (
    ...@SmallSecondaryTextButtonStyle,
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
