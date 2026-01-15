[← Back](../Variables.md)

# FourFrame

**Defined at:** `Pages\Portals\Portals.ui:1`

## Value

```ui
Group {
  @FrameShort = 1;
  @FrameLong = 88;

  Group {
    Anchor: (Left: @FrameShort, Top: 0, Width: @BoxWidth - @FrameShort * 2, Height: @FrameShort);
    Background: (TexturePath: "FrameTop.png");
  }

  Group {
    Anchor: (Right: 0, Top: 0, Width: @FrameShort, Height: @BoxHeight);
    Background: (TexturePath: "FrameRight.png");
  }

  Group {
    Anchor: (Left: @FrameShort, Bottom: 0, Width: @BoxWidth - @FrameShort * 2, Height: @FrameShort);
    Background: (TexturePath: "FrameBottom.png");
  }

  Group {
    Anchor: (Left: 0, Top: 0, Width: @FrameShort, Height: @BoxHeight);
    Background: (TexturePath: "FrameLeft.png");
  }
}
```
