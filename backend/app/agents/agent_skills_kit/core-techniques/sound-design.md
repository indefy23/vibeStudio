---
name: sound-design
description: Sound design techniques for video including Foley, ambience, effects, and immersive audio mixing
metadata:
  tags: sound, design, Foley, ambience, SFX, mixing, audio
---

## When to use

Use this skill whenever you need to create or enhance the audio landscape of your video beyond just music and dialogue. Sound design includes adding sound effects (SFX), Foley (recorded everyday sounds), ambient/background audio, and using audio techniques to create immersion, depth, and emotional impact. It's what makes viewers feel like they're in the scene.

## Core Principles

### 1. What is Sound Design?
- **Definition**: The process of creating, selecting, and manipulating audio elements to support the visual narrative and evoke emotion.
- **Components**:
  - **Dialogue**: Spoken words (primary audio).
  - **Music**: Emotional underscore, theme, background.
  - **Sound Effects (SFX)**: Artificial or exaggerated sounds (explosions, whooshes, UI beeps).
  - **Foley**: Realistic recorded sounds of everyday actions (footsteps, cloth rustle, door handles).
  - **Ambience/Atmosphere**: Background bed that establishes space (room tone, wind, city noise).
- **Goal**: Create an immersive audio experience that feels real (or intentionally stylized) and supports the story.

### 2. The Sound Design Hierarchy
- **Dialogue is king**: Always prioritize clarity of speech. Everything else supports it.
- **Music sets mood**: Provides emotional context.
- **Foley grounds reality**: Makes actions feel tangible and authentic.
- **SFX emphasize moments**: Highlight important visual events.
- **Ambience fills space**: Creates sense of location and continuity.

### 3. Foley - The Art of Realistic Sound
- **What is Foley**: Recording everyday sounds in sync with picture (footsteps, clothing, props).
- **Foley categories**:
  - **Feet**: Footsteps on different surfaces (concrete, wood, carpet).
  - **Clothes**: Rustling fabric, zippers, buttons.
  - **Props**: Handling objects (keys, phones, tools).
  - **Specific**: Unique sounds (sword swing, glass break, paper crumple).
- **Foley performance**: Watch the picture and perform actions in time. Record multiple variations.
- **Foley editing**: Sync precisely to picture. Clean up noise. Normalize levels.
- **Foley mixing**: Balance with other audio. Usually lower than dialogue but present.

### 4. Sound Effects (SFX)
- **Types**:
  - **Realistic**: Actual recordings of real sounds (gunshot, car engine).
  - **Exaggerated**: Enhanced or created sounds for impact (larger-than-life punches, cartoon boings).
  - **Designed**: Completely synthetic or manipulated sounds (lasers, magic, UI sounds).
- **SFX libraries**: Use royalty-free libraries (Boom Library, SoundMorph, freesound.org).
- **Layering**: Combine multiple SFX for richness (e.g., explosion = deep boom + crackle + debris fall).
- **Processing**: Apply EQ, reverb, pitch shift, distortion to shape SFX.

### 5. Ambience & Atmosphere
- **Purpose**: Fill silence, establish location, provide continuity between shots.
- **Types**:
  - **Room tone**: The sound of a silent room. Essential to fill gaps.
  - **Location ambience**: City street, forest, office, cafe.
  - **Weather**: Rain, wind, thunder.
  - **Crowd beds**: Distant chatter, applause, murmurs.
- **Layering**: Combine multiple ambience tracks for depth (foreground + background).
- **Looping**: Ambience should loop seamlessly. Use crossfades at loop points.
- **Level**: Low volume (-40 to -30 dBFS). Should be felt, not noticed.

### 6. Spatial Audio & Panning
- **Stereo field**: Place sounds in left/right spectrum for directionality.
- **Panning rules**:
  - **On-screen left**: Pan left (-50 to -100).
  - **On-screen right**: Pan right (+50 to +100).
  - **Center**: Pan 0 (dialogue usually center).
  - **Off-screen**: Pan extreme or use reverb to indicate distance.
