---
name: fonts
description: Font selection, loading, and typography best practices for video projects
metadata:
  tags: fonts, typography, text, readability, licensing
---

## When to use

Use this skill whenever you need to work with fonts in your video projects - selecting appropriate typefaces, loading fonts correctly, ensuring readability, and applying typographic principles to create effective on-screen text.

## Core Principles

### 1. Font Fundamentals
- **Typeface vs Font**:
  - **Typeface**: Design of lettering (Arial, Times New Roman).
  - **Font**: Specific style/size/weight of typeface (Arial Bold 12pt).
- **Font categories**:
  - **Serif**: Small strokes on letter ends (Times, Georgia). Traditional, formal, readable in print.
  - **Sans-serif**: No strokes (Arial, Helvetica). Modern, clean, better for screens.
  - **Monospace**: All characters same width (Courier, Consolas). Technical, code, typewriter style.
  - **Display**: Decorative, for headlines (Impact, Bebas). Large sizes only.
  - **Script**: Handwritten style (Brush Script, Pacifico). Informal, personal.
  - **Slab serif**: Thick serifs (Rockwell, Courier). Bold, industrial.
- **Font metrics**:
  - **Ascender**: Part of letter above x-height (b, d, h).
  - **Cap height**: Height of capital letters.
  - **x-height**: Height of lowercase x. Main body size.
  - **Descender**: Part below baseline (g, p, y).
  - **Baseline**: Line letters sit on.
  - **Leading**: Space between baselines (line spacing).
  - **Tracking**: Letter spacing across entire text block.
  - **Kerning**: Space between specific pairs (AV, To).

### 2. Font Selection for Video
- **Readability first**: Video is viewed on small screens, fast motion. Choose clear fonts.
- **Sans-serif for body**: Arial, Helvetica, Roboto, Inter, SF Pro. Most readable on screens.
- **Serif for elegance**: Times, Georgia for formal/traditional content.
- **Display for impact**: Use decorative fonts only for headlines, logos. Never for body.
- **Match tone**: Corporate = clean sans, luxury = elegant serif, playful = rounded/script.
- **Limit families**: Use 1-2 font families per video. Too many looks unprofessional.
- **Weight variety**: Use light, regular, medium, bold, black from same family for hierarchy.
- **Avoid overused fonts**: Comic Sans, Papyrus, Curlz MT (unprofessional).

### 3. Font Sizing & Scaling
- **Minimum size**: 24pt for 1080p video. For mobile (TikTok), 32pt+.
- **Size hierarchy**:
  - **Headline**: 48-72pt
  - **Subhead**: 32-48pt
  - **Body**: 24-32pt
  - **Caption**: 18-24pt
- **Pixel vs point**: Video software often uses pixels. 1pt ≈ 1.33px at 72 DPI. But video is resolution-based. Test readability.
- **Viewing distance**: Larger text for expected viewing distance (phone vs TV).
- **Safe area**: Text within 90% of frame. Don't put important text at edges.

### 4. Color & Contrast
- **Contrast is king**: Text must stand out from background.
- **Light text on dark**: White/yellow on dark background. Most common.
- **Dark text on light**: Black/dark gray on light background.
- **Outline/stroke**: Add 1-2px outline to improve readability on busy backgrounds.
- **Shadow**: Drop shadow (offset, blur) separates text from background.
- **Background box**: Semi-transparent rectangle behind text.
- **Color psychology**:
  - **White**: Clean, neutral.
  - **Yellow**: Attention, caution.
  - **Red**: Urgency, danger.
  - **Blue**: Trust, calm.
  - **Green**: Success, nature.
- **Brand colors**: Use brand palette for consistency.
- **Accessibility**: WCAG AA requires 4.5:1 contrast ratio for normal text.

