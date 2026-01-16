[← Back](../Variables.md)

# PrimarySquareButton ⚠️

⚠️ This variable has only been found in Client ui files, you may or may not be able to use it in mods.

**Defined at:** `Client/Data/Game/Interface/Common.ui:196`

## Value

```ui
Button = Button {
  @Anchor = Anchor();
  @Sounds = ();
  Style: (
    ...@PrimarySquareButtonStyle,
    Sounds: (
      ...$Sounds.@ButtonsLight,
      ...@Sounds
    )
  );
  Anchor: (...@Anchor, Height: @PrimaryButtonHeight, Width: @PrimaryButtonHeight);
  Padding: (Horizontal: @ButtonPadding);
}
```
