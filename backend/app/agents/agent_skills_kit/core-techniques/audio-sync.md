---
name: audio-sync
description: Audio synchronization techniques for video editing including beat matching, dialogue mixing, and music alignment
metadata:
  tags: audio, sync, beat-matching, mixing, dialogue, music
---

## When to use

Use this skill whenever you need to synchronize audio elements with video, align cuts to music beats, mix dialogue with background music and sound effects, or create precise audio-video timing. This is fundamental for any video with music, voiceover, or sound effects that need to hit specific moments.

## Core Principles

### 1. Beat-Based Editing
- **Understanding beats**: Beats are the rhythmic pulses in music. Most music has a consistent BPM (beats per minute).
- **Finding beats**: Use the audio waveform to identify peaks (transients) which usually correspond to beats. Tap tempo manually if needed.
- **Cutting on beat**: Align video cuts to occur exactly on a beat for rhythmic satisfaction. This creates a "tight" feel.
- **Downbeat vs upbeat**: The downbeat (first beat of measure) is strongest. Important cuts should land on downbeats.
- **Beat grid**: Enable beat snapping in your editor to automatically align cuts to detected beats.

### 2. Dialogue & Music Balance
- **Ducking**: Automatically lower music volume when dialogue or important sound occurs. Use sidechain compression or manual keyframing.
- **Ducking depth**: Typically lower music by 6-12 dB during speech.
- **Ducking speed**: Attack should be fast (10-50ms) to avoid cutting in late. Release should be smooth (200-500ms) to avoid pumping.
- **Frequency separation**: Dialogue lives in mid frequencies (500Hz-2kHz). Music can be slightly reduced in this range to improve clarity.
- **Loudness standards**: Dialogue should be primary. Music should be background (-20 to -25 LUFS relative to dialogue).

### 3. Sound Effects Timing
- **On-beat SFX**: Sound effects should land exactly on video cuts or musical beats for maximum impact.
- **Pre-roll**: Sometimes a sound effect starts 0.1-0.2 seconds BEFORE the visual to create anticipation (like a whoosh before a whip pan).
- **Post-roll**: Let SFX ring out slightly after the visual for emphasis (0.2-0.5 seconds).
- **Layering**: Combine multiple SFX (e.g., whoosh + impact + whoosh) for richer sound.
- **Foley importance**: Realistic sound effects (footsteps, cloth rustle, object handling) add immersion even if subtle.

### 4. Audio Bridges & Transitions
- **J-cut**: Audio from next scene starts before video changes. Creates smooth forward momentum.
- **L-cut**: Video changes first, audio from previous scene continues. Creates continuity or emotional carryover.
- **Ambient continuity**: Maintain consistent room tone or ambient sound across cuts to smooth transitions.
- **Sound ramps**: Gradually increase or decrease audio (volume or pitch) to smooth scene changes.

### 5. Sync Techniques
- **Manual sync**: Align waveform peaks visually. Use clapperboard or hand clap for reference.
- **Timecode sync**: If you have timecode from multiple sources, they can auto-sync.
- **Waveform sync**: Use software to automatically align based on audio waveform similarity.
- **PluralEyes-style**: For multi-cam, sync by matching audio tracks from different cameras.

## Technical Guidelines

### Audio Specifications
- **Sample rate**: 48kHz standard for video. 44.1kHz acceptable for web.
- **Bit depth**: 24-bit for recording, 16-bit for delivery (unless high-res required).
- **Channels**: Stereo for most content. 5.1/7.1 for surround.
- **Loudness targets**:
  - YouTube: -14 LUFS integrated
  - TikTok/Reels: -14 to -16 LUFS
  - Broadcast: -23 LUFS (EBU R128)
  - Dialogue: -6 to -3 dB peak

### Tools & Effects
- **Waveform visualization**: Essential for seeing beats and transients.
- **Beat detection**: Software can auto-detect beats, but verify manually.
- **Time remapping**: Speed up/slow down audio without pitch change (using time-stretch algorithms).
- **Pitch shifting**: Change pitch without speed change, or vice versa.
- **Compression**: Control dynamic range. Fast attack for transients, slow release for sustain.
- **EQ**: Carve out space for different audio elements. Cut competing frequencies.
- **Reverb & delay**: Add space and depth. Use sparingly for dialogue.

