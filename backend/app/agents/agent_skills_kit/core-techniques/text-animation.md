---
name: text-animation
description: Kinetic typography and animated text techniques for video including reveal effects, motion, and readability
metadata:
  tags: text, animation, typography, kinetic, motion-graphics, titles
---

## When to use

Use this skill whenever you need to animate text in your video - titles, lower thirds, captions, call-to-actions, or any on-screen text. Animated text captures attention, emphasizes key points, and enhances storytelling when done correctly. Poor text animation, however, can make content unprofessional and hard to read.

## Core Principles

### 1. Readability First
- **Text must be readable at all times**: If animation makes text hard to read, it's a failure.
- **Adequate size**: Text should be large enough to read on small screens (minimum 24pt for body, 48pt+ for headlines on 1080p).
- **Sufficient contrast**: Text must stand out from background. Use shadows, outlines, or background boxes if needed.
- **Hold time**: Text should remain on screen long enough to be read. Rule of thumb: 1 second per 3-4 words minimum.
- **Simple fonts**: Use clean, legible fonts for body text. Fancy fonts only for short headlines.
- **Avoid excessive motion**: Text that moves too much or too frequently causes eye strain.

### 2. Text Animation Categories
- **Entrance animations**: How text appears on screen.
  - **Fade In**: Simple opacity fade. Elegant, subtle.
  - **Slide/Translate**: Text moves into position from off-screen.
  - **Scale/Pop**: Text grows from small to full size. Energetic.
  - **Typewriter**: Characters appear one by one. Classic, emphasizes each word.
  - **Reveal mask**: Text is masked and mask animates open.
  - **Glitch**: Digital distortion reveal. Tech/hacker aesthetic.
  - **Blur In**: Text starts blurry and sharpens.

- **Hold/Idle**: Text remains on screen with subtle motion.
  - **Subtle bounce**: Very slight up/down float.
  - **Breathing**: Slight scale or opacity pulse.
  - **Static**: No motion. Sometimes best.
  - **Background movement**: Text stays still while background moves.

- **Exit animations**: How text leaves screen.
  - **Fade Out**: Simple opacity fade.
  - **Slide out**: Text moves off screen.
  - **Scale down**: Text shrinks away.
  - **Blur out**: Text becomes blurry then disappears.
  - **Disintegrate**: Text breaks apart or dissolves.
  - **No exit**: Text just disappears (cut). Can be jarring but sometimes appropriate.

- **On-hold animations**: Text animates while visible.
  - **Word-by-word**: Each word animates separately.
  - **Letter-by-letter**: Each character animates. Good for emphasis.
  - **Highlight**: Underline or color change on specific words.
  - **Bounce/Shake**: Attention-grabbing for key phrases.
  - **Path animation**: Text follows a curved path.

### 3. Timing & Duration
- **Entrance duration**: 0.3-0.8 seconds for most animations. Longer (1-2s) for dramatic reveals.
- **Hold duration**: Text should stay on screen at least 2-3 seconds after entrance before exiting or changing.
- **Exit duration**: 0.2-0.5 seconds. Usually faster than entrance.
- **Total on-screen time**: Minimum 3-5 seconds for short phrases, 1 second per word for longer text.
- **Staggering**: For multi-line or multi-element text, animate elements with 0.1-0.2 second delays.
- **Sync to audio**: Text animations should align with voiceover or sound effects. Text appears when word is spoken.

### 4. Text Hierarchy & Layout
- **Primary text**: Headlines, main messages. Largest font, most animation.
- **Secondary text**: Supporting info, subtitles. Smaller, simpler animation.
- **Tertiary text**: Captions, labels. Smallest, minimal or no animation.
- **Positioning**:
  - **Lower third**: Bottom 1/3 of screen. Standard for names/titles.
  - **Center**: Main headlines, calls-to-action.
  - **Top**: Titles, chapter headings.
  - **Avoid center for long text**: Hard to read over action.
- **Text safe area**: Keep text within title safe margins (10% from edges).
- **Line length**: 30-50 characters per line maximum for readability.
- **Line spacing**: 1.2-1.5x font size for body, tighter for headlines.

