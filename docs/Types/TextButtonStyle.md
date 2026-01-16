[← Back](../Types.md)

# TextButtonStyle

This type has been found in Server ui files, you should be able to use it in mods.

**First used at:** `Common.ui:98`

## Fields

### Default
Example Values:

- `(LabelStyle: (...@ButtonLabelStyleSelected), LabelMaskTexturePath: "../../Common/TextGradient.png")`
- `(Background: PatchStyle(TexturePath: "Common/Buttons/Destructive.png", Border: @ButtonBorder), LabelStyle: @DefaultButtonLabelStyle)`
- `(Background: (TexturePath: "Common/ButtonSmall.png", Border: 6), LabelStyle: @SmallButtonLabelStyle)`
- `(
    Background: #ffffff(0.3),
    LabelStyle: (
      VerticalAlignment: Center
    )
  )`
- `(Background: PatchStyle(TexturePath: "Common/Buttons/Secondary.png", Border: @ButtonBorder), LabelStyle: @SecondaryButtonLabelStyle)`
- `(Background: @PrimaryButtonDefaultBackground, LabelStyle: @PrimaryButtonLabelStyle)`
- `(LabelStyle: @NavigationItemSelectedStyle, LabelMaskTexturePath: "../../Common/TextGradient.png", Background: (TexturePath: "SecondaryTabHighlight.png"))`
- `(LabelStyle: @NavigationItemSelectedStyle, LabelMaskTexturePath: "../../Common/TextGradient.png")`
- `(Background: @ServerBrowserButtonDefaultBackground, LabelStyle: @PrimaryButtonLabelStyle)`
- `(Background: $Common.@PrimaryButtonDefaultBackground, LabelStyle: @TypeButtonLabelStyle)`
- `(Background: PatchStyle(TexturePath: "Common/Buttons/Destructive.png", Border: @ButtonBorderSize), LabelStyle: @PrimaryButtonLabelStyle)`
- `(Background: PatchStyle(TexturePath: "Common/Buttons/Secondary.png", Border: @ButtonBorderSize), LabelStyle: @SmallSecondaryButtonLabelStyle)`
- `(Background: PatchStyle(TexturePath: "ProcessingOnButton.png", Border: $Common.@ButtonBorderSize), LabelStyle: $Common.@SecondaryButtonLabelStyle)`
- `(Background: PatchStyle(Color: #222222(0.3)), LabelStyle: @TagTextButtonLabelStyle)`
- `(LabelStyle: @ButtonLabelStyle)`
- `(LabelStyle: @HeaderTextButtonLabelStyle)`
- `(Background: PatchStyle(TexturePath: "Common/Buttons/Tertiary.png", Border: @ButtonBorder), LabelStyle: @SecondaryButtonLabelStyle)`
- `(LabelStyle: @NavigationItemStyle)`
- `(Background: PatchStyle(TexturePath: "Common/Buttons/Tertiary.png", Border: @ButtonBorderSize), LabelStyle: @SecondaryButtonLabelStyle)`
- `(Background: @ServerBrowserButtonPressedBackground, LabelStyle: @PrimaryButtonLabelStyle)`
- `(
    Background: #ffffff(0.05),
    LabelStyle: (
      VerticalAlignment: Center
    )
  )`
- `(Background: @DefaultButtonDefaultBackground, LabelStyle: @DefaultButtonLabelStyle)`
- `(Background: PatchStyle(TexturePath: "Common/Buttons/Secondary.png", Border: @ButtonBorder), LabelStyle: @SmallSecondaryButtonLabelStyle)`
- `(LabelStyle: (...@ButtonLabelStyle, TextColor: #ffffffff), LabelMaskTexturePath: "MenuButtonLabelGradient.png")`
- `(LabelStyle: (...@SecondaryButtonLabelStyle, TextColor: #ffffffff), LabelMaskTexturePath: "HomeButtonLabelGradient.png")`
- `(Background: PatchStyle(TexturePath: "Common/Buttons/Secondary.png", Border: @ButtonBorderSize), LabelStyle: @SecondaryButtonLabelStyle)`
- `(LabelStyle: (...@ButtonLabelStyle, TextColor: #ffffffff), LabelMaskTexturePath: "HomeButtonLabelGradient.png")`
- `(
    LabelStyle: @NavigationButtonLabelStyle
  )`

### Hovered
Example Values:

- `(Background: PatchStyle(TexturePath: "Common/Buttons/Secondary_Hovered.png", Border: @ButtonBorderSize), LabelStyle: @SecondaryButtonLabelStyle)`
- `(
    LabelStyle: @NavigationButtonLabelStyle,
    Background: #ffffff(0.15)
  )`
