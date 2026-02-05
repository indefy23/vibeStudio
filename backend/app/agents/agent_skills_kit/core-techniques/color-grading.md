---
name: color-grading
description: Color correction and grading techniques for video including LUTs, contrast, saturation, and cinematic looks
metadata:
  tags: color, grading, correction, LUTs, contrast, saturation, cinematic
---

## When to use

Use this skill whenever you need to correct color issues in your footage or apply artistic color styles to enhance mood, create consistency, or achieve a specific visual aesthetic. Color grading is essential for making your video look professional, cinematic, and emotionally resonant.

## Core Principles

### 1. Color Correction vs. Color Grading
- **Color Correction**: Fix technical issues to make footage look natural and balanced.
  - White balance: Ensure whites are white under given lighting.
  - Exposure: Adjust brightness/darkness to proper levels.
  - Contrast: Make darks dark and lights bright without clipping.
  - Saturation: Make colors natural, not oversaturated.
  - Goal: Make different shots match each other (continuity).

- **Color Grading**: Apply artistic style to evoke emotion or create look.
  - Color palette: Choose specific color combinations (teal & orange, muted tones, high contrast).
  - Mood: Warm tones = cozy, nostalgic; cool tones = clinical, futuristic, sad.
  - Style: Cinematic, vintage, cyberpunk, film noir, etc.
  - Goal: Create visual storytelling that supports narrative.

- **Workflow order**: Always correct first, then grade. You can't grade bad color effectively.

### 2. Understanding Color Theory
- **Color wheel**: Primary (red, blue, yellow), secondary (green, orange, purple), tertiary.
- **Complementary colors**: Opposite on wheel (blue/orange, red/green). Create contrast and visual interest.
- **Analogous colors**: Adjacent on wheel (blue, blue-green, green). Create harmony.
- **Triadic**: Three evenly spaced colors. Vibrant, balanced.
- **Warm vs cool**: Warm (red, orange, yellow) = advance, come forward. Cool (blue, green) = recede.
- **Color psychology**:
  - Red: passion, danger, energy
  - Blue: calm, trust, sadness
  - Green: nature, envy, sickness
  - Yellow: happiness, caution
  - Purple: luxury, mystery
  - Orange: warmth, enthusiasm
  - Black: power, elegance, death
  - White: purity, simplicity

### 3. Technical Color Parameters
- **Luma (brightness)**: 0 (black) to 100 (white).
- **Contrast**: Difference between darkest and brightest areas. High contrast = punchy, cinematic. Low contrast = flat, dreamy.
- **Saturation**: Intensity of colors. 0 = grayscale, 100 = vivid.
- **Hue**: Actual color (red, green, blue, etc.). Shifting hue changes color family.
- **Luminance**: Brightness of specific color channel (R, G, B).
- **Color temperature**: Warm (yellow/orange) vs cool (blue). Measured in Kelvin.
- **Tint**: Green vs magenta balance.

### 4. Color Grading Workflow
- **Step 1: Normalize**: Bring all clips to similar exposure and white balance.
- **Step 2: Primary correction**: Adjust overall image with lift/gamma/gain or shadows/midtones/highlights.
  - **Lift/Shadows**: Dark areas. Raise to brighten shadows, lower to deepen.
  - **Gamma/Midtones**: Middle brightness. Affects overall contrast curve.
  - **Gain/Highlights**: Bright areas. Lower to bring down highlights, raise to brighten.
- **Step 3: Secondary correction**: Adjust specific color ranges (HSL qualifiers).
  - Isolate skin tones and keep them natural.
  - Adjust specific colors (make blues more cyan, greens more yellow).
- **Step 4: Creative grade**: Apply stylistic look (LUTs, color wheels, curves).
- **Step 5: Final touches**: Vignette, grain, sharpening, saturation boost.

### 5. LUTs (Look-Up Tables)
- **What is a LUT**: A mathematical formula that transforms input colors to output colors.
- **Types**:
  - **Technical LUT**: Convert camera log/raw to standard color space (Rec.709).
  - **Creative LUT**: Apply stylistic look (cinematic, vintage, etc.).
- **How to use**:
  - Apply technical LUT first to get proper color space.
  - Then apply creative LUT for style.
  - Adjust intensity (opacity) to taste (usually 50-100%).
- **Where to get**:
  - Camera manufacturers (Canon, Sony, RED, Arri provide LUTs).
  - Free/paid packs online (CineStyle, ImpulZ, FilmConvert).
  - Create your own by grading one shot and saving as LUT.