### 5. Line Spacing & Layout
- **Leading (line spacing)**: 1.3-1.5x font size. Too tight = cramped, too loose = disconnected.
- **Measure (line length)**: 35-50 characters per line maximum. Longer lines hard to read.
- **Alignment**:
  - **Left**: Most readable (left-aligned, ragged right).
  - **Center**: For headlines, short text. Harder for long blocks.
  - **Right**: Rare, for specific design.
  - **Justified**: Can create rivers (gaps). Use hyphenation.
- **Margins**: Leave breathing room. Don't edge-to-edge.
- **Text safe area**: Keep within 90% of frame.

### 6. Hierarchy & Emphasis
- **Size**: Larger = more important.
- **Weight**: Bold > medium > regular > light.
- **Color**: Bright/dark draws attention.
- **Style**: Italic, uppercase for emphasis.
- **Spacing**: More space around important elements.
- **Position**: Top/center = important.
- **Contrast**: High contrast elements stand out.
- **Isolation**: Alone = more important than in group.

### 7. Font Licensing & Rights
- **Check license**: Can you use in video? Most desktop licenses allow.
- **Embedding**: Some fonts restrict embedding in video. Check EULA.
- **Web fonts**: Different license. Don't use without permission.
- **Open source**: Google Fonts, Adobe Fonts (included with subscription) safe.
- **Commercial use**: Ensure license covers commercial distribution.
- **Modification**: Some fonts forbid modification.
- **Attribution**: Some require credit.
- **Sublicensing**: Can you include with product? Usually no.
- **Keep records**: Save license documentation with project.

### 8. Font Loading & Management
- **System fonts**: Already installed. Use directly. Fast.
- **Project fonts**: Copy font files to project folder, load manually.
- **Font activation**: Use font manager (Suitcase, FontBase) to activate/deactivate.
- **Font embedding**: Some apps embed fonts in project file. Be aware of licensing.
- **Font subsets**: Load only needed characters (subsetting) to reduce size.
- **Font fallbacks**: Specify backup fonts in case primary missing.
  - Example: `font-family: 'CustomFont', Arial, sans-serif`.
- **Font formats**: OTF, TTF standard. WOFF/WOFF2 for web.
- **Font caching**: Clear font cache if issues.

### 9. Text Animation Considerations
- **Readability during motion**: Text moving too fast = unreadable. Keep motion slow enough to read.
- **Motion blur**: Can reduce readability. Use sparingly on text.
- **Scale limits**: Don't scale text too small or too large (pixelation).
- **Easing**: Smooth motion easier to read than linear.
- **Duration**: Text should stay on screen long enough to read (1.5s minimum).
- **Reveal animations**: Text should appear before reader needs it.
- **Position changes**: Avoid moving text horizontally while reading (eye tracking difficulty).
- **Color changes**: Subtle. Sudden color shifts distracting.

### 10. Platform-Specific Typography
- **TikTok/Reels**:
  - **Size**: Very large (32-48pt+).
  - **Font**: Bold sans-serif (Impact, Bebas, custom bold fonts).
  - **Duration**: Quick (1-3s).
  - **Position**: Top/bottom thirds, not center (avoid UI).
  - **Contrast**: High. White with black outline or black with white outline.
  - **Animation**: Pop-in, typewriter, glitch.
- **YouTube**:
  - **Size**: Moderate (24-36pt).
  - **Font**: Clean sans (Roboto, Open Sans).
  - **Duration**: Longer (3-10s).
  - **Position**: Bottom for subtitles, top/bottom for emphasis.
  - **Lower thirds**: Standard 3-line format.
- **Instagram**:
  - **Size**: Large (28-40pt).
  - **Font**: Stylish but readable (Montserrat, Poppins).
  - **Aesthetic**: Match brand look.
  - **Captions**: Often burned in. Large, high contrast.
- **Twitter/X**:
  - **Size**: Large (28-40pt).
  - **Font**: Bold, impactful.
  - **Duration**: Very short (1-3s).
  - **Loopable**: Text should make sense looped.
