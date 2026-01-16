[← Back](../Variables.md)

# TextButton

This variable has been found in Server ui files, you should be able to use it in mods.

**Defined at:** `Common.ui:167`

## Value

```ui
TextButton = TextButton {
  @Anchor = Anchor();
  @Sounds = ();
  Style: (
    ...@DefaultTextButtonStyle,
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
