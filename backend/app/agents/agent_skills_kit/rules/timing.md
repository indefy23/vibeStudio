---
name: timing
description: Timing concepts, duration control, and time-based editing techniques for video
metadata:
  tags: timing, duration, pacing, clocks, time-remapping, scheduling
---

## When to use

Use this skill whenever you need to control the timing of elements in your video - setting clip durations, animation timing, pacing, time remapping, and any time-based decisions. Timing is fundamental to rhythm, engagement, and narrative flow.

## Core Principles

### 1. What is Timing in Video?
- **Definition**: The arrangement and duration of visual and audio elements over time.
- **Aspects**:
  - **Duration**: How long something lasts (clip, shot, animation).
  - **Pacing**: Overall speed of the video (fast, slow, variable).
  - **Rhythm**: Pattern of timing (regular, irregular, syncopated).
  - **Tempo**: Beats per minute (BPM) for music-synced editing.
- **Impact**: Timing affects emotion, comprehension, engagement, and professionalism.

### 2. Time Units & Measurement
- **Frames**: Smallest unit. 1 frame at 30fps = 1/30s ≈ 0.0333s.
- **Seconds**: Common unit. 1 second = 30 frames at 30fps.
- **Timecode**: SMPTE format HH:MM:SS:FF (hours:minutes:seconds:frames).
- **BPM**: Beats per minute. Beat duration = 60/BPM seconds.
- **Beat divisions**:
  - **1/1**: Whole beat
  - **1/2**: Half beat
  - **1/4**: Quarter beat (most common for cuts)
  - **1/8**: Eighth beat (very fast)
  - **1/16**: Sixteenth beat (extremely fast)
- **Musical notes**: Whole, half, quarter, eighth, sixteenth correspond to beat divisions.

### 3. Duration Guidelines
- **Shot duration**:
  - **Very fast**: 0.3-0.5s (high-energy, chaotic)
  - **Fast**: 0.5-1.5s (standard for fast-paced content)
  - **Medium**: 1.5-3s (normal speech, action)
  - **Slow**: 3-5s (contemplative, dramatic)
  - **Very slow**: 5s+ (establishing, emotional)
- **Text duration**:
  - **Short phrase (1-3 words)**: 1-2s
  - **Sentence (5-10 words)**: 2-4s
  - **Paragraph (15+ words)**: 4-8s
  - **Reading speed**: 2-3 words per second average.
- **Transition duration**:
  - **Hard cut**: 0 frames (instant)
  - **Quick transition**: 0.1-0.3s (3-10 frames at 30fps)
  - **Standard**: 0.5-1s (15-30 frames)
  - **Slow**: 1-2s (30-60 frames)
- **Animation duration**:
  - **Micro-interaction**: 0.1-0.3s (button press)
  - **UI animation**: 0.3-0.5s (menu slide)
  - **Element entrance**: 0.5-1s (text pop-in)
  - **Complex motion**: 1-3s (logo reveal)
  - **Character action**: 0.5-2s (walk cycle)

### 4. Pacing & Rhythm
- **Pacing types**:
  - **Fast**: Many short shots (0.5-1s). Energy, urgency, chaos.
  - **Slow**: Few long shots (3-10s). Calm, serious, dramatic.
  - **Variable**: Mix of fast and slow. Dynamic, engaging.
  - **Accelerando**: Gradually speeds up.
  - **Ritardando**: Gradually slows down.
- **Rhythm patterns**:
  - **Regular**: Consistent timing (like a metronome). Predictable.
  - **Irregular**: Varied timing. Interesting, less predictable.
  - **Syncopated**: Accents on off-beats. Exciting, surprising.
  - **Free**: No discernible pattern. Organic, natural.
- **Creating rhythm**:
  - **Beat-synced**: Cuts on musical beats. Most common for music videos.
  - **On-beat**: Cuts on downbeat (1, 2, 3, 4). Strong.
  - **Off-beat**: Cuts on upbeat (the "and" of beat). Syncopated.
  - **Every two beats**: Slower, more relaxed.
  - **Every half beat**: Very fast, energetic.

