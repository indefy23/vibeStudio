---
name: audio
description: Audio handling in video editing including importing, trimming, volume, speed, pitch, and mixing
metadata:
  tags: audio, sound, music, volume, speed, pitch, mixing
---

## When to use

Use this skill whenever you need to work with audio files in your video project - importing music, sound effects, voiceovers; trimming and editing audio; adjusting volume, speed, and pitch; and mixing multiple audio tracks together.

## Core Principles

### 1. Audio Types & Roles
- **Dialogue**: Spoken words. Primary audio. Must be clear and intelligible.
- **Music**: Emotional underscore. Sets mood, fills gaps, enhances emotion.
- **Sound Effects (SFX)**: Emphasize visual events. Add impact and realism.
- **Ambience**: Background bed. Establishes location and fills silence.
- **Foley**: Recorded realistic sounds of actions. Grounds reality.

### 2. Importing Audio
- **Supported formats**: MP3, WAV, AIFF, M4A, OGG, FLAC.
- **Sample rate**: Match project settings (usually 48kHz for video).
- **Bit depth**: 16-bit for delivery, 24-bit for recording.
- **Channels**: Mono or stereo. Mono for dialogue, stereo for music/SFX.
- **File organization**: Name clearly, organize in bins/folders by type.
- **Linking vs embedding**: Link to external files to save project size, but keep files accessible.

### 3. Trimming & Editing Audio
- **In/Out points**: Set where audio starts and ends in timeline.
- **Razor/split**: Cut audio at specific points.
- **Fade in/out**: Gradual volume increase/decrease at edges.
  - **Fade shape**: Linear, exponential, logarithmic. Exponential most natural.
  - **Fade duration**: 0.5-2 seconds typical. Shorter for punchy sounds.
- **Crossfade**: Overlap two audio clips with fading.
  - **Equal power**: Constant perceived volume. Good for music.
  - **Constant power**: Smooth transition. Default in many editors.
- **Looping**: Repeat audio to fill duration. Ensure seamless loop points.
- **Time stretching**: Change duration without changing pitch (or vice versa).
- **Pitch shifting**: Change pitch without changing speed (or vice versa).

### 4. Volume & Gain
- **Gain**: Input level (before processing). Adjust clip gain.
- **Volume**: Output level (after processing). Adjust track volume or clip volume.
- **Decibels (dB)**:
  - **0 dBFS**: Maximum digital level (clipping). Never exceed.
  - **-6 dB**: Strong signal, safe headroom.
  - **-12 dB**: Moderate level.
  - **-20 dB**: Quiet level.
- **Normalization**: Raise entire clip to target level without clipping.
- **Keyframing volume**: Animate volume over time for fades, ducking, emphasis.
- **Volume automation**: Draw volume curves on timeline.

### 5. Audio Effects & Processing
- **EQ (Equalization)**:
  - **High-pass filter**: Remove low frequencies (<80Hz). Clean rumble.
  - **Low-pass filter**: Remove high frequencies (>12kHz). Muffle/distant effect.
  - **Band EQ**: Boost/cut specific frequencies.
  - **Parametric EQ**: Precise frequency, Q, gain control.
- **Compression**:
  - **Purpose**: Reduce dynamic range (difference between quietest and loudest).
  - **Threshold**: Level above which compression starts.
  - **Ratio**: How much compression (2:1 mild, 4:1 moderate, 10:1 heavy).
  - **Attack**: How fast compressor engages (fast 1-5ms for transients, slow 10-50ms for sustain).
  - **Release**: How fast compressor disengages (50-200ms typical).
  - **Makeup gain**: Boost after compression to restore level.
  - **Use**: Dialogue (smooth levels), music (punch), SFX (control peaks).
- **Reverb**: Add space/echo.
  - **Types**: Room, hall, plate, spring, cathedral.
  - **Parameters**: Decay, pre-delay, wet/dry mix, damping.
  - **Use sparingly**: Too much reverb makes audio muddy.
- **Delay/Echo**: Repeat sound after delay.
  - **Delay time**: Milliseconds between repeats.
  - **Feedback**: How many repeats.
  - **Mix**: Wet/dry balance.
- **Distortion/Saturation**: Add harmonics, warmth, grit.
  - **Soft clipping**: Gentle saturation (tape saturation).
  - **Hard clipping**: Aggressive distortion.
- **Noise reduction**: Remove hiss, hum, wind, clicks.
  - **Spectral editing**: Visual removal of noise.
  - **Noise profile**: Sample noise and subtract.
- **Pitch shifting**: Change pitch without speed change.
- **Time stretching**: Change speed without pitch change.
- **Modulation**: Chorus, flanger, phaser for movement.

### 6. Mixing Multiple Tracks
- **Track hierarchy**:
  - **Dialogue**: Highest priority. -6 to -3 dB peak.
  - **Music**: Lower than dialogue. -18 to -12 dB.
  - **SFX**: Variable, but usually between dialogue and music.
  - **Ambience**: Very low, -40 to -30 dB.
- **Panning**: Place sounds in stereo field (left/right).
- **Balance**: Adjust relative volumes of tracks.
- **Mute/solo**: Isolate tracks for troubleshooting.
- **Grouping**: Combine tracks for collective processing.
- **Send/return**: Send audio to effect track (reverb bus) to save CPU.

