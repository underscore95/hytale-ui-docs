[← Back](../Variables.md)

# TabButton ⚠️

⚠️ This variable has only been found in Client ui files, you may or may not be able to use it in mods.

**Defined at:** `Client/Data/Game/Interface/MainMenu\MyAvatar\MyAvatarPage.ui:71`

## Value

```ui
Group {
  Anchor: (Width: 47, Height: 47, Top: 2, Bottom: 2);
  Background: (TexturePath: "CategoryIconBackground.png");

  Button #Button {
    Anchor: Anchor(Width: 66, Height: 50);
    Style: (
      ...$Common.@PrimaryButtonStyle,
      Sounds: $Sounds.@ButtonsLight
    );

    Group {
      Anchor: Anchor(Width: 67, Height: 33, Left: -2);
      Background: "SelectedCategoryArrow.png";
      Visible: false;
    }
  }
}
```