### 5. Time Remapping
- **Speed ramping**: Change speed within a clip.
  - **Speed up**: 1.5x, 2x, 4x.
  - **Slow down**: 0.5x, 0.25x, 0.1x.
  - **Ramp**: Smooth transition between speeds.
- **Time reversal**: Play clip backwards.
- **Freeze frame**: Hold on single frame.
- **Frame blending**: Mix frames for smooth slow-mo.
- **Optical flow**: Generate intermediate frames for ultra-smooth slow-mo.
- **Time stretching**: Change duration without pitch change (audio).
- **Time remapping curve**: Graph showing speed over time. Can create complex speed variations.

### 6. Beat Alignment
- **Detect beats**:
  - **Manual**: Tap along, mark beats.
  - **Automatic**: Beat detection algorithms (Ableton, Adobe Audition).
  - **Visual**: Waveform transients.
- **Beat grid**: Align timeline to beats.
  - **Set BPM**: Enter beats per minute.
  - **Snap**: Enable snap to beat grid.
  - **Markers**: Place beat markers on timeline.
- **Cut on beat**: Align cut points to beat markers.
- **Effect on beat**: Trigger animations, transitions, SFX on beat.
- **Sub-beats**: Cut on 1/2, 1/4, 1/8 beats for faster rhythm.
- **Beat drop**: Special emphasis on downbeat after build-up.

### 7. Timing for Different Content Types
- **TikTok/Reels**:
  - **Hook**: 0-3s must grab.
  - **Shot length**: 0.5-1.5s average.
  - **Text duration**: 1-3s.
  - **Transitions**: On beat, very fast (0.1-0.3s).
- **YouTube**:
  - **Hook**: 0-15s (depends on length).
  - **Shot length**: 1-4s typical.
  - **Pacing**: Variable, can be slower.
  - **Mid-roll considerations**: Don't cut during ad break.
- **Documentary**:
  - **Shot length**: 3-10s for talking heads.
  - **Pacing**: Slower, contemplative.
  - **Silence**: Used for impact.
- **Action movie**:
  - **Shot length**: 0.5-2s during action.
  - **Pacing**: Fast, but with variation (slow during dialogue).
- **Tutorial/Explainer**:
  - **Shot length**: 2-5s for demonstrations.
  - **Pacing**: Moderate, clear.
  - **Text duration**: Long enough to read (3-6s).
- **Music video**:
  - **Shot length**: Sync to beat (often 1 beat per shot).
  - **Pacing**: Matches music tempo.
  - **Cut on beat**: Almost every beat.

### 8. Timing for Transitions
- **Transition timing**:
  - **Cut**: 0 frames.
  - **Whip pan**: 0.1-0.3s (3-10 frames).
  - **Zoom**: 0.2-0.5s.
  - **Fade**: 0.5-2s.
  - **Dissolve**: 0.5-1.5s.
- **Transition placement**:
  - **On beat**: Most common for energetic videos.
  - **On action**: Cut during movement (masking cut).
  - **On word**: Cut after spoken word for impact.
  - **On glance**: Cut after character looks.
- **Transition duration vs shot length**:
  - **Fast shots**: Short transitions (0.1-0.3s).
  - **Slow shots**: Longer transitions (0.5-1s).
  - **Rule**: Transition should be noticeable but not dominate.

### 9. Timing for Text & Graphics
- **Text reveal timing**:
  - **Before speech**: Text appears 0.5-1s before voiceover starts.
  - **With speech**: Text appears exactly when word spoken.
  - **After speech**: Text stays 1-2s after speech ends for retention.
- **Text duration**:
  - **Headline**: 2-4s.
  - **Subtitle**: 3-6s.
  - **Bullet point**: 2-3s each.
