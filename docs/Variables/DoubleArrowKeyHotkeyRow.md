[← Back](../Variables.md)

# DoubleArrowKeyHotkeyRow ⚠️

⚠️ This variable has only been found in Client ui files, you may or may not be able to use it in mods.

**Defined at:** `Client/Data/Game/Interface/InGame\Hud\ToolsLegends\ToolsLegendsCommon.ui:172`

## Value

```ui
Group {
  @IconOne = "";
  @IconTwo = "";
  @Text = "";
  @InputBindingKeyPrefix = "";
  @LayoutMode = Middle; // or Top

  @Row {
    @RowHintContainer {
      LayoutMode: CenterMiddle;

      HotkeyLabel {
        InputBindingKey: @InputBindingKeyPrefix;
      }
      Group {
        Anchor: (Width: @RowHintIconSize, Height: @RowHintIconSize);
        Background: @IconOne;
      }
      Group {
        Anchor: (Width: @RowHintIconSize, Height: @RowHintIconSize);
        Background: @IconTwo;
      }
    }

    @RowLabelContainer {
      LayoutMode: @LayoutMode;
      @RowLabel {
        Text: @Text;
      }
    }
  }
}
```
