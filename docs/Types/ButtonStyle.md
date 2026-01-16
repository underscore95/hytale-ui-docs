[← Back](../Types.md)

# ButtonStyle

This type has been found in Server ui files, you should be able to use it in mods.

**First used at:** `Common.ui:90`

## Fields

### Default
Example Values:

- `(
    Background: "../IconGeneralSettings.png"
  )`
- `(Background: @PrimaryButtonDefaultBackground)`
- `(Background: (TexturePath: "../Common/OptionBackgroundPatch.png", Border: 16))`
- `(
    Background: "../IconGeneralSettingsActivated.png"
  )`
- `(
    Background: "GameModeTileDisabled.png"
  )`
- `(Background: (TexturePath: "RandomizationUnlockedIcon.png"))`
- `(Background: PatchStyle(TexturePath: "Common/Buttons/Destructive.png", Border: @ButtonBorderSize))`
- `(Background: "CharacterPanelButton.png")`
- `(Background: @DefaultButtonDefaultBackground)`
- `(
    Background: "../IconMaskSettingsActivated.png"
  )`
- `(Background: (TexturePath: "MatchHairColorsIconOn.png"))`
- `(Background: PatchStyle(TexturePath: "Common/Buttons/Secondary.png", Border: @ButtonBorderSize))`
- `(Background: (TexturePath: "ServerRowBackgroundDefault.png", Border: 8))`
- `(Background: PatchStyle(TexturePath: "Common/Buttons/Secondary.png", Border: @ButtonBorder))`
- `(
    Background: "../IconMaskSettings.png"
  )`
- `(Background: PatchStyle(TexturePath: "Common/Buttons/Tertiary.png", Border: @ButtonBorderSize))`
- `(
    Background: "GameModeTile.png"
  )`
- `(Background: $Common.@InputBoxSelectedBackground)`
- `(
    Background: "GameModeTileSelected.png"
  )`
- `(Background: (Color: #00000000))`
- `(Background: PatchStyle(TexturePath: "Common/Buttons/Tertiary.png", Border: @ButtonBorder))`
- `(Background: @PrimarySquareButtonDefaultBackground)`
- `(Background: $Common.@InputBoxBackground)`
- `(Background: "CharacterPanelButtonActive.png")`
- `(Background: (TexturePath: "../../Common/InputBoxSelected.png", Border: 16))`
- `(Background: PatchStyle(TexturePath: "Common/Buttons/Destructive.png", Border: @ButtonBorder))`
- `(Background: (TexturePath: "MatchHairColorsIconOff.png"))`
- `(Background: (TexturePath: "../../Common/InputBox.png", Border: 16))`
- `(Background: (TexturePath: "RandomizationLockedIcon.png"))`
- `(Background: (TexturePath: "../Common/InputBoxSelected.png", Border: 16))`

### Hovered
Example Values:

- `(Background: PatchStyle(TexturePath: "Common/Buttons/Secondary_Hovered.png", Border: @ButtonBorder))`
- `(
    Background: "../IconGeneralSettingsActivated.png"
  )`
- `(Background: (TexturePath: "../../Common/InputBoxHovered.png", Border: 16))`
- `(Background: (TexturePath: "RandomizationUnlockedIconHovered.png"))`
- `(Background: (Color: #ffffff10))`
- `(Background: PatchStyle(TexturePath: "Common/Buttons/Tertiary_Hovered.png", Border: @ButtonBorderSize))`
- `(Background: (TexturePath: "ServerRowBackgroundHovered.png", Border: 8))`
- `(Background: PatchStyle(TexturePath: "Common/Buttons/Destructive_Hovered.png", Border: @ButtonBorderSize))`
- `(Background: PatchStyle(TexturePath: "Common/Buttons/Secondary_Hovered.png", Border: @ButtonBorderSize))`
- `(Background: (TexturePath: "MatchHairColorsIconOffHovered.png"))`
- `(Background: PatchStyle(TexturePath: "Common/Buttons/Destructive_Hovered.png", Border: @ButtonBorder))`
- `(
    Background: "../IconMaskSettingsActivated.png"
  )`
