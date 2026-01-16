[← Back](../Variables.md)

# SecondaryButton ⚠️

⚠️ This variable has only been found in Client ui files, you may or may not be able to use it in mods.

**Defined at:** `Client/Data/Game/Interface/MainMenu\HomePage.ui:49`

## Value

```ui
TextButton {
  @Sounds = ();
  Anchor: (Height: 45);
  Style: (
    ...@SecondaryButtonStyle,
    Sounds: (
      ...$Sounds.@ButtonsMain,
      ...@Sounds
    )
  );
  Text: @Text;
  Padding: (Left: 80, Bottom: 10);
}
```
