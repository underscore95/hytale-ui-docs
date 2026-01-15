[← Back](../Variables.md)

# CancelTextButton

**Defined at:** `Common.ui:196`

## Value

```ui
TextButton = TextButton {
  @Anchor = Anchor();
  @Sounds = ();
  Style: (
    ...@CancelTextButtonStyle,
    Sounds: (
      ...$Sounds.@ButtonsCancel,
      ...@Sounds
    )
  );
  Anchor: (...@Anchor, Height: @DefaultButtonHeight);
  Padding: (Horizontal: @DefaultButtonPadding);
  Text: @Text;
}
```