- `(Background: (TexturePath: "Common/ButtonSmallHovered.png", Border: 6), LabelStyle: @SmallButtonLabelStyle)`
- `(LabelStyle: (...@ButtonLabelStyleSelected), LabelMaskTexturePath: "../../Common/TextGradient.png")`
- `(Background: @PrimaryButtonHoveredBackground, LabelStyle: @PrimaryButtonLabelStyle)`
- `(Background: PatchStyle(TexturePath: "Common/Buttons/Tertiary_Hovered.png", Border: @ButtonBorderSize), LabelStyle: @SecondaryButtonLabelStyle)`
- `(Background: PatchStyle(TexturePath: "Common/Buttons/Destructive_Hovered.png", Border: @ButtonBorderSize), LabelStyle: @PrimaryButtonLabelStyle)`
- `(Background: @DefaultButtonHoveredBackground, LabelStyle: @DefaultButtonLabelStyle)`
- `(Background: PatchStyle(Color: #222222(0.5)), LabelStyle: @TagTextButtonLabelStyle)`
- `(LabelStyle: (...@ButtonLabelStyle, TextColor: #bbcedf))`
- `(LabelStyle: (...@HeaderTextButtonLabelStyle, TextColor: #eaebee))`
- `(LabelStyle: (...@SecondaryButtonLabelStyle, TextColor: #ffffffff), LabelMaskTexturePath: "HomeButtonLabelHoveredGradient.png")`
- `(Background: PatchStyle(TexturePath: "Common/Buttons/Tertiary_Hovered.png", Border: @ButtonBorder), LabelStyle: @SecondaryButtonLabelStyle)`
- `(Background: PatchStyle(TexturePath: "Common/Buttons/Secondary_Hovered.png", Border: @ButtonBorder), LabelStyle: @SmallSecondaryButtonLabelStyle)`
- `(Background: PatchStyle(TexturePath: "Common/Buttons/Destructive_Hovered.png", Border: @ButtonBorder), LabelStyle: @DefaultButtonLabelStyle)`
- `(Background: PatchStyle(TexturePath: "Common/Buttons/Secondary_Hovered.png", Border: @ButtonBorderSize), LabelStyle: @SmallSecondaryButtonLabelStyle)`
- `(Background: PatchStyle(TexturePath: "Common/Buttons/Secondary_Hovered.png", Border: @ButtonBorder), LabelStyle: @SecondaryButtonLabelStyle)`
- `(Background: @ServerBrowserButtonPressedBackground, LabelStyle: @PrimaryButtonLabelStyle)`
- `(LabelStyle: (...@ButtonLabelStyle, TextColor: #ffffffff, FontSize: 37), LabelMaskTexturePath: "HomeButtonLabelHoveredGradient.png", Background: "Runes.png")`
- `(LabelStyle: (...@ButtonLabelStyle, TextColor: #ffffffff), LabelMaskTexturePath: "MenuButtonLabelHoveredGradient.png")`
- `(Background: @ServerBrowserButtonHoveredBackground, LabelStyle: @PrimaryButtonLabelStyle)`
- `(Background: $Common.@PrimaryButtonHoveredBackground, LabelStyle: @TypeButtonLabelStyle)`
- `(LabelStyle: (...@NavigationItemStyle, TextColor: #7b8998))`
- `(Background: PatchStyle(TexturePath: "ProcessingOnButtonHovered.png", Border: $Common.@ButtonBorderSize), LabelStyle: $Common.@SecondaryButtonLabelStyle)`

### Pressed
Example Values:

- `(Background: PatchStyle(TexturePath: "Common/Buttons/Secondary_Pressed.png", Border: @ButtonBorderSize), LabelStyle: @SecondaryButtonLabelStyle)`
- `(LabelStyle: (...@ButtonLabelStyleSelected), LabelMaskTexturePath: "../../Common/TextGradient.png")`
- `(LabelStyle: (...@ButtonLabelStyle, TextColor: #bbb9b9, FontSize: 37), LabelMaskTexturePath: "HomeButtonLabelHoveredGradient.png", Background: "Runes.png")`
- `(Background: @PrimaryButtonPressedBackground, LabelStyle: @PrimaryButtonLabelStyle)`
- `(Background: PatchStyle(TexturePath: "Common/Buttons/Destructive_Pressed.png", Border: @ButtonBorderSize), LabelStyle: @PrimaryButtonLabelStyle)`
- `(Background: @DefaultButtonPressedBackground, LabelStyle: @DefaultButtonLabelStyle)`
- `(LabelStyle: (...@ButtonLabelStyle, TextColor: #bbb9b9), LabelMaskTexturePath: "MenuButtonLabelHoveredGradient.png")`
- `(Background: PatchStyle(TexturePath: "Common/Buttons/Destructive_Pressed.png", Border: @ButtonBorder), LabelStyle: @DefaultButtonLabelStyle)`
- `(Background: PatchStyle(TexturePath: "Common/Buttons/Secondary_Pressed.png", Border: @ButtonBorder), LabelStyle: @SecondaryButtonLabelStyle)`
- `(Background: PatchStyle(Color: #222222(0.5)), LabelStyle: @TagTextButtonLabelStyle)`
- `(Background: PatchStyle(TexturePath: "Common/Buttons/Secondary_Pressed.png", Border: @ButtonBorder), LabelStyle: @SmallSecondaryButtonLabelStyle)`
- `(Background: PatchStyle(TexturePath: "Common/Buttons/Secondary_Pressed.png", Border: @ButtonBorderSize), LabelStyle: @SmallSecondaryButtonLabelStyle)`
- `(LabelStyle: (...@ButtonLabelStyle, TextColor: #ffffff))`
- `(LabelStyle: (...@SecondaryButtonLabelStyle, TextColor: #bbb9b9), LabelMaskTexturePath: "HomeButtonLabelHoveredGradient.png")`
- `(Background: PatchStyle(TexturePath: "ProcessingOnButtonPressed.png", Border: $Common.@ButtonBorderSize), LabelStyle: $Common.@SecondaryButtonLabelStyle)`
- `(Background: PatchStyle(TexturePath: "Common/Buttons/Tertiary_Pressed.png", Border: @ButtonBorderSize), LabelStyle: @SecondaryButtonLabelStyle)`
- `(Background: @ServerBrowserButtonPressedBackground, LabelStyle: @PrimaryButtonLabelStyle)`
- `(
    LabelStyle: @NavigationButtonLabelStyle,
    Background: #ffffff(0.1)
  )`
