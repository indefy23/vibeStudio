---
name: subtitles
description: Best practices for creating, positioning, and animating captions and subtitles in video
metadata:
  tags: subtitles, captions, text, accessibility, readability
---

## When to use

Use this skill whenever you need to add subtitles or captions to your video. This includes: dialogue subtitles for foreign language or hearing impaired, captions for social media (many watch without sound), karaoke-style lyrics, or any on-screen text that needs to be read while watching.

## Core Principles

### 1. Readability is Paramount
- **Font size**: Minimum 24pt for 1080p video. For mobile viewing (TikTok, Reels), use 32pt+.
- **Font choice**: Clean, sans-serif fonts (Arial, Helvetica, Roboto, Inter). Avoid decorative fonts for body text.
- **Contrast**: Text must stand out from background. Use:
  - Black text with white outline (stroke)
  - White text with black outline
  - Semi-transparent background box behind text
  - Text shadow (drop shadow)
- **Line length**: 35-50 characters per line maximum. Longer lines are hard to read quickly.
- **Line spacing**: 1.3-1.5x font size. Too tight = cramped, too loose = disconnected.
- **Text safe area**: Keep within 90% of frame (10% margin from edges).
- **Hold time**: Minimum 1.5 seconds for short subtitles, 2-3 seconds for longer. Rule: 1 second per 3-4 words.

### 2. Subtitle Types & Conventions
- **Closed captions (CC)**: Can be turned on/off. Include speaker identification, sound cues.
- **Open captions**: Burned into video. Always visible. Used for social media.
- **Subtitles**: Translation of dialogue. Usually just speech, no sound cues.
- **Forced narratives**: On-screen text that's part of the scene (signs, letters). Usually not subtitled.
- **SDH (Subtitles for the Deaf and Hard of Hearing)**: Include non-speech information (sound effects, music cues, speaker IDs).

### 3. Timing & Synchronization
- **In cue**: Subtitles appear slightly before speech starts (typically 0.2-0.5s).
- **Out cue**: Subtitles disappear slightly after speech ends (0.1-0.3s).
- **Reading speed**: Average person reads 2-3 words per second. Adjust for audience (children slower, adults faster).
- **Minimum duration**: Even a single word should stay on screen at least 0.8 seconds.
- **Maximum duration**: Single subtitle should not exceed 7 seconds (split long speeches).
- **Gap between subtitles**: Minimum 0.3 seconds between consecutive subtitles.
- **Synchronization**: Must match audio waveform exactly. Use transcript with timestamps.

### 4. Positioning
- **Standard position**: Bottom center, 3-5% from bottom edge.
- **Top position**: Used when bottom is obstructed (lower thirds, graphics).
- **Speaker identification**: If multiple speakers, position left/right to indicate who's talking.
- **Avoid covering important visuals**: Don't place over faces, text, or key action.
- **Consistent positioning**: Same type of subtitle should always be in same position.
- **Vertical text**: Some languages (Chinese, Japanese) may use vertical orientation.

### 5. Formatting Conventions
- **Speaker labels**: Use brackets or different color. Example: [JOHN] or (off-screen).
- **Sound cues**: Use parentheses or brackets. Example: (door slams), (music playing), (laughing).
- **Multiple speakers**: Use dashes or different colors to distinguish.
- **Foreign language**: Italicize when translated, or use different color.
- **Uncertain dialogue**: Use question marks or [inaudible].
- **Music lyrics**: Often karaoke-style (highlight current word).
- **Emphasis**: Bold or color for emphasis (use sparingly).

