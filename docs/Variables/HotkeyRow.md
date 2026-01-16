[← Back](../Variables.md)

# HotkeyRow ⚠️

⚠️ This variable has only been found in Client ui files, you may or may not be able to use it in mods.

**Defined at:** `Client/Data/Game/Interface/InGame\Hud\ToolsLegends\ToolsLegendsCommon.ui:149`

## Value

```ui
Group {
  @InputBindingKey = "";
  @InputBindingKeyPrefix = "";
  @Description = "";
  @LayoutMode = Middle; // or Top

  @Row {
    @RowHintContainer{
      HotkeyLabel {
        InputBindingKey: @InputBindingKey;
        InputBindingKeyPrefix: @InputBindingKeyPrefix;
      }
    }

    @RowLabelContainer {
      LayoutMode: @LayoutMode;
      @RowLabel {
        Text: @Description;
      }
    }
  }
}
```