- **Caution**: LUTs are not magic. They need proper exposure to work. Overuse looks cheap.

### 6. Popular Cinematic Looks
- **Teal & Orange**: Complementary colors. Shadows teal, highlights orange. Works well with skin tones.
- **High contrast**: Crushed blacks, bright highlights, saturated colors. Dramatic, intense.
- **Low contrast**: Flat, muted, desaturated. Dreamy, nostalgic, indie.
- **Vintage/Film**: Add grain, reduce saturation, shift colors (cyan shadows, warm highlights).
- **Cyberpunk**: Neon colors, high contrast, teal/magenta, vignette.
- **Black & White**: Remove color, adjust contrast curve. Classic, dramatic.
- **Desaturated**: Lower saturation 30-50%. Gritty, serious, documentary.
- **Warm**: Increase temperature, add orange/red tint. Nostalgic, cozy.
- **Cool**: Decrease temperature, add blue tint. Clinical, futuristic, sad.

### 7. Skin Tone Preservation
- **Skin tone line**: On vectorscope, skin tones cluster around I-line (upper right). Keep skin tones natural.
- **Use HSL secondary**: Isolate skin tones and protect them from heavy grading.
- **Avoid extreme color shifts on skin**: Don't make faces too green, purple, or blue.
- **Use mask**: Track face and apply different grade to skin if needed.
- **Check on different monitors**: Skin tones should look natural on phone, computer, TV.

### 8. Matching Shots
- **Use reference shot**: Grade one perfect shot, then match others to it.
- **Use waveform/vectorscope**: Compare scopes of shots. Match luminance and color distribution.
- **Color match tools**: Some software has auto-match (Premiere Lumetri Match Color, DaVinci Color Match).
- **Shoot with same settings**: Use same picture profile, white balance, ISO to minimize matching work.
- **Time of day**: Outdoor shots change color temperature throughout day. Match or embrace.

### 9. Color Spaces & Gamma
- **Color spaces**:
  - **Rec.709**: Standard HD video. Used for most delivery.
  - **Rec.2020**: Ultra HD. Wider gamut.
  - **sRGB**: Web/computer. Similar to Rec.709.
  - **DCI-P3**: Digital cinema. Wider than Rec.709.
- **Gamma curves**:
  - **Gamma 2.4**: Standard for digital cinema.
  - **Gamma 2.2**: Standard for computer displays.
  - **Log**: Flattened, low contrast. Needs grading to look normal.
- **Workflow**: Shoot log → apply LUT to convert to Rec.709 → grade → deliver in Rec.709 (unless HDR).

### 10. Delivery Considerations
- **Broadcast**: Strict color specs. Use broadcast safe filters.
- **Web**: Rec.709, sRGB. Slightly higher contrast/saturation looks good on phones.
- **HDR**: Wider color gamut (Rec.2020/P3), higher brightness. Different workflow.
- **Print**: Convert to sRGB for web, CMYK for print (different color space).

## Technical Guidelines

### Software Tools
- **DaVinci Resolve**: Industry standard. Free version powerful. Color page with scopes, qualifiers, power windows.
- **Premiere Pro**: Lumetri Color panel. Good for basic to intermediate.
- **After Effects**: Similar to Premiere. Good for motion graphics.
- **Final Cut Pro**: Color board or third-party plugins.
- **Lumetri Color**: Primary tool in Adobe ecosystem.

### Scopes (Essential for Accurate Grading)
- **Waveform**: Shows brightness distribution. Avoid clipping (0 or 100).
- **Vectorscope**: Shows color saturation and hue. Skin tones should be on I-line.
- **Parade**: RGB channels separately. Check for color balance.
- **Histogram**: Overall brightness distribution.

### Best Practices
- **Grade in full screen**: Not on small laptop screen.
- **Calibrate monitor**: Use colorimeter for accurate grading.
- **Work at proper brightness**: Room not too bright, monitor not too dim.
- **Use reference monitor**: If possible, grade on professional monitor.
- **Check on multiple devices**: Phone, tablet, TV to ensure it looks good everywhere.
- **Render at proper bit depth**: 10-bit or higher to avoid banding.

## Common Pitfalls to Avoid