- **Text animation timing**:
  - **Pop-in**: 0.2-0.4s.
  - **Typewriter**: 0.05-0.1s per character.
  - **Slide**: 0.3-0.6s.
  - **Fade**: 0.3-0.5s.
- **Lower thirds**:
  - **In**: 0.3-0.5s animation.
  - **On screen**: 3-10s (or until speaker done).
  - **Out**: 0.3-0.5s when no longer relevant.
- **Graphic duration**:
  - **Logo sting**: 1-3s.
  - **Animated background**: Loops seamlessly.
  - **Call to action**: 3-5s at end.

### 10. Timing for Audio
- **Dialogue pacing**:
  - **Natural speech**: 150-160 words per minute (2.5-2.7 wps).
  - **Voiceover**: 140-150 wpm for clarity.
  - **Fast talk**: 200+ wpm for urgency.
  - **Slow talk**: 100 wpm for gravitas.
- **Music timing**:
  - **Cut on beat**: Most common.
  - **Cut on downbeat**: Strongest.
  - **Cut on off-beat**: Syncopated feel.
  - **Cut every 2 beats**: More relaxed.
- **Sound effect timing**:
  - **On action**: Exactly when visual event occurs.
  - **Pre-action**: 0.1-0.3s before for anticipation.
  - **Post-action**: 0.1-0.2s after for impact.
- **Silence timing**:
  - **Pause for impact**: 0.5-2s silence after big reveal.
  - **Beat drop**: Silence before drop (1/2 to 1 beat).
  - **Dramatic pause**: 1-3s for emphasis.
- **Audio ducking timing**:
  - **Duck start**: 0.2-0.5s before dialogue.
  - **Duck end**: 0.2-0.5s after dialogue ends.
  - **Duck amount**: -3 to -6 dB typical.

## Technical Guidelines

### Frame Rates & Timecode
- **Common frame rates**: 23.976, 24, 25, 29.97, 30, 50, 59.94, 60 fps.
- **Timecode formats**:
  - **SMPTE**: HH:MM:SS:FF (non-drop)
  - **SMPTE drop**: HH:MM:SS;FF (drop frame for 29.97/59.94)
  - **Frames**: Total frame count from start.
  - **Seconds**: Decimal seconds.
- **Frame accuracy**: Edit to frame boundary. No sub-frame precision in most editors.
- **Timecode display**: Show in timeline for precision.

### Duration Calculation
- **Frames to seconds**: `seconds = frames / fps`
- **Seconds to frames**: `frames = seconds * fps`
- **Beat duration**: `beat_seconds = 60 / BPM`
- **Frames per beat**: `frames_per_beat = (60 / BPM) * fps`
- **Example**: 120 BPM at 30fps = 0.5s per beat = 15 frames per beat.

### Timeline Management
- **Work area**: Set start/end for rendering.
- **In/Out points**: Define clip usage.
- **Markers**: Place at important timing points (beats, scene changes).
- **Nested sequences**: Manage timing in sub-sequences.
- **Time remapping**: Use time remap property for speed changes.
- **Frame blending**: Enable for smooth slow-mo.
- **Motion blur**: Shutter angle affects motion blur duration.

### Precision Timing Tools
- **Numeric entry**: Enter exact time/frame numbers.
- **Snapping**: Snap to other clips, markers, playhead.
- **Ripple edit**: Shift subsequent clips when trimming.
- **Rolling edit**: Adjust in/out of adjacent clips simultaneously.
- **Slip/slide**: Change content without changing duration/position.
- **Timecode monitor**: Show current timecode.
- **JKL navigation**: Shuttle forward/backward at variable speed.

## Common Pitfalls to Avoid

