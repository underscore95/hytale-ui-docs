[← Back](../Variables.md)

# ServerBrowserTopTextButton ⚠️

⚠️ This variable has only been found in Client ui files, you may or may not be able to use it in mods.

**Defined at:** `Client/Data/Game/Interface/MainMenu\Servers\ServersPage.ui:25`

## Value

```ui
TextButton = TextButton {
  @Anchor = Anchor();
  @Sounds = ();
  Style: (
    ...@ServerBrowserTopTextButtonStyle,
    Sounds: (
      ...$Sounds.@ButtonsLight,
      ...@Sounds
    )
  );
  Anchor: (...@Anchor, Height: $Common.@PrimaryButtonHeight);
  Padding: (Horizontal: $Common.@ButtonPadding);
  Text: @Text;
}
```
