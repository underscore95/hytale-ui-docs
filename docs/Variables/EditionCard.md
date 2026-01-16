[← Back](../Variables.md)

# EditionCard ⚠️

⚠️ This variable has only been found in Client ui files, you may or may not be able to use it in mods.

**Defined at:** `Client/Data/Game/Interface/MainMenu\Shop\ShopPage.ui:12`

## Value

```ui
Group {
  Anchor: (Width: @EditionWidth, Height: @EditionHeight + 60);
  LayoutMode: Top;

  Group {
    Anchor: (Width: @EditionWidth, Height: @EditionHeight);
    Background: (TexturePath: @ImagePath);
  }

  Group {
    Anchor: (Top: -15, Height: $Common.@PrimaryButtonHeight);
    LayoutMode: Center;

    Button #Button {
      Anchor: (Width: @ButtonWidth, Height: $Common.@PrimaryButtonHeight);
      Style: @ButtonStyle;
      Padding: (Left: 24, Right: 24);

      Group {
        LayoutMode: Center;

        Label #ButtonLabel {
          Text: @ButtonText;
          Style: @LabelStyle;
        }

        Group #IconContainer {
          Anchor: (Width: 20, Height: 20, Left: 5);
          Background: (TexturePath: "IconRedirect.png");
          Visible: @ShowIcon;
        }
      }
    }
  }
}
```