- **Inconsistent pacing**: Random shot lengths without reason. Establish rhythm.
- **Shots too long**: Lose attention. Trim aggressively.
- **Shots too short**: Viewers can't process. Minimum 0.3s for most content.
- **Off-beat editing**: Cuts not on music beat feel sloppy. Sync to audio.
- **No variation**: All same duration = boring. Mix it up.
- **Text too brief**: Can't read before it disappears. Extend duration.
- **Text too long**: Viewers wait for next thing. Shorten.
- **Transitions too long**: Slow down pace. Keep short (0.1-0.5s).
- **Transitions too short**: Not noticeable. At least 3-5 frames.
- **No pauses**: Constant motion = exhausting. Include rests.
- **Poor timing on actions**: Cut in middle of motion. Cut on peaks/landings.
- **Ignoring natural pauses**: Cut during speech pause. Respect breathing.
- **No beat alignment**: Music and video feel disconnected. Sync them.
- **Frame inaccuracy**: Cuts between frames = jittery. Snap to frames.
- **Ignoring platform norms**: TikTok vs YouTube have different timing expectations.

## Advanced Techniques

### 1. Advanced Time Remapping
- **Speed ramps with bezier**: Smooth acceleration/deceleration curves.
- **Time reversal with easing**: Reverse motion with natural ease.
- **Frame blending modes**: Pixel motion vs frame blending for slow-mo.
- **Time remapping expressions**: Use expressions for procedural timing.
- **Time displacement**: Use one layer's luminance to displace another in time.
- **Echo with time offset**: Create motion trails by offsetting in time.

### 2. Complex Beat Sync
- **Multiple BPM sections**: Song changes tempo. Adjust timing accordingly.
- **Beat subdivision**: Cut on 1/8 or 1/16 notes for hyper-fast editing.
- **Polyrhythms**: Overlay different rhythmic patterns.
- **Sync to transients**: Cut on audio transients (drum hits, clicks) not just beat.
- **Anticipatory cuts**: Cut slightly before beat for anticipation.
- **Delayed cuts**: Cut slightly after beat for weight.

### 3. Variable Pacing Strategies
- **Tension curve**:
  - **Build**: Shorten shots, increase tempo.
  - **Peak**: Very fast (0.3-0.5s shots), high energy.
  - **Release**: Lengthen shots, slow down.
  - **Repeat**: Cycle for emotional journey.
- **Pacing by content**:
  - **Dialogue**: Longer shots (2-4s) to hear speech.
  - **Action**: Short shots (0.5-1.5s) for energy.
  - **Exposition**: Medium (1-3s) with text support.
  - **Emotion**: Slow (3-8s) for impact.
- **Pacing transitions**:
  - **Fast→slow**: Use long transition (fade) or pause.
  - **Slow→fast**: Use quick cut or whip pan.
  - **Variable**: Mix within sequence for dynamism.

### 4. Timing for Narrative
- **Three-act timing**:
  - **Act 1 (setup)**: Moderate pacing, establish characters.
  - **Act 2 (confrontation)**: Variable, build tension.
  - **Act 3 (resolution)**: Fast climax, slow denouement.
- **Hero's journey timing**:
  - **Ordinary world**: Normal pace.
  - **Call to adventure**: Accelerate.
  - **Trials**: Variable, some fast, some slow.
  - **Climax**: Very fast.
  - **Return**: Slow, reflective.
- **Mystery structure**:
  - **Clues**: Slow, detailed.
  - **Red herrings**: Medium.
  - **Revelation**: Fast cuts for excitement.
  - **Explanation**: Slow for comprehension.

### 5. Advanced Synchronization
- **Phoneme sync**: Cut when mouth closes/opens. Use for dialogue.
- **Action sync**: Cut on peak of action (jump, throw, hit).
- **Eye trace**: Cut when eyes move or blink.
- **Gesture sync**: Cut at end of gesture.
- **Music video style**: Every cut on beat or even every half-beat.
- **Sound design sync**: Cuts align with sound effect transients.

### 6. Timing Automation
- **Expressions for timing**:
  - `time` - current time.
  - `timeToFrames()` - frames from start.
  - `timeToCurrentFormat()` - formatted time.
  - `loopOut()` - loop animation.
  - `wiggle()` - random timing variations.