- **Distance cues**:
  - **Volume**: Distant sounds are quieter.
  - **High-frequency roll-off**: Distant sounds lose highs (use low-pass filter).
  - **Reverb**: Distant sounds have more reverb/echo.
  - **Muffled**: Reduce clarity for far sounds.
- **3D audio**: Use surround formats (5.1, 7.1) or binaural for immersive experiences.

### 7. Reverb & Space
- **Reverb types**: Room, hall, plate, spring, cathedral, outdoor.
- **Reverb parameters**:
  - **Decay time**: How long reverb lasts. Short for small rooms, long for large spaces.
  - **Pre-delay**: Time before reverb starts. Creates separation.
  - **Wet/dry mix**: Balance between original and reverberant sound.
  - **Damping**: High-frequency absorption. Softer reverb.
- **Use reverb to**:
  - Place sounds in same space (match reverb on all audio).
  - Create depth (more reverb = farther away).
  - Add atmosphere and mood.
- **Avoid reverb on dialogue**: Usually keep dialogue dry (no reverb) for clarity, unless stylized.

### 8. Audio Processing
- **EQ (Equalization)**:
  - **High-pass filter**: Remove rumble (<80Hz). Apply to most non-bass sounds.
  - **Low-pass filter**: Remove harsh highs (>12kHz). Use for distant/muffled effects.
  - **Band EQ**: Boost/cut specific frequencies to shape tone.
  - **Dialogue EQ**: Cut 200-400Hz (mud), boost 2-5kHz (clarity).
- **Compression**:
  - **Purpose**: Control dynamic range (difference between quietest and loudest).
  - **Dialogue compression**: Fast attack (1-5ms), medium release (50-100ms), ratio 2:1 to 4:1. Makes speech consistent.
  - **SFX compression**: Can be more aggressive for punch.
  - **Ambience compression**: Light compression to keep bed steady.
- **Noise reduction**: Remove unwanted noise (hiss, hum, wind). Use spectral editing or NR plugins.
- **Pitch shifting**: Change pitch without speed change (or vice versa). Use for creature sounds, voice effects.
- **Time stretching**: Change duration without pitch change. Use for fitting SFX.

### 9. Mixing & Levels
- **Level hierarchy (approximate dBFS)**:
  - **Dialogue**: -6 to -3 dB peak, -20 to -16 LUFS integrated.
  - **Music**: -18 to -12 dB peak, -24 to -20 LUFS.
  - **SFX**: -12 to -6 dB peak (but varies widely).
  - **Ambience**: -40 to -30 dB peak.
- **Headroom**: Keep peaks below 0 dBFS (digital clipping). Aim for -3 dB max peak.
- **Loudness standards**:
  - YouTube: -14 LUFS
  - TikTok/Reels: -14 to -16 LUFS
  - Broadcast: -23 LUFS (EBU R128)
- **Balancing**: Start with dialogue, then add music, then SFX, then ambience. Adjust each.
- **Automation**: Draw volume curves over time for precise control.

### 10. Sound Design Workflow
- **Step 1: Organization**: Label tracks: Dialogue, Music, SFX, Foley, Ambience. Use colors.
- **Step 2: Dialogue edit**: Clean up speech (remove noise, mouth clicks, breaths). Compress.
- **Step 3: Music bed**: Add music. Adjust level to leave space for dialogue.
- **Step 4: Ambience**: Add room tone/location bed. Low volume.
- **Step 5: Foley**: Record or add Foley for all actions. Sync precisely.
- **Step 6: SFX**: Add sound effects for visual events. Layer as needed.
- **Step 7: Processing**: Apply EQ, reverb, compression to each element.
- **Step 8: Mix**: Balance all levels. Use automation for changes over time.
- **Step 9: Final loudness**: Measure LUFS. Adjust to target.
- **Step 10: Render**: Export audio with video or as stems.

## Technical Guidelines

### Audio Specifications
- **Sample rate**: 48kHz for video. 44.1kHz for web-only.
- **Bit depth**: 24-bit for recording, 16-bit for delivery (unless high-res).
- **Channels**: Stereo for most content. 5.1/7.1 for surround.
- **File formats**: WAV (uncompressed), AIFF, or high-bitrate MP3/AAC for delivery.

