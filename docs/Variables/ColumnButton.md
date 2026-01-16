[← Back](../Variables.md)

# ColumnButton ⚠️

⚠️ This variable has only been found in Client ui files, you may or may not be able to use it in mods.

**Defined at:** `Client/Data/Game/Interface/MainMenu\Servers\ServersPage.ui:106`

## Value

```ui
Button = Button {
  LayoutMode: Center;
  Padding: (Horizontal: 9);
  Anchor: (Left: 10, Right: 10);

  Label {
    Style: (HorizontalAlignment: Center, VerticalAlignment: Center, TextColor: #6c7886);
    Text: @Text;
  }

  Group #SortCaret {
    Visible: false;
    Anchor: (Width: 18, Height: 9, Left: 6);
    Background: "SortCaret.png";
  }

  Group #ReverseSortCaret {
    Visible: false;
    Anchor: (Width: 18, Height: 9, Left: 6);
    Background: "ReverseSortCaret.png";
  }
}
```