- `(Background: @PrimarySquareButtonHoveredBackground)`
- `(Background: @PrimaryButtonHoveredBackground)`
- `(
    Background: "../IconGeneralSettingsHovered.png"
  )`
- `(Background: (TexturePath: "../Common/OptionBackgroundPatch.png", Border: 16, Color: #ffffff(0.7)))`
- `(Background: PatchStyle(TexturePath: "Common/Buttons/Tertiary_Hovered.png", Border: @ButtonBorder))`
- `(
    Background: "GameModeTileHovered.png"
  )`
- `(Background: @DefaultButtonHoveredBackground)`
- `(
    Background: "../IconMaskSettingsHovered.png"
  )`

### Pressed
Example Values:

- `(Background: @PrimarySquareButtonPressedBackground)`
- `(Background: PatchStyle(TexturePath: "Common/Buttons/Destructive_Pressed.png", Border: @ButtonBorderSize))`
- `(Background: (TexturePath: "../../Common/InputBoxPressed.png", Border: 16))`
- `(Background: PatchStyle(TexturePath: "Common/Buttons/Tertiary_Pressed.png", Border: @ButtonBorder))`
- `(Background: @DefaultButtonPressedBackground)`
- `(Background: @PrimaryButtonPressedBackground)`
- `(Background: (TexturePath: "ServerRowBackgroundDefault.png", Border: 8))`
- `(Background: (TexturePath: "../Common/OptionBackgroundPatch.png", Border: 16, Color: #ffffff(0.85)))`
- `(Background: PatchStyle(TexturePath: "Common/Buttons/Destructive_Pressed.png", Border: @ButtonBorder))`
- `(Background: PatchStyle(TexturePath: "Common/Buttons/Secondary_Pressed.png", Border: @ButtonBorder))`
- `(Background: PatchStyle(TexturePath: "Common/Buttons/Tertiary_Pressed.png", Border: @ButtonBorderSize))`
- `(Background: (Color: #ffffff08))`
- `(Background: PatchStyle(TexturePath: "Common/Buttons/Secondary_Pressed.png", Border: @ButtonBorderSize))`

### Disabled
Example Values:

- `(Background: @DefaultButtonDisabledBackground)`
- `(Background: @PrimaryButtonDisabledBackground)`
- `(Background: (TexturePath: "../Common/OptionBackgroundPatch.png", Border: 16))`
- `(Background: PatchStyle(TexturePath: "Common/Buttons/Disabled.png", Border: @ButtonBorderSize))`
- `(Background: (TexturePath: "ServerRowBackgroundDefault.png", Border: 8))`
- `(Background: PatchStyle(TexturePath: "Common/Buttons/Disabled.png", Border: @ButtonBorder))`
- `(Background: @PrimarySquareButtonDisabledBackground)`

### Sounds
Example Values:

- `$Sounds.@Tiles`
- `(
    Activate: (SoundPath: "../../Sounds/WorldCreationTileActivate.ogg", Volume: 6),
    MouseHover: (SoundPath: $Sounds.@ButtonsLightHover, Volume: 6)
  )`
- `(Activate: (SoundPath: $Sounds.@Tick, Volume: 6))`
- `$Common.@ButtonSounds`
- `[ButtonSounds](Variables/ButtonSounds.md)`
- `(
    Activate: (SoundPath: $Sounds.@Untick, Volume: 6)
  )`
- `$Sounds.@Unlock`
- `(
    Activate: (SoundPath: $Sounds.@Tick, Volume: 6)
  )`
- `(
    Activate: (SoundPath: "../../Sounds/WorldCreationTileActivate.ogg", Volume: 6),
    MouseHover: (SoundPath: $Sounds.@ButtonsLightHover, Volume: 6),
    Context: (SoundPath: $Sounds.@ButtonsLightActivate, Volume: 6)
  )`
- `$Sounds.@Lock`

### ...@AdventureTileButtonSelectedStyle,  Sounds
Example Values:

- `(
    Context: (SoundPath: $Sounds.@ButtonsLightActivate, Volume: 6)
  )`

