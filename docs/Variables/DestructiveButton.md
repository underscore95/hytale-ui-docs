[← Back](../Variables.md)

# DestructiveButton ⚠️

⚠️ This variable has only been found in Client ui files, you may or may not be able to use it in mods.

**Defined at:** `Client/Data/Game/Interface/Common.ui:225`

## Value

```ui
Button = Button {
  @Anchor = Anchor();
  @Sounds = ();
  @Width = @PrimaryButtonHeight;
  Style: (
    ...@DestructiveButtonStyle,
    Sounds: (
      ...$Sounds.@ButtonsLight,
      ...@Sounds
    )
  );
  Anchor: (...@Anchor, Height: @PrimaryButtonHeight, Width: @Width);
}
```