### 5. Animation Principles for Text
- **Easing**: Use ease-out for entrances (fast start, slow end), ease-in for exits (slow start, fast end).
- **Anticipation**: Text can slightly shrink or move back before appearing (preload).
- **Follow-through**: Text can overshoot final position and settle back.
- **Arcs**: Text should move on curved paths, not straight lines, for organic feel.
- **Squash & stretch**: Can apply to text for playful effect (scale X vs Y differently).
- **Exaggeration**: Make entrance/exit more dramatic than you think necessary.

### 6. Kinetic Typography Techniques
- **Word isolation**: Animate key words differently (color, size, motion) to emphasize.
- **Text as visual element**: Text can be part of scene, interacting with objects (behind, in front, masked by).
- **Text transformation**: Text changes shape, color, or font during animation.
- **Text path**: Text follows a motion path (curve, wave, circle).
- **Text reveal**: Text is hidden initially (mask, opacity) and revealed progressively.
- **Text reaction**: Text responds to audio (pulses with beat, reacts to voice).
- **3D text**: Text with depth (extrusion, bevel) for cinematic titles.
- **Text particles**: Text explodes into particles or assembles from particles.

### 7. Synchronization
- **Voiceover sync**: Text should appear exactly when word is spoken. Use transcript timing.
- **Music beat sync**: Text animations should land on musical beats for impact.
- **Sound effect sync**: Text reveal accompanied by sound effect (whoosh, pop, click).
- **On-screen action sync**: Text appears when relevant visual happens.
- **Pacing**: Text animation speed should match video pacing (fast for hype, slow for drama).

### 8. Style-Specific Text Animation
- **Cinematic**: Subtle fades, smooth slides, elegant serif fonts, minimal motion.
- **Hype/TikTok**: Pop-in effects, glitch text, bold sans-serif, fast timing (0.2-0.4s).
- **Corporate**: Clean slides, professional fonts, consistent branding colors.
- **Comedy**: Bouncy animations, exaggerated effects, playful fonts.
- **Tech/Cyberpunk**: Glitch, decode, matrix-style, monospace fonts, neon colors.
- **Educational**: Clear fades, simple slides, high contrast, no distracting motion.
- **Gaming**: Dynamic motion, game UI elements, pixel fonts, effects that feel interactive.

## Technical Guidelines

### Software & Tools
- **Keyframing**: Animate position, scale, rotation, opacity, anchor point.
- **Text animators**: Pre-built text animation presets (per character/word/line).
- **Expressions**: Use expressions for procedural text animation (wiggle, time, loop).
- **Masks & track mattes**: Reveal text through shapes or other layers.
- **Shape layers**: Create custom text backgrounds, underlines, highlights.
- **Pre-compositions**: Complex text animations should be pre-comped for reuse.

### Fonts & Typography
- **Font licensing**: Ensure you have rights to use fonts in video (embedding rights).
- **Variable fonts**: Use weight/width/optical size axes for dynamic text.
- **Text rendering**: Use high-quality anti-aliasing (not pixelated).
- **Fallback fonts**: Have backup fonts in case primary doesn't support certain characters.
- **Text alignment**: Left-align for body, center for headlines, right for technical info.

### Performance
- **Text layers**: Many text layers can slow down preview. Pre-render complex animations.
- **Font caching**: First render of each font is slow. Pre-warm by rendering once.
- **Vector vs bitmap**: Vector text scales cleanly but can be slower. Bitmap text faster but pixelates when scaled.
- **Simplify**: Avoid excessive effects on text (blur, glow, shadow) if not needed.

### Export Considerations
- **Text safety**: Keep text within title safe area (90% of frame).
- **Readability on small screens**: Test on phone. Text should be legible at 25% size.
- **Closed captions**: If providing captions, ensure they don't conflict with on-screen text.
- **Multiple languages**: Text length varies by language. Design for expansion (German longer than English).

## Common Pitfalls to Avoid

- **Text too small**: Unreadable on mobile. Test on phone.
- **Poor contrast**: Text blends into background. Add outline/shadow/background.
- **Too much motion**: Text flying everywhere distracts from message.
- **Animation too fast**: Viewer can't read before text changes.
- **Animation too slow**: Viewer gets bored waiting for text to finish.
- **Inconsistent style**: Different fonts, sizes, or animations throughout. Establish style guide.
- **Overusing effects**: Drop shadows, glows, strokes on everything looks cheap.
- **Poor timing**: Text appears too early or too late relative to audio/action.
- **Center-align long paragraphs**: Hard to read. Use left-align for body text.
- **Fancy fonts for body text**: Decorative fonts reduce readability. Use simple fonts for long text.
- **Text going off-screen**: Ensure text stays within frame boundaries.
- **No hold time**: Text appears and immediately disappears. Give viewer time to read.
- **Ignoring hierarchy**: All text same size/color. Use hierarchy to guide attention.
- **Forgetting accessibility**: Low vision users need high contrast and adequate size.