### Sync Workflow
1. **Import all audio**: Music, dialogue, SFX on separate tracks.
2. **Normalize**: Ensure all dialogue clips are at similar volume.
3. **Add music**: Place music track first. Mark beat points.
4. **Edit to beat**: Cut video clips to align with music beats.
5. **Add dialogue**: Place voiceover. Use ducking to lower music during speech.
6. **Add SFX**: Place sound effects on key moments, aligned to beats or cuts.
7. **Ambient bed**: Add room tone or ambient sound to fill gaps.
8. **Mix**: Balance all levels. Use compression on master if needed.
9. **Loudness meter**: Check final loudness meets target.
10. **Export**: Render audio with video, or export stems.

## Common Pitfalls to Avoid

- **Off-beat cuts**: Cuts that don't align with music feel sloppy. Use beat grid.
- **Music too loud**: Dialogue should be clear. Music is background.
- **No ducking**: Music playing under dialogue makes speech unintelligible.
- **Inconsistent audio levels**: Some clips too quiet, others too loud. Normalize.
- **Missing ambient sound**: Dead air feels unnatural. Add room tone.
- **Poor SFX timing**: Sound effects that arrive late or early break immersion.
- **Clipping**: Audio exceeding 0 dB causes distortion. Leave headroom.
- **Wrong loudness**: Too quiet = viewers turn up, then loud music blasts. Too loud = distorted.
- **No audio bridges**: Abrupt audio changes are jarring. Use J-cuts/L-cuts.
- **Ignoring frequency clashes**: Multiple elements fighting in same frequency range create muddiness.

## Advanced Techniques

### 1. Advanced Beat Matching
- **Beat warping**: Stretch or compress audio to match a specific BPM without changing pitch.
- **Beat substitution**: Replace certain drum hits with different sounds while keeping rhythm.
- **Half-time/double-time**: Edit to every other beat (half-time) or double the beats (double-time) for different energy.
- **Polyrhythms**: Use multiple rhythmic patterns simultaneously for complex feel.

### 2. Dynamic Mixing
- **Automation**: Draw volume curves for precise control over time.
- **Multiband compression**: Compress different frequency bands separately.
- **Sidechain EQ**: Only duck music frequencies that clash with dialogue.
- **Parallel compression**: Blend compressed and uncompressed signals for punch.

### 3. Sound Design Integration
- **Layered SFX**: Combine 3-5 sounds for complex effects (e.g., explosion = deep boom + crackle + debris fall).
- **Foley artistry**: Record custom sound effects for unique quality.
- **Field recording**: Capture real-world sounds for authenticity.
- **Synthesis**: Create sounds from scratch using synthesizers.

### 4. Spatial Audio
- **Panning**: Place sounds in stereo field (left/right) for directionality.
- **3D audio**: Use binaural or ambisonic techniques for immersive experience.
- **Distance cues**: Reduce high frequencies and add reverb for distant sounds.
- **Doppler effect**: Pitch shift moving sounds as they pass by.

### 5. Audio Restoration
- **Noise reduction**: Remove hum, hiss, wind, etc.
- **De-reverberation**: Reduce room echo.
- **De-clipping**: Repair distorted audio.
- **Volume matching**: Make multiple clips sound like they were recorded together.

## Workflow Recommendations

1. **Organization**: Label all audio tracks clearly (Dialogue, Music, SFX, Ambience). Use color coding.
2. **Sync reference**: Choose one audio track as timebase (usually music or primary dialogue).
3. **Beat detection**: Run beat detection on music. Verify accuracy.
4. **Edit to beat**: Place video cuts on beat markers. Adjust as needed.
5. **Dialogue editing**: Clean up speech: remove mouth clicks, breaths, pauses. Compress.
6. **Music mixing**: Apply EQ, compression, limiting to music track.
7. **SFX placement**: Add sound effects on key moments. Sync to video cuts and music beats.
8. **Ducking setup**: Configure sidechain compression or draw automation.
9. **Ambient bed**: Add low-level room tone or ambient sound throughout.
10. **Final mix**: Balance all elements. Use loudness meter. A/B test on different speakers.

## Related Skills

For complementary techniques, refer to:
- `./core-techniques/pacing.md` - Rhythm and timing in editing
- `./core-techniques/sound-design.md` - Creating and manipulating sound effects
- `./core-techniques/transitions.md` - Audio transitions and crossfades
- `./styles/gameplay.md` - Game audio integration
- `./styles/dark-tutorial.md` - Voiceover recording and mixing
- `./styles/dark-meme-dynamic.md` - SFX-heavy meme editing