### Common Sound Design Tasks
- **Creating a whoosh**: Sweep filter + noise + wind + whoosh sample. Layer and pan.
- **Creating an explosion**: Deep boom + crackle + debris + rumble. Add reverb.
- **Creating UI sounds**: Short, clean, often synthesized. Use sine/square waves with envelopes.
- **Creating creature sounds**: Pitch-shifted animal recordings, vocal manipulations.
- **Creating magic sounds**: Chimes, shimmer, reverse cymbals, granular synthesis.

### Tools & Software
- **DAWs**: Pro Tools, Reaper, Ableton, Logic, FL Studio.
- **Video editors**: Premiere, DaVinci Resolve, Final Cut have audio capabilities.
- **Plugins**:
  - **Reverb**: Valhalla VintageVerb, Lexicon, Altiverb.
  - **Delay**: Soundtoys EchoBoy, H-Delay.
  - **Distortion**: Decapitator, Softube Saturation.
  - **EQ**: FabFilter Pro-Q, TDR Nova.
  - **Compression**: FabFilter Pro-C, Waves SSL.
  - **Spectral editing**: iZotope RX, Acon Digital Restoration.
- **Field recorders**: Zoom H1n, Tascam DR-05, Sound Devices.

## Common Pitfalls to Avoid

- **Dialogue unintelligible**: Most important. If viewers can't understand speech, you've failed.
- **Music too loud**: Should never compete with dialogue. Duck properly.
- **No ambience**: Dead air feels unnatural. Always have some room tone.
- **SFX too quiet**: Impact sounds need to be felt. Don't bury them.
- **Reverb overload**: Too much reverb makes audio muddy. Use sparingly.
- **Clipping**: Distortion from peaks over 0 dB. Leave headroom.
- **Noisy audio**: Hiss, hum, rumble distract. Clean up with NR.
- **Inconsistent levels**: Some clips loud, others quiet. Normalize/compress.
- **Poor panning**: All audio centered = flat, unrealistic. Use stereo field.
- **Overpowering ambience**: Ambience should be subtle, not noticeable.
- **Unrealistic Foley**: Footsteps that don't match surface, cloth that doesn't rustle.
- **Repetitive SFX**: Same explosion sound every time gets old. Vary.
- **No audio bridges**: Abrupt audio changes are jarring. Use J-cuts/L-cuts.
- **Ignoring frequency clashes**: Multiple elements fighting in same frequency range create muddiness. Use EQ to carve space.

## Advanced Techniques

### 1. Advanced Foley
- **Foley walking**: Different surfaces, shoes, speeds. Record multiple takes.
- **Foley props**: Create custom sounds for specific objects (unique sword, specific gun).
- **Foley editing**: Use multiple layers (footstep + cloth + environment).
- **Foley performance**: Watch picture closely, match timing exactly, perform with character.

### 2. Sound Layering & Stacking
- **Layering principle**: Combine 2-4 sounds to create richer, more complex SFX.
- **Frequency separation**: Each layer occupies different frequency range (sub, mid, high).
- **Temporal separation**: Layers start at slightly different times for width.
- **Spatial separation**: Pan layers differently for stereo width.
- **Example explosion**:
  - Layer 1: Deep sub-bass (20-60Hz) - body feel
  - Layer 2: Mid boom (100-300Hz) - main explosion
  - Layer 3: High crackle (2-5kHz) - debris
  - Layer 4: Rumble (50-100Hz) - distant thunder

### 3. Creative Sound Design
- **Sound montage**: Build sequence entirely from sound before picture.
- **Audio-visual metaphor**: Sound represents emotion or theme (heartbeat for tension, wind for loneliness).
- **Subjective audio**: Audio reflects character's perspective (muffled when underwater, heightened when scared).
- **Audio flashback**: Sound from past scene bleeds into present.
- **Silence as tool**: Strategic silence can be powerful. Remove all sound for impact.