### 7. Audio Sync & Timing
- **Sync to video**: Audio must match picture exactly.
- **Sync to music**: Cuts, effects, animations should land on beats.
- **J-cut**: Audio from next scene starts before video.
- **L-cut**: Video changes first, audio from previous continues.
- **Audio bridges**: Sound that spans transition (door slam continues).
- **Beat detection**: Use beat markers to align audio and video.

### 8. Loudness & Delivery
- **Loudness standards**:
  - **YouTube**: -14 LUFS integrated.
  - **TikTok/Reels**: -14 to -16 LUFS.
  - **Broadcast**: -23 LUFS (EBU R128).
  - **Cinema**: -20 to -24 LUFS.
- **True peak**: Ensure no samples exceed 0 dBFS. Use true peak limiter.
- **Normalization**: Adjust overall level to target loudness.
- **Mono compatibility**: Check phase issues when summed to mono.

## Technical Guidelines

### Software Tools
- **Video editors**: Premiere Pro, DaVinci Resolve, Final Cut Pro.
- **DAWs**: Pro Tools, Reaper, Logic, Ableton, FL Studio.
- **Audio repair**: iZotope RX, Acon Digital Restoration.
- **Meters**: Loudness meters (Youlean, iZotope Insight).

### Best Practices
- **Record quality**: Good source audio is easier than fixing bad audio.
- **Use headphones**: Monitor audio accurately.
- **Check on multiple systems**: Phone speakers, laptop, headphones.
- **Leave headroom**: Don't peak at 0 dB. Leave -3 dB margin.
- **Organize tracks**: Color code, label clearly.
- **Use sub-mixes**: Group similar tracks (all dialogue, all music).
- **Reference tracks**: Compare your mix to professional content.
- **Take breaks**: Ears fatigue. Rest and come back.

## Common Pitfalls to Avoid

- **Clipping**: Distortion from peaks over 0 dB. Leave headroom.
- **Dialogue unintelligible**: Most important. If can't understand speech, fail.
- **Music too loud**: Should never compete with dialogue. Duck properly.
- **No ambience**: Dead air feels unnatural. Add room tone.
- **Poor sync**: Audio doesn't match picture. Fix with nudge.
- **Inconsistent levels**: Some clips loud, others quiet. Normalize/compress.
- **Mono compatibility**: Phase issues cause cancellation in mono. Check.
- **Noisy audio**: Hiss, hum, rumble. Clean up with NR.
- **Over-processing**: Too much compression, reverb, EQ. Less is more.
- **Ignoring loudness standards**: Too quiet or too loud for platform.

## Advanced Techniques

### 1. Advanced Mixing
- **Parallel compression**: Blend compressed and uncompressed signals.
- **Sidechain compression**: Duck music when dialogue present.
- **Multiband compression**: Compress different frequency bands separately.
- **Dynamic EQ**: EQ that changes based on level.
- **Automation**: Precise volume/pan/effect changes over time.
- **Stem mixing**: Mix groups separately then combine.

### 2. Sound Design Integration
- **Layering**: Combine multiple sounds for richness.
- **Frequency separation**: Each layer occupies different frequency range.
- **Spatial placement**: Pan and use reverb to place sounds in 3D space.
- **Processing chains**: Multiple effects in series/parallel.

### 3. Restoration & Repair
- **Spectral editing**: Visually remove unwanted sounds.
- **De-hum**: Remove electrical hum (50/60Hz and harmonics).
- **De-click**: Remove clicks, pops, crackles.
- **De-reverb**: Reduce room echo.
- **De-clip**: Repair distorted audio from clipping.
- **Mouth click removal**: Remove lip smacks and clicks.

### 4. Advanced Editing
- **Elastic audio**: Time-stretch without pitch change (or vice versa).
- **Varispeed**: Change speed and pitch together (tape effect).
- **Conform to tempo**: Match audio to specific BPM.
- **Beat mapping**: Align audio to beat grid.
- **Crossfade shapes**: Custom fade curves.

### 5. Surround & 3D Audio
- **5.1/7.1 mixing**: Assign tracks to surround channels.
- **Ambisonics**: Full-sphere 3D audio.
- **Binaural**: 3D audio for headphones.
- **Object-based audio**: Dolby Atmos.

## Workflow Recommendations

1. **Organize**: Create tracks: Dialogue, Music, SFX, Ambience, Foley. Color code.
2. **Import**: Bring all audio files into project. Label clearly.
3. **Sync**: Ensure all audio matches video. Use clap or timecode if available.
4. **Clean dialogue**: Remove noise, mouth clicks, breaths. Compress.
5. **Add music**: Place music track. Adjust level to leave space for dialogue.
6. **Add ambience**: Low-level bed. Fill gaps.
7. **Add SFX**: For visual events. Layer as needed.
8. **Add Foley**: For actions. Sync precisely.
9. **Process**: Apply EQ, compression, reverb to each element.
10. **Mix**: Balance all levels. Use automation.
11. **Loudness**: Measure LUFS. Adjust to target.
12. **Final check**: Listen on multiple systems. Fix any issues.
13. **Export**: Render final audio with video or as stems.

## Related Skills

For complementary techniques, refer to:
- `./core-techniques/audio-sync.md` - Synchronizing audio to video and beats
- `./core-techniques/sound-design.md` - Advanced sound design techniques
- `./core-techniques/pacing.md` - How audio affects pacing
- `./styles/cinematic.md` - Subtle, realistic audio for film
- `./styles/gameplay.md` - Game audio integration
- `./styles/dark-meme-dynamic.md` - SFX-heavy, punchy audio
- `./styles/tiktok-news-hype.md` - Beat-synced, high-energy audio