- **LinkedIn**:
  - **Size**: Moderate (24-32pt).
  - **Font**: Professional (Arial, Helvetica, Georgia).
  - **Tone**: Business-appropriate.
  - **Subtitles**: Important for sound-off viewing.

## Technical Guidelines

### Font Formats & Compatibility
- **OTF (OpenType)**: Modern, advanced features (ligatures, alternates). Preferred.
- **TTF (TrueType)**: Older, simpler. Widely supported.
- **WOFF/WOFF2**: Web fonts. Compressed. For web use.
- **Variable fonts**: Single file with multiple weights/widths. Efficient.
- **Bitmap fonts**: Pixelated. Rare, for retro effect.
- **Stroke/fill fonts**: Outline only. For effects.

### Font Installation & Activation
- **Windows**:
  - **Install**: Right-click → Install for all users.
  - **Location**: C:\Windows\Fonts.
  - **Activate**: Automatic once installed.
- **macOS**:
  - **Install**: Double-click → Install Font.
  - **Location**: /Library/Fonts (system) or ~/Library/Fonts (user).
  - **Font Book**: Manage fonts.
- **Linux**:
  - **Install**: Copy to ~/.fonts or /usr/share/fonts.
  - **Update cache**: `fc-cache -fv`.
- **Font managers**:
  - **Suitcase**: Professional font management.
  - **FontBase**: Free, modern.
  - **NexusFont**: Windows.
  - **RightFont**: macOS.

### Using Fonts in Video Software
- **After Effects**:
  - **Text layer**: Choose font from character panel.
  - **Font loading**: If font missing, AE substitutes. Install font to fix.
  - **Font collection**: Use font collection to organize.
  - **Text animator**: Animate font properties.
- **Premiere Pro**:
  - **Essential Graphics**: Choose font in graphics panel.
  - **Legacy titles**: Font dropdown.
  - **Font missing**: Yellow warning. Install font.
- **DaVinci Resolve**:
  - **Text+**: Choose font in inspector.
  - **Fusion text**: Font controls in inspector.
- **Motion**:
  - **Text tool**: Font in format inspector.

### Font Subsetting & Optimization
- **Why subset**: Reduce file size by including only used characters.
- **When**: Web delivery, embedded fonts in video (rare).
- **Tools**:
  - **pyftsubset** (fonttools): Command-line subsetting.
  - **Glyphhanger**: Web font subsetting.
  - **Font Squirrel Generator**: Online subsetter.
- **Process**:
  - **Analyze**: Find which characters used in project.
  - **Subset**: Create new font file with only those characters.
  - **Replace**: Use subset font in project.
- **Caution**: Subsetting irreversible. Keep original.

### Font Rendering & Anti-Aliasing
- **Anti-aliasing**: Smooths jagged edges.
  - **None**: Sharp, pixelated. For retro effect.
  - **Sharp**: Crisp edges. Good for small text.
  - **Strong**: Very smooth. Good for large text.
  - **Crisp**: Balanced.
- **Subpixel rendering**: Uses LCD subpixels for sharper text (Windows ClearType).
- **Hinting**: Adjusts outlines to pixel grid. Improves small text clarity.
- **Resolution**: Higher resolution = smoother text.
- **Scaling**: Don't scale text too much. Scale up = pixelated, scale down = blurry.
- **Motion blur**: Text in motion may need more anti-aliasing.

### Font Accessibility
- **Size**: Minimum 24pt for video. Larger for accessibility.
- **Contrast**: 4.5:1 ratio minimum (WCAG AA).
- **Font choice**: Simple, sans-serif for dyslexic readers (OpenDyslexic, Arial).
- **Line spacing**: 1.5x for readability.
- **Avoid all caps**: Harder to read. Use for short emphasis only.
- **Avoid italics**: Harder to read. Use sparingly.
- **Justified text**: Creates rivers. Left-align better.
- **Color blindness**: Don't rely on color alone. Use patterns/labels.
- **Language support**: Font must support all characters needed (CJK, Arabic, etc.).