### 6. Technical Specifications
- **Character limit per line**: 32 characters (broadcast standard), 42 for streaming.
- **Lines per subtitle**: Maximum 2 lines (3 lines only if absolutely necessary).
- **Font**: Sans-serif, proportional. Minimum 24pt for 1080p.
- **Colors**:
  - **Primary**: White (#FFFFFF) or yellow (#FFFF00)
  - **Outline**: Black (#000000) or dark gray
  - **Background**: Semi-transparent black (0-80% opacity)
- **Outline width**: 1-2 pixels (or 1-2% of font size).
- **Background padding**: 1-2% of frame width around text.
- **Safe area**: Keep within title safe (90% of frame).

### 7. Localization & Languages
- **Text expansion**: German, Finnish, Russian are longer than English (plan for 30-50% expansion).
- **Text contraction**: Chinese, Japanese, Korean are shorter (plan for 30-50% reduction).
- **Right-to-left**: Arabic, Hebrew require RTL text direction.
- **Diacritics**: Ensure font supports accents (é, ü, ñ, etc.).
- **Character sets**: Some languages need special fonts (CJK, Arabic script).
- **Line breaking**: Different languages have different word-breaking rules.

### 8. Social Media Specific
- **Sound-off viewing**: 85% of Facebook videos, 40% of Instagram videos watched without sound. Subtitles essential.
- **Fast pacing**: TikTok/Reels need shorter subtitles, larger font, quicker timing.
- **Platform guidelines**: Each platform has specific subtitle recommendations (TikTok: larger, shorter).
- **Engagement**: Subtitles increase watch time and retention on social media.
- **Branding**: Can use brand colors for subtitles (but maintain readability).

### 9. Accessibility Best Practices
- **Hearing impaired**: Include all relevant audio information (speaker IDs, sound effects, music tone).
- **D/deaf**: Use proper terminology (capital D for cultural identity, lowercase d for medical condition).
- **Complex audio**: Multiple speakers, accents, background noise - provide clear subtitles.
- **Descriptive subtitles**: For important non-speech sounds that convey meaning.
- **Avoid**: All caps (harder to read), fancy fonts, low contrast, fast timing.

### 10. Quality Control
- **Proofread**: No spelling or grammar errors. Use spell check and human review.
- **Timing check**: Verify subtitles match audio exactly. No early/late.
- **Readability test**: Watch on small phone screen. Can read easily?
- **Duration check**: No subtitle too short or too long.
- **Overlap check**: No subtitles overlapping or too close together.
- **Position check**: No subtitles covering important visuals.
- **Consistency**: Same style throughout video (font, size, color, position).

## Technical Implementation

### Software Tools
- **Dedicated subtitling**: Aegisub, Subtitle Edit, Subtitle Workshop.
- **Video editors**: Premiere Pro (captions panel), DaVinci Resolve (subtitles page), Final Cut Pro.
- **Motion graphics**: After Effects (subtitles templates).
- **Online services**: Rev.com, SubtitleHorse, Kapwing.
- **AI tools**: Auto-transcription (Premiere, DaVinci, Descript) but always review.

### File Formats
- **SubRip (.srt)**: Most common. Plain text with timecodes.
- **WebVTT (.vtt)**: Web standard. Slightly different format.
- **Scenarist (.scc)**: Broadcast closed captions.
- **STL, CAP, PAC**: Various broadcast formats.
- **Embedded**: Burned into video (open captions).
- **Sidecar**: Separate file (closed captions).

### SRT Format Example
```
1
00:00:01,000 --> 00:00:04,000
This is the first subtitle line.

2
00:00:04,500 --> 00:00:08,000
This is the second subtitle line.
```
- Timecode format: HH:MM:SS,mmm (comma for milliseconds).
- Duration format: start --> end (arrow with spaces).
- Blank line between subtitles.
- Number each subtitle sequentially.

### Workflow
1. **Transcription**: Get accurate transcript of dialogue.
2. **Segmentation**: Break transcript into subtitle chunks (by sentence or phrase).
3. **Timing**: Assign in/out times to each chunk based on audio.
4. **Positioning**: Determine where on screen each subtitle goes.
5. **Formatting**: Apply font, color, outline, background.
6. **Review**: Watch video with subtitles. Check timing, readability, overlap.
7. **Export**: Export in required format (SRT, VTT, burn in).
8. **QC**: Final quality check on multiple devices.

## Common Pitfalls to Avoid

- **Text too small**: Unreadable on mobile. Test on phone.
- **Poor contrast**: Text blends into background. Add outline/background.
- **Too much text on screen**: More than 2 lines or long lines. Split.
- **Timing too fast**: Viewers can't keep up. Extend duration.
- **Timing too slow**: Subtitles lag behind speech. Sync properly.
- **Inconsistent style**: Different fonts/colors throughout. Establish style guide.
- **Covering important visuals**: Text over faces or key action. Reposition.
- **Spelling/grammar errors**: Unprofessional. Proofread.
- **No sound cues for hearing impaired**: Missing important audio information. Add.
- **All caps**: Harder to read than sentence case. Use sparingly.
- **Fancy fonts**: Decorative fonts reduce readability. Use simple fonts.
- **Too close to edge**: Text gets cut off on some screens. Use safe area.
- **No background on busy video**: Text disappears into complex background. Add box.
- **Overlapping subtitles**: Two subtitles on screen at once. Adjust timing.
- **Long gaps**: No subtitles for long periods when audio is present. Fill gaps.

## Advanced Techniques

### 1. Styling & Animation
- **Animated subtitles**: Text slides, fades, or types in. Use sparingly for emphasis.
- **Highlight current word**: Karaoke style - current word highlighted as spoken.
- **Color coding**: Different colors for different speakers.
- **Position animation**: Subtitles move to avoid covering visuals.
- **Background animation**: Subtle animated background behind text.
- **Emoji integration**: Add relevant emojis to convey tone.

### 2. Advanced Timing
- **Scene change detection**: Avoid subtitles crossing scene cuts.
- **Shot change detection**: Adjust timing if shot changes mid-subtitle.
- **Audio-based timing**: Use speech detection algorithms for auto-timing.
- **Reading speed adjustment**: Customize based on target audience (children, elderly).
- **Gap optimization**: Smart gaps between subtitles for natural reading.

### 3. Quality Automation
- **Line length checking**: Auto-flag lines that exceed character limit.
- **Duration checking**: Auto-flag subtitles too short or too long.
- **Reading speed calculation**: Auto-calculate words per second.
- **Overlap detection**: Auto-detect overlapping subtitles.
- **Profanity filtering**: Auto-censor or flag inappropriate content.
- **Language detection**: Verify subtitle language matches audio.

### 4. Multi-language Workflows
- **Translation memory**: Reuse previously translated segments.
- **Subtitle alignment**: Align subtitles across multiple language versions.
- **Quality assurance**: Check translated subtitles for timing and readability.
- **Localization testing**: Test subtitles on devices from target region.
- **Character expansion handling**: Auto-adjust timing for longer/shorter languages.

### 5. Accessibility Enhancements
- **Audio description integration**: Coordinate with AD narration.
- **Sign language overlay**: Position subtitles to not overlap sign language interpreter.
- **High contrast mode**: Special mode for low-vision viewers.
- **Font scaling**: Allow viewer to adjust subtitle size (in player).
- **Background opacity control**: Let viewer adjust text background.
- **Colorblind-friendly palettes**: Avoid red-green combinations.

## Related Skills

For complementary techniques, refer to:
- `./core-techniques/text-animation.md` - Text animation principles that apply to subtitles
- `./core-techniques/audio-sync.md` - Synchronizing subtitles to audio
- `./core-techniques/pacing.md` - How subtitle timing affects video pacing
- `./styles/dark-tutorial.md` - Subtitles in tutorial videos
- `./styles/dark-meme-dynamic.md` - Fast, flashy subtitles for memes
- `./styles/tiktok-news-hype.md` - Punchy subtitles for news content

