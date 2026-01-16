[← Back](../Variables.md)

# Button ⚠️

⚠️ This variable has only been found in Client ui files, you may or may not be able to use it in mods.

**Defined at:** `Client/Data/Game/Interface/InGame\Pages\ContentCreationPage.ui:10`

## Value

```ui
Button = Button {
  Padding: (Left: 20, Right: 20, Top: 17, Bottom: 20);
  Anchor: (Bottom: 10);
  LayoutMode: Left;
  Visible: false;
  Style: (
    Default: (Background: (TexturePath: "Inventory/RecipeCatalogueItemPatch.png", Border: 8)),
    Hovered: (Background: (TexturePath: "Inventory/RecipeCatalogueItemPatch.png", Border: 8, Color: #ffffff(0.5)))
  );

  Group {
    LayoutMode: Top;
    FlexWeight: 1;

    Label {
      Text: @Title;
      Style: ( RenderBold: true);
    }

    Label {
      Style: (Wrap: true, TextColor: #ffffff(0.4));
      Text: @Description;
    }
  }

  Group {
    Anchor: (Left: 50);

    ActionButton #BindingLabel {}
  }
}
```
