[← Back](../Variables.md)

# TertiaryTextButton ⚠️

⚠️ This variable has only been found in Client ui files, you may or may not be able to use it in mods.

**Defined at:** `Client/Data/Game/Interface/Common.ui:283`

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
  Anchor: (...@Anchor, Height: @PrimaryButtonHeight);
  Padding: (Horizontal: @ButtonPadding);
  Text: @Text;
}
```
