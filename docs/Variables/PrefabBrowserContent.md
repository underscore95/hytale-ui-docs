[← Back](../Variables.md)

# PrefabBrowserContent

This variable has been found in Server ui files, you should be able to use it in mods.

**Defined at:** `Pages\PrefabBrowser.ui:3`

## Value

```ui
Group {
  LayoutMode: Top;

  Group {
    LayoutMode: Left;
    Anchor: (Bottom: 10, Height: $C.@DropdownBoxHeight);

    $C.@DropdownBox #RootSelector {
      Anchor: (Width: 120, Right: 10, Height: $C.@DropdownBoxHeight);
    }

    $C.@TextField #SearchInput {
      @Anchor = (Left: 0);
      FlexWeight: 1;
      PlaceholderText: %server.customUI.prefabBrowser.searchPlaceholder;
    }
  }

  Group #FileList {
    FlexWeight: 1;
    LayoutMode: TopScrolling;
    ScrollbarStyle: $C.@DefaultScrollbarStyle;
  }
}
```
