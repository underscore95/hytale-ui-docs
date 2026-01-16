[← Back](../Variables.md)

# Legend ⚠️

⚠️ This variable has only been found in Client ui files, you may or may not be able to use it in mods.

**Defined at:** `Client/Data/Game/Interface/InGame\Hud\ToolsLegends\ToolsLegendsCommon.ui:64`

## Value

```ui
Group {
  Background: (TexturePath: "LegendContainerPanelPatch.png", Border: 4);
  LayoutMode: Top;
  Anchor: (Left: 20, Top: 130, Width: 280, Height: 780);
  Padding: (Full: 14);
  Visible: true;

  Group {
    Anchor: (Bottom: 10);
    LayoutMode: Left;

    Group {
      FlexWeight: 1;
      LayoutMode: Left;

      @RowHintContainer {
        HotkeyLabel #ToggleLegendKey {
          InputBindingKey: "L";
        }
      }
    }

    Label #Title {
      Style: (
        Alignment: Center,
        FontSize: 16,
        RenderBold: true,
        RenderUppercase: true
      );
      Text: %client.builderTools.legend.title;
    }

    Group {
      FlexWeight: 1;
    }

  }

  Group #Pages {}

  Group {
    FlexWeight: 1;
  }

  Group {
    LayoutMode: Center;

    ActionButton #PreviousPage {
      Disabled: true;
      KeyBindingLabel: "J";
    }

    Label #PageCount {
      Padding: (Horizontal: 10);
      Style: (
        Alignment: Center,
        FontSize: 16,
        RenderBold: true,
        RenderUppercase: false
      );
      Text: "X / X";
    }

    ActionButton #NextPage {
      Disabled: true;
      KeyBindingLabel: "K";
    }
  }
}
```