### 4. Advanced Processing
- **Modulation**: Chorus, flanger, phaser for movement.
- **Granular synthesis**: Break sound into grains, reassemble for textures.
- **Convolution reverb**: Use real space impulse responses for authentic reverb.
- **Spectral processing**: Manipulate frequency content over time.
- **Dynamic EQ**: EQ that changes based on level (e.g., reduce bass when dialogue present).
- **Multiband compression**: Compress different frequency bands separately.

### 5. Spatial Audio & 3D Sound
- **Binaural recording**: Capture 3D audio with two mics in ear positions.
- **Ambisonics**: Full-sphere 3D audio format (first-order, higher-order).
- **Object-based audio**: Individual sound objects with position metadata (Dolby Atmos).
- **HRTF processing**: Simulate 3D positioning in headphones.
- **Surround mixing**: 5.1, 7.1 channel layouts. Use surround for ambience, effects.

### 6. Dialogue Processing
- **Noise reduction**: Remove background noise without making voice sound robotic.
- **De-essing**: Reduce harsh "s" sounds (sibilance).
- **De-plosives**: Remove "p" and "b" pops (pop filter or EQ cut below 100Hz).
- **Mouth clicks**: Remove lip smacks and clicks (spectral editing).
- **Volume automation**: Smooth out level changes within a single take.
- **EQ for presence**: Boost 2-5kHz for clarity, cut 200-400Hz for mud.
- **Compression**: Even out dynamics. Fast attack, medium release.

### 7. Music Integration
- **Music editing**: Cut music to fit video length. Use loops, stems.
- **Music spotting**: Decide where music starts/stops, changes intensity.
- **Music-to-picture**: Edit music to match visual cuts and beats.
- **Source vs score**: Source music (diegetic, heard by characters) vs score (non-diegetic, only audience hears).
- **Music transitions**: Crossfades, stingers, stings, hits.

### 8. Audio Restoration
- **Noise profiling**: Capture noise print and subtract.
- **De-hum**: Remove electrical hum (50/60Hz and harmonics).
- **De-click**: Remove clicks, pops, crackles.
- **De-reverb**: Reduce room echo.
- **De-clip**: Repair distorted audio from clipping.
- **Spectral repair**: Visually remove unwanted sounds in spectrogram view.

### 9. Delivery & Loudness
- **Loudness normalization**: Measure integrated LUFS and adjust to target.
- **True peak limiting**: Ensure no samples exceed 0 dBFS (use true peak limiter).
- **Format-specific**: Different platforms have different loudness standards.
- **Stereo vs mono**: Some platforms require mono compatibility. Check phase.
- **Sample rate conversion**: If needed, use high-quality resampler.

## Workflow Recommendations

1. **Spotting session**: Watch picture with director/sound designer. Note all audio needs.
2. **Sound gathering**: Collect or record all needed SFX, Foley, music.
3. **Organization**: Import and label all audio files. Create track layout.
4. **Dialogue first**: Clean, process, and balance dialogue tracks.
5. **Ambience bed**: Add room tone and location ambience. Set level.
6. **Foley pass**: Add Foley for all actions. Sync precisely.
7. **SFX pass**: Add sound effects for visual events. Layer as needed.
8. **Music pass**: Add music. Adjust timing to picture.
9. **Processing**: Apply EQ, compression, reverb to each element.
10. **Mix**: Balance all levels. Use automation for dynamics.
11. **Loudness check**: Measure LUFS. Adjust to target.
12. **Final review**: Listen on multiple systems (headphones, speakers, phone).
13. **Render**: Export final mix or stems.

## Related Skills

For complementary techniques, refer to:
- `./core-techniques/audio-sync.md` - Synchronizing audio to video and beats
- `./core-techniques/pacing.md` - How audio affects pacing
- `./core-techniques/transitions.md` - Audio transitions and bridges
- `./styles/cinematic.md` - Subtle, realistic sound design for film
- `./styles/gameplay.md` - Game audio integration and dynamic mixing
- `./styles/dark-meme-dynamic.md` - SFX-heavy, punchy sound for memes
- `./styles/tiktok-news-hype.md` - Beat-synced, high-energy sound design