## Common Pitfalls to Avoid

- **Font too small**: Unreadable on mobile. Test on phone.
- **Poor contrast**: Text blends into background. Add outline/background.
- **Decorative fonts for body**: Hard to read. Use only for headlines.
- **Too many fonts**: Looks unprofessional. Limit to 1-2 families.
- **Missing font**: Text falls back to system font. Install or outline.
- **Licensing violation**: Using font without proper license. Check EULA.
- **No hierarchy**: All text same size/weight. Viewer doesn't know what's important.
- **Justified text with rivers**: Gaps in text. Use left-align or hyphenate.
- **All caps for long text**: Harder to read than sentence case.
- **Italics for long blocks**: Reduced readability.
- **Text on busy background**: Disappears. Add background box or outline.
- **Text too close to edge**: Gets cut off. Use safe area.
- **No fallback fonts**: If primary font missing, defaults to ugly system font. Specify stack.
- **Scaling text too much**: Pixelated when scaled up. Use vector (text layer) not raster.
- **Ignoring platform guidelines**: Each platform has font recommendations.

## Advanced Techniques

### 1. Dynamic Font Loading
- **Parameter-driven**: Load different fonts based on parameter (brand, language).
- **Font fallback chain**: `font-family: 'CustomFont', 'BackupFont', Arial, sans-serif`.
- **Web font loading**: For web-based video players, load via CSS `@font-face`.
- **Font subsetting**: Load only needed characters to reduce size.
- **Font loading APIs**: Use Font Loading API to know when font ready.

### 2. Advanced Typography
- **Ligatures**: Special character combinations (fi, fl). Enable for elegance.
- **Small caps**: Uppercase letters at x-height. Elegant alternative to lowercase.
- **Oldstyle figures**: Numbers with varying height (like lowercase). More readable.
- **Tabular figures**: Monospaced numbers for tables.
- **Fractions**: Proper fraction glyphs (½ not 1/2).
- **Superscript/subscript**: For footnotes, formulas.
- **Stylistic sets**: Alternate character sets (swash, etc.).
- **Variable fonts**: Adjust weight, width, optical size continuously.

### 3. Text Effects & Styling
- **Stroke**: Outline around text. Improves readability.
- **Shadow**: Drop shadow for depth.
- **Fill gradient**: Text with gradient instead of solid color.
- **Texture fill**: Text filled with image/pattern.
- **3D extrusion**: Extrude text for 3D effect.
- **Glow**: Outer glow for neon effect.
- **Bevel & emboss**: 3D relief effect.
- **Displacement**: Distort text with map.
- **Text on path**: Text follows curved path.
- **Text masking**: Text reveals underlying video/image.

### 4. Responsive Typography
- **Scale with composition**: Use relative units (em, rem) or calculate based on comp size.
- **Breakpoints**: Different font sizes for different resolutions (mobile vs desktop).
- **Container queries**: Text size based on container width (advanced).
- **Clamp**: `clamp(min, preferred, max)` for fluid scaling.
- **Viewport units**: `vw`, `vh` scale with viewport.
- **Aspect ratio**: Maintain readability across aspect ratios.

### 5. International Typography
- **CJK fonts**: Chinese, Japanese, Korean need specific fonts (Noto Sans CJK, Source Han Sans).
- **Arabic script**: Right-to-left, connected letters. Use appropriate fonts (Noto Naskh Arabic).
- **Devanagari**: Hindi, Sanskrit. Complex shaping.
- **Thai**: No spaces between words. Different line height.
- **Diacritics**: Accents (é, ü, ñ). Font must support.
- **Text expansion**: German, Finnish longer than English. Plan layout.
- **Text contraction**: Chinese, Japanese shorter. May need larger font.
- **Line breaking rules**: Different languages have different word-breaking rules.
- **Hyphenation**: Language-specific hyphenation patterns.