- `(Background: $Common.@PrimaryButtonPressedBackground, LabelStyle: @TypeButtonLabelStyle)`
- `(Background: (TexturePath: "Common/ButtonSmallPressed.png", Border: 6), LabelStyle: @SmallButtonLabelStyle)`
- `(Background: PatchStyle(TexturePath: "Common/Buttons/Tertiary_Pressed.png", Border: @ButtonBorder), LabelStyle: @SecondaryButtonLabelStyle)`
- `(LabelStyle: (...@HeaderTextButtonLabelStyle, TextColor: #b6bbc2))`
- `(LabelStyle: (...@NavigationItemStyle, TextColor: #a5b4c4))`

### Disabled
Example Values:

- `(Background: PatchStyle(TexturePath: "Common/Buttons/Disabled.png", Border: @ButtonBorder), LabelStyle: @SmallSecondaryButtonLabelStyle)`
- `(
    Background: #ffffff(0.05),
    LabelStyle: (
      VerticalAlignment: Center,
      TextColor: #ffffff(0.3)
    )
  )`
- `(LabelStyle: (...@ButtonLabelStyle, TextColor: #7c8b99(0.4)))`
- `(LabelStyle: (...@ButtonLabelStyle, TextColor: #ffffff(0.5)), LabelMaskTexturePath: "MenuButtonLabelGradient.png")`
- `(Background: PatchStyle(TexturePath: "Common/Buttons/Disabled.png", Border: @ButtonBorder), LabelStyle: @DefaultButtonLabelStyle)`
- `(Background: @DefaultButtonDisabledBackground, LabelStyle: @DefaultButtonDisabledLabelStyle)`
- `(Background: PatchStyle(TexturePath: "Common/Buttons/Disabled.png", Border: @ButtonBorder), LabelStyle: @SecondaryButtonLabelStyle)`
- `(Background: @DefaultButtonDisabledBackground, LabelStyle: @SmallButtonDisabledLabelStyle)`
- `(Background: PatchStyle(TexturePath: "Common/Buttons/Disabled.png", Border: @ButtonBorderSize), LabelStyle: @SmallSecondaryButtonDisabledLabelStyle)`
- `(
    LabelStyle: (
      ...@NavigationButtonLabelStyle,
      TextColor: #ffffff(0.2)
    )
  )`
- `(Background: PatchStyle(Color: #222222(0.5)), LabelStyle: @TagTextButtonLabelStyle)`
- `(Background: @PrimaryButtonDisabledBackground, LabelStyle: @PrimaryButtonDisabledLabelStyle)`
- `(Background: PatchStyle(TexturePath: "Common/Buttons/Disabled.png", Border: @ButtonBorderSize), LabelStyle: @SecondaryButtonDisabledLabelStyle)`
- `(Background: @ServerBrowserButtonPressedBackground, LabelStyle: @PrimaryButtonDisabledLabelStyle)`
- `(Background: @ServerBrowserButtonDisabledBackground, LabelStyle: @PrimaryButtonDisabledLabelStyle)`
- `(LabelStyle: (...@ButtonLabelStyle, TextColor: #ffffff(0.5)), LabelMaskTexturePath: "HomeButtonLabelGradient.png")`
- `(Background: PatchStyle(TexturePath: "Common/Buttons/Disabled.png", Border: @ButtonBorderSize), LabelStyle: @PrimaryButtonLabelStyle)`
- `(Background: PatchStyle(TexturePath: "Common/Buttons/Disabled.png", Border: @ButtonBorderSize), LabelStyle: @SecondaryButtonLabelStyle)`

### Sounds
Example Values:

- `$Sounds.@ButtonsMain`
- `[ButtonDestructiveSounds](Variables/ButtonDestructiveSounds.md)`
- `$Common.@ButtonSounds`
- `[ButtonSounds](Variables/ButtonSounds.md)`
- `[ButtonsCancel](Variables/ButtonsCancel.md)`
- `$Sounds.@ButtonsLight`
- `$Sounds.@TopBar`