- **Scripting timing**:
  - **ExtendScript**: Automate timing adjustments.
  - **Python**: Batch process timing.
  - **Expressions**: Procedural timing based on comp time.
- **Template timing**: Pre-set timing patterns that can be applied.

### 7. Timing for Multi-Camera
- **Cut timing**: Cut on action or beat, not on speech.
- **Camera switch duration**: Instant cut or very short dissolve (0.2-0.5s).
- **Reaction shots**: Insert after line spoken, before response.
- **Coverage timing**: Ensure all angles have enough footage for cuts.
- **Sync points**: Use clap or timecode to sync cameras.

### 8. Timing in Motion Graphics
- **Text reveal timing**:
  - **Typewriter**: 0.05-0.1s per character.
  - **Pop-in**: 0.2-0.4s with overshoot.
  - **Slide**: 0.3-0.6s with ease out.
- **Logo animation timing**:
  - **Build**: 0.5-1s.
  - **Hold**: 1-2s.
  - **Exit**: 0.3-0.5s.
- **UI animation timing**:
  - **Button press**: 0.1-0.2s.
  - **Menu slide**: 0.3-0.5s.
  - **Page turn**: 0.5-1s.
- **Transition timing**:
  - **Wipe**: 0.3-0.8s.
  - **Zoom**: 0.2-0.5s.
  - **Fade**: 0.5-1.5s.

### 9. Timing for Social Media
- **TikTok**:
  - **First 3s**: Must hook.
  - **Shot length**: 0.5-1.5s average.
  - **Text**: 1-3s, large font.
  - **Loop**: Last 1-2s should lead back to first.
- **Instagram Reels**: Similar to TikTok.
- **YouTube Shorts**: Similar to TikTok.
- **Twitter/X**: Under 2min, very punchy.
- **LinkedIn**: Professional, slightly longer acceptable.

### 10. Timing Analysis & Optimization
- **Retention graphs**: See where viewers drop off. Adjust timing there.
- **Heatmaps**: See where viewers look. Time reveals accordingly.
- **A/B testing**: Try different timing patterns, measure engagement.
- **Frame-by-frame review**: Check timing precision.
- **Real-time playback**: Watch at full speed, not slow.
- **Audience testing**: Watch with target audience, note confusion/boredom.
- **Audio waveform analysis**: See natural pauses, speech rhythm.
- **Beat detection software**: Automatically find beats.

## Workflow Recommendations

1. **Determine overall pacing**: Fast, slow, variable? Based on content type and goal.
2. **Set BPM**: If syncing to music, know the BPM.
3. **Create beat grid**: Mark beats on timeline.
4. **Rough cut**: Place clips in order, ignore timing initially.
5. **Trim to duration**: Cut clips to appropriate lengths for content.
6. **Sync to beat**: Align cuts to beat grid (if applicable).
7. **Adjust pacing**: Speed up slow sections, slow down fast sections as needed.
8. **Add transitions**: Insert transitions with appropriate duration.
9. **Time text/graphics**: Ensure text duration matches reading speed.
10. **Time audio**: Sync SFX, duck music, set voiceover pace.
11. **Review**: Watch at real speed. Does timing feel right?
12. **Test on device**: Phone, tablet, TV. Timing still good?
13. **Get feedback**: Others may notice timing issues.
14. **Iterate**: Refine timing based on feedback.
15. **Final check**: Frame-by-frame review for precision.

## Related Skills

For complementary techniques, refer to:
- `./core-techniques/pacing.md` - Overall rhythm and speed control
- `./core-techniques/audio-sync.md` - Synchronizing audio to timing
- `./core-techniques/transitions.md` - Transition timing
- `./core-techniques/text-animation.md` - Text timing
- `./rules/sequencing.md` - Arranging elements in time
- `./styles/cinematic.md` - Film pacing
- `./styles/dark-meme-dynamic.md` - Fast meme timing
- `./styles/tiktok-news-hype.md` - Beat-synced news timing

