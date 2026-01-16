[← Back](../Variables.md)

# PrimaryButton ⚠️

⚠️ This variable has only been found in Client ui files, you may or may not be able to use it in mods.

**Defined at:** `Client/Data/Game/Interface/MainMenu\HomePage.ui:35`

## Value

```ui
TextButton {
  @Sounds = ();
  Anchor: (Top: 10, Height: 60);
  Style: (
    ...@ButtonStyle,
    Sounds: (
      ...$Sounds.@ButtonsMain,
      ...@Sounds
    )
  );
  Text: @Text;
  Padding: (Left: 80, Bottom: 10);
}
```