- **Over-saturating**: Makes video look cheap and unnatural. Subtlety is key.
- **Crushing blacks too much**: Loses detail in shadows. Keep some shadow detail unless stylized.
- **Clipping highlights**: Blown-out whites look unprofessional.
- **Inconsistent color**: Shots that don't match break immersion. Match all shots.
- **Ignoring skin tones**: Faces look unnatural if heavily graded. Protect skin.
- **Using LUTs blindly**: LUTs are starting points, not final grades. Adjust after applying.
- **Grading in a bright room**: Ambient light affects perception. Grade in dim environment.
- **Not correcting first**: Grading uncorrected footage amplifies problems.
- **Too much contrast**: Can make video look harsh. Balance contrast with midtones.
- **Forgetting delivery specs**: Broadcast has different requirements than web.

## Advanced Techniques

### 1. Power Windows & Masks
- **Power window**: Localized adjustment (brighten face, darken background).
- **Types**: Circle, polygon, gradient, magic mask (AI-based).
- **Tracking**: Track moving subject so mask follows. Essential for moving shots.
- **Softness**: Feather edges to blend adjustment.

### 2. Qualifiers & HSL
- **HSL qualifier**: Select specific color range (skin, sky, product color).
- **Use**: Isolate and adjust only that color (make blues more cyan, greens more yellow).
- **Matte**: Refine selection with soften, blur, shrink/expand.
- **Multiple qualifiers**: Combine for complex selections.

### 3. Curves
- **RGB curves**: Precise control over contrast and color. Points on line adjust.
- **Luma curve**: Adjust brightness contrast (S-curve for contrast).
- **RGB curves separately**: Adjust color balance in shadows/midtones/highlights.
- **Hue vs hue/sat/luma**: Change specific hues, their saturation, or brightness.

### 4. Noise Reduction & Grain
- **Temporal NR**: Compare frames to reduce noise. Can cause smear if too strong.
- **Spatial NR**: Clean up single frame. Can soften image.
- **Add grain**: Match footage to film look. Control size, intensity, color.
- **Match grain**: Add grain to CG elements to blend with real footage.

### 5. Advanced LUT Techniques
- **Layer LUTs**: Apply multiple LUTs with different opacities.
- **Custom LUT creation**: Grade a shot perfectly, then export as LUT for batch use.
- **3D LUT vs 1D LUT**: 3D LUT more powerful (affects all three dimensions).
- **LUT stacking**: Technical LUT + Creative LUT + Adjustment LUT.

### 6. HDR Grading
- **Higher brightness**: Up to 1000+ nits. Use PQ/HLG transfer functions.
- **Wide color gamut**: Rec.2020 or P3. More saturated colors possible.
- **Tone mapping**: Convert HDR to SDR for delivery.
- **Separate grades**: Sometimes need different grade for HDR and SDR versions.

### 7. ACES Workflow
- **ACES**: Academy Color Encoding System. Industry standard.
- **Benefits**: Consistent color across different cameras and software.
- **Workflow**: Shoot in camera color space → transform to ACES → grade in ACES → output to delivery space.
- **Complex**: Requires understanding of IDTs, ODTs, RRTs.

### 8. Creative Effects
- **Bleach bypass**: Desaturate, increase contrast. Gritty, dramatic.
- **Day for night**: Underexpose, add blue tint, add highlights.
- **Vintage film**: Add grain, vignette, color shifts (cyan shadows, warm highlights).
- **Duotone**: Two-color gradient map. Stylized, graphic.
- **Solarization**: Invert tones above/below threshold. Surreal.

## Workflow Recommendations

1. **Organize footage**: Label by scene, shot type, camera angle.
2. **Create timeline**: Assemble rough cut with all shots.
3. **Normalize**: Apply basic correction to all shots (white balance, exposure).
4. **Match shots**: Use reference shot or color match tool to make all shots consistent.
5. **Primary grade**: Adjust shadows/midtones/highlights for overall look.
6. **Secondary grade**: Isolate and adjust specific colors or areas.
7. **Apply creative LUT**: Try different looks. Adjust opacity.
8. **Fine-tune**: Make small adjustments to perfect the look.
9. **Skin check**: Ensure all skin tones look natural.
10. **Scope check**: Verify no clipping, proper contrast, good color distribution.
11. **Render test**: Export short segment to check on different devices.
12. **Final render**: Export full video at proper settings.

## Related Skills

For complementary techniques, refer to:
- `./core-techniques/color-grading.md` (this file)
- `./core-techniques/color-grading.md`
- `./styles/cinematic.md` - Cinematic color palettes
- `./styles/dark-tutorial.md` - Clean, balanced color for tutorials
- `./styles/gameplay.md` - Vibrant, high-contrast color for gaming
- `./styles/dark-meme-dynamic.md` - Extreme saturation and contrast for memes