### 6. Kinetic Typography
- **Text animation**: Animate text properties (position, scale, rotation, opacity).
- **Per-character animation**: Animate each letter separately.
- **Text path animation**: Text follows motion path.
- **Text reveal**: Typewriter, fade, slide, wipe.
- **Text deformation**: Squash, stretch, wave.
- **Text particle**: Text made of particles that disperse/reform.
- **Text 3D**: Extrude, animate in 3D space.
- **Text sync to audio**: Animate text to voiceover or music.

### 7. Font Performance Optimization
- **Subset fonts**: Only include used characters.
- **Use system fonts**: Fastest, no loading.
- **Cache fonts**: Browser/OS caching.
- **Preload**: For web, preload critical fonts.
- **Variable fonts**: Single file replaces multiple weights.
- **Compress fonts**: WOFF2 compressed format.
- **Limit font families**: Fewer fonts = less memory.
- **Avoid too many weights**: Only use needed weights.
- **Use font-display: swap**: Show fallback while loading.

### 8. Font Testing & QA
- **Readability test**: View on actual device (phone, tablet, TV).
- **Size test**: Check minimum readable size.
- **Contrast test**: Use contrast checker tool.
- **Language test**: Ensure all characters render correctly.
- **Fallback test**: Disable primary font, check fallback.
- **Motion test**: Animated text readable at speed?
- **Duration test**: Text on screen long enough to read?
- **Accessibility test**: Screen reader compatibility (if interactive).
- **Cross-platform**: Test on different OS/browsers.

### 9. Font Management in Teams
- **Font library**: Shared repository of approved fonts.
- **Licensing tracker**: Document font licenses, expiration.
- **Font installation guide**: Instructions for new team members.
- **Naming conventions**: Consistent font naming.
- **Version control**: Track font file versions.
- **Backup**: Backup font library.
- **Audit**: Periodically review font usage, remove unused.
- **Compliance**: Ensure all fonts properly licensed.

### 10. Custom Font Creation
- **When to create**: No existing font fits brand/need.
- **Tools**:
  - **Glyphs**: Mac, professional.
  - **FontLab**: Cross-platform, professional.
  - **RoboFont**: Mac, scriptable.
  - **FontForge**: Free, open-source.
  - **BirdFont**: Free, simple.
- **Process**:
  - **Design**: Draw glyphs (characters).
  - **Metrics**: Set widths, side bearings.
  - **Kerning**: Adjust pairs.
  - **Hinting**: Add pixel-level instructions (optional).
  - **Export**: OTF/TTF.
  - **Test**: Use in projects.
- **Considerations**:
  - **Time**: Font creation is weeks/months.
  - **Skill**: Requires typography knowledge.
  - **Licensing**: Decide distribution rights.
  - **Character set**: Which languages/symbols needed?

## Workflow Recommendations

1. **Define requirements**: What text needs? Headlines, body, captions? Languages?
2. **Select font families**: Choose 1-2 families with multiple weights.
3. **Check licensing**: Ensure proper rights for use.
4. **Install/activate**: Get fonts installed on system.
5. **Test readability**: Sample text at target size on target device.
6. **Define hierarchy**: Map sizes/weights to content levels.
7. **Create style guide**: Document font choices, sizes, colors, spacing.
8. **Apply consistently**: Use style guide throughout project.
9. **Review**: Check all text for readability, contrast, hierarchy.
10. **Export**: Ensure fonts embedded or converted to paths if needed.

## Related Skills

For complementary techniques, refer to:
- `./core-techniques/text-animation.md` - Animating text
- `./rules/subtitles.md` - Subtitles and captions typography
- `./core-techniques/color-grading.md` - Color for text contrast
- `./core-techniques/design.md` - General design principles
- `./styles/cinematic.md` - Elegant typography for film
- `./styles/dark-tutorial.md` - Tutorial text presentation
- `./styles/tiktok-news-hype.md` - High-impact typography for news

