[← Back](../Variables.md)

# SmallSecondaryTextButton ⚠️

⚠️ This variable has only been found in Client ui files, you may or may not be able to use it in mods.

**Defined at:** `Client/Data/Game/Interface/Common.ui:254`

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
