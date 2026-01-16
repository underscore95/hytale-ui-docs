[← Back](../Variables.md)

# CancelTextButton

This variable has been found in Server ui files, you should be able to use it in mods.

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