## Advanced Techniques

### 1. Text on Path
- **Path following**: Text follows a curved or custom path.
- **Path animation**: The path itself can animate (draw itself, move).
- **Reverse path**: Text can follow path backwards.
- **Per-character**: Each character follows path independently for organic feel.

### 2. Text Deformation
- **Bend/Arch**: Curve text along arc.
- **Wave**: Sine wave distortion.
- **Bulge/Pinch**: Spherize or pinch text.
- **Displacement**: Use map to distort text.
- **3D extrusion**: Give text depth with bevel and extrusion.

### 3. Text Particle Systems
- **Text to particles**: Text explodes into particles.
- **Particles to text**: Particles assemble into text.
- **Particle text**: Text composed entirely of particles that move.
- **Text trails**: Text leaves particle trail as it moves.

### 4. Advanced Reveal Techniques
- **Stroke reveal**: Text outline draws itself, then fills.
- **Clip-path reveal**: Text is clipped by animated shape.
- **Glitch decode**: Text appears with random characters before settling.
- **Typewriter with errors**: Simulates typing with backspaces and corrections.
- **Handwriting**: Text draws itself as if written by hand.
- **Liquid fill**: Text fills with liquid color.

### 5. Text Interaction with Scene
- **Text in 3D space**: Text exists in 3D with camera movement.
- **Text occlusion**: Objects pass in front of text, text passes behind objects.
- **Text shadows**: Dynamic shadows that respond to light sources.
- **Text reflection**: Text reflects on surfaces below.
- **Text as mask**: Text used as alpha channel to reveal video underneath.

### 6. Data-Driven Text
- **Dynamic text**: Text content changes based on data (scores, numbers, names).
- **Counters**: Animated numbers counting up/down.
- **Date/time**: Real-time clocks or countdown timers.
- **Variable substitution**: Template text with placeholders filled dynamically.

### 7. Text Synchronization Techniques
- **Audio reactivity**: Text scales/bounces with audio amplitude.
- **Beat sync**: Text changes on musical beats.
- **Phoneme sync**: Text animates to speech phonemes (mouth shapes).
- **Word-by-word highlight**: Current spoken word highlighted.
- **Karaoke style**: Text fills as word is spoken.

### 8. Performance Optimization
- **Pre-render text animations**: Complex text animations can be pre-rendered as alpha channel video.
- **Use text presets**: Save custom text animations as presets for reuse.
- **Cache text layers**: Enable caching in After Effects for text-heavy comps.
- **Simplify expressions**: Complex text expressions can slow down. Use simpler alternatives.

## Workflow Recommendations

1. **Plan**: Determine what text is needed (headlines, captions, lower thirds) and when they appear.
2. **Script timing**: If voiceover exists, get transcript with timestamps. Align text to speech.
3. **Design style**: Choose font, color, size, and animation style. Create style guide.
4. **Create text layers**: Add all text to composition. Position correctly.
5. **Pre-animate**: Set text to final state (fully visible, correct position).
6. **Animate entrance**: Add keyframes or presets for entrance. Time to audio/beat.
7. **Animate exit**: Add exit animation if text leaves screen.
8. **Add idle motion**: Subtle motion while text is visible (optional).
9. **Sync to audio**: Fine-tune timing to match voiceover or music.
10. **Review readability**: Watch on small screen. Is text readable? Adjust size/contrast.
11. **Consistency check**: Ensure all text throughout video follows same style.
12. **Render test**: Export segment to verify text looks correct on different devices.

## Related Skills

For complementary techniques, refer to:
- `./core-techniques/animation.md` - General animation principles that apply to text
- `./core-techniques/audio-sync.md` - Syncing text to audio
- `./core-techniques/pacing.md` - Text timing and rhythm
- `./styles/cinematic.md` - Subtle, elegant text for film
- `./styles/dark-tutorial.md` - Clear, readable text for tutorials
- `./styles/dark-meme-dynamic.md` - Fast, flashy text for memes
- `./styles/tiktok-news-hype.md` - Punchy text animations for news

