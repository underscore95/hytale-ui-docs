[← Back](../Variables.md)

# SecondaryTextButton ⚠️

⚠️ This variable has only been found in Client ui files, you may or may not be able to use it in mods.

**Defined at:** `Client/Data/Game/Interface/Common.ui:239`

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
  Anchor: (...@Anchor, Height: @PrimaryButtonHeight);
  Padding: (Horizontal: @ButtonPadding);
  Text: @Text;
}
```
