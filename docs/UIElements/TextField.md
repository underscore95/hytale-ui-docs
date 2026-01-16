[← Back](../UIElements.md)

# TextField

This UI element has been found in Server ui files, you should be able to use it in mods.

**First used at:** `Common.ui:424`

## Fields

### Style
Example Values:

- `(FontSize:15)`
- `(FontSize:15,TextColor:#a5b4c4)`
- `(...$Common.@DefaultInputFieldStyle,FontSize:12)`
- `(FontSize:14)`
- `(FontSize:12)`
- `$Common.@DefaultInputFieldStyle`
- `[DefaultInputFieldStyle](Variables/DefaultInputFieldStyle.md)`

### PlaceholderStyle
Example Values:

- `(TextColor:#969494,RenderItalics:true,FontSize:12)`
- `$Common.@DefaultInputFieldPlaceholderStyle`
- `(RenderItalics:true,TextColor:#ffffff(0.5),FontSize:14)`
- `[DefaultInputFieldPlaceholderStyle](Variables/DefaultInputFieldPlaceholderStyle.md)`
- `(TextColor:#ffffff(0.4),RenderItalics:true,)`
- `(TextColor:#4b576c,FontSize:15)`

### Background
Example Values:

- `$Common.@InputBoxBackground`
- `#ffffff(0.1)`
- `(TexturePath:"ChatInputPatch.png",Border:10)`
- `[InputBoxBackground](Variables/InputBoxBackground.md)`

### Anchor
Example Values:

- `(Height:38,Width:200,Right:10)`
- `(Width:230,Right:5)`
- `(...@Anchor,Height:38)`
- `(Height:@InputHeight,Bottom:0)`
- `(Height:$Common.@PrimaryButtonHeight,Width:385)`
- `(Width:270,Right:10)`
- `(Height:38,Width:385,Right:7)`
- `(Height:32)`
- `(Right:0,Width:170,Height:28)`
- `(Width:170)`
- `(Height:44)`
- `(Height:36)`
- `(Top:5,Height:35)`
- `(Height:38)`

### Padding
Example Values:

- `(Left:8)`
- `(Horizontal:27)`
- `(Horizontal:12,Left:28)`
- `(Horizontal:14)`
- `(Horizontal:10,Vertical:8)`
- `(Full:10)`
- `(Horizontal:8)`
- `(Horizontal:10)`

### MaxLength
Example Values:

- `0`
- `32`
- `100`

### PlaceholderText
Example Values:

- `%client.assetEditor.fileSelector.findFile`
- `%client.general.searchField.placeholder`
- `%client.mainMenu.onlinePlay.shareCode.placeholder`
- `%client.mainMenu.servers.inviteCodePlaceholder`
- `%client.feedback.field.summary.placeholder`
- `%client.assetEditor.fileSelector.newDirectoryNamePlaceholder`

### Decoration
Example Values:

- `(Default:(Background:(TexturePath:"SearchFieldPatch.png",Border:8,Color:#ffffff(0.8)),Icon:(Texture:"SearchFieldIcon.png",Width:15,Height:15,Offset:8)))`
- `(Default:(Background:(TexturePath:"SearchFieldPatch.png",Border:8),Icon:(Texture:"SearchFieldIcon.png",Width:15,Height:15,Offset:8)))`
- `(Default:(Icon:(Texture:(TexturePath:"SearchIcon.png",Color:#ffffff(0.25)),Width:16,Height:16,Offset:5),ClearButtonStyle:@ClearButtonStyle))`

### PasswordChar
Example Values:

- `"*"`

### IsReadOnly
Example Values:

- `true`

### FlexWeight
Example Values:

- `1`

