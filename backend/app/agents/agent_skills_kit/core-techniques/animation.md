---
name: animation
description: Core animation techniques including keyframing, easing, and motion design principles for video editing
metadata:
  tags: animation, keyframing, easing, motion-design, motion-graphics
---

## When to use

Use this skill whenever you need to create animated elements, motion graphics, or animated transitions in your video. This covers everything from simple text animations to complex layered motion graphics. Understanding animation principles is essential for making static elements feel dynamic and engaging.

## Core Principles

### 1. Keyframing Fundamentals
- **Definition**: Keyframes define the start and end points of any animation. The software interpolates between them to create motion.
- **Setting keyframes**: Place a keyframe at the beginning of a motion (position, scale, rotation, opacity, etc.), then move to a later time and change the property. The software creates the in-between frames.
- **Keyframe density**: More keyframes = more control but also more work. Use as few as needed for the desired motion.
- **Keyframe types**:
  - **Linear**: Constant speed between keyframes. Feels robotic.
  - **Eased (Bezier)**: Accelerates and decelerates naturally. Feels organic.
  - **Hold**: Freezes value until next keyframe changes it.

### 2. Easing & Interpolation
- **Why easing matters**: Real-world objects don't start and stop instantly. Easing simulates acceleration and deceleration.
- **Common easing types**:
  - **Ease In**: Slow start, fast end (like a car accelerating)
  - **Ease Out**: Fast start, slow end (like a car braking)
  - **Ease In-Out**: Slow start and end, fast middle (most natural)
  - **Bounce**: Overshoots and settles (for playful effects)
  - **Elastic**: Springs back and forth (for bouncy UI)
  - **Exponential**: Rapid acceleration or deceleration
- **Graph editor**: Use the velocity/position graph to fine-tune easing curves. This is where professional animators spend most of their time.
- **Easing duration**: Typically 10-30% of total animation duration for natural motion.

### 3. Animation Principles (From Disney's 12 Principles)
- **Squash and stretch**: Deform objects during motion to convey weight and flexibility. A bouncing ball squashes on impact and stretches in air.
- **Anticipation**: Prepare the viewer for an action. A character crouches before jumping. A button depresses before releasing.
- **Staging**: Direct viewer attention. Use motion to highlight what's important.
- **Straight-ahead vs pose-to-pose**:
  - **Pose-to-pose**: Plan key poses, then fill in between. Better for controlled, precise animations.
  - **Straight-ahead**: Animate frame by frame spontaneously. Better for organic, unpredictable motion (particles, fire).
- **Follow-through and overlapping action**: Not all parts move at once. Hair, clothing, or secondary elements continue moving after the main action stops.
- **Slow in and slow out**: The first and last frames of any motion should have more spacing (slower), middle frames closer together (faster). This is easing.
- **Arcs**: Natural motion follows curved paths, not straight lines. Use curved motion paths for organic movement.
- **Timing**: The speed of action conveys weight and emotion. Heavy objects move slower, light objects faster.
- **Exaggeration**: Amplify movements for clarity and impact. Realism is less important than readability.
- **Solid drawing**: Understand 3D form. Even 2D animations should feel like they exist in 3D space.
- **Appeal**: Characters and motion should be interesting to watch. Charisma matters.

### 4. Motion Design Specifics
- **Purpose-driven animation**: Every animation should serve a purpose: guide attention, indicate state change, provide feedback, or add delight.
- **Duration guidelines**:
  - **UI feedback**: 100-300ms (instant response)
  - **Transitions**: 300-500ms (smooth but quick)
  - **Complex motion**: 500-1000ms (allows viewer to follow)
  - **Never exceed 2 seconds** for a single animated element unless it's a main feature.
- **Staggering**: Animate multiple elements with slight delays (50-100ms) to create wave effects and guide the eye sequentially.
- **Looping**: For continuous animations (loading spinners, ambient motion), ensure the loop is seamless. Match start and end states exactly.
- **Pausing**: Give viewers time to absorb information. After a complex animation, hold the final state for at least 500ms before moving on.

### 5. Text Animation
- **Readability first**: Animated text must remain readable. Avoid excessive motion that makes text hard to read.
- **Reveal techniques**:
  - **Typewriter**: Characters appear one by one. Good for emphasis.
  - **Fade in/out**: Simple, elegant. Good for subtitles.
  - **Slide/translate**: Text moves into position. Good for headlines.
  - **Scale/pop**: Text grows into view. Good for punchlines.
  - **Glitch**: Distorted reveal. Good for tech/hacker themes.
- **Text hierarchy**: Animate primary text (headlines) more prominently than secondary (captions).
- **Sync to audio**: Text animations should align with voiceover or sound effects for maximum impact.

## Technical Guidelines

### Software & Tools
- **Keyframe interpolation**: Linear, Bezier, Auto Bezier, Continuous Bezier
- **Graph editor**: Essential for fine-tuning motion curves
- **Motion paths**: Use Bézier curves for organic movement
- **Expressions**: Use simple expressions (wiggle, loop, time) for procedural animation
- **Parenting**: Link layers so child follows parent's motion
- **Null objects**: Use as animation controllers

### Performance Considerations
- **Pre-rendering**: Complex animations may need pre-rendering for smooth playback
- **Proxy workflow**: Use lower resolution proxies while animating
- **Render quality**: 100% for final, 50% for preview
- **Frame rate**: 24/25/30fps for cinematic, 60fps for smooth motion graphics

### Color & Opacity Animation
- **Opacity fades**: Use 0.1-0.3 second fades for smooth transitions
- **Color shifts**: Animate hue/saturation for mood changes
- **Exposure**: Animate brightness for emphasis

## Common Pitfalls to Avoid

- **Linear motion everywhere**: Makes everything feel robotic. Use easing.
- **Too many keyframes**: Creates jittery, uneven motion. Simplify.
- **No anticipation**: Actions feel abrupt and confusing. Add prep frames.
- **Ignoring arcs**: Straight-line motion looks unnatural. Use curved paths.
- **Over-animating**: Everything moving at once creates visual chaos. Have resting elements.
- **Poor timing**: Too fast = can't follow, too slow = boring. Test with real viewers.
- **Ignoring weight**: Heavy objects should move slower, light objects faster.
- **No follow-through**: Motion stops dead. Add secondary motion.
- **Text unreadable**: Fancy animation that sacrifices readability is a failure.
- **Loop seams**: Looping animations that jump at the loop point are jarring. Ensure perfect seamlessness.

## Advanced Techniques

### 1. Procedural Animation
- **Wiggle expression**: `wiggle(frequency, amplitude)` for subtle organic movement
- **Time remapping**: Speed up/slow down clips dynamically
- **Loop expressions**: `loopOut()` for seamless repeating animations
- **Inverse kinematics (IK)**: For character animation, control end effector (hand/foot) and let software calculate joint rotations

### 2. Particle Systems
- **Particle emitters**: Create fire, smoke, rain, sparks, dust
- **Particle parameters**: Birth rate, lifetime, velocity, gravity, size, color
- **Particle types**: Points, sprites, textured polygons
- **Particle forces**: Wind, turbulence, attractors, repulsors

### 3. 3D Space in 2D
- **2.5D**: Use Z-position and scale to create depth in 2D compositions
- **Parallax**: Move layers at different speeds to create depth illusion
- **Camera simulation**: Animate a virtual camera through 2D layers for 3D feel
- **Lighting**: Add drop shadows, inner glows, and bevels to enhance depth

### 4. Character Animation Basics
- **Rigging**: Create skeleton (bones/joints) for characters
- **Skinning**: Bind mesh to skeleton
- **FK vs IK**: Forward Kinematics (rotate joints from root) vs Inverse Kinematics (position end effector)
- **Facial rigging**: Bone-based or morph-target-based for expressions
- **Lip sync**: Phoneme shapes matched to audio

### 5. Motion Tracking Integration
- **Track motion**: Use point tracking to attach graphics to moving objects
- **stabilize footage**: Remove unwanted camera shake
- **3D camera solve**: Extract 3D camera movement from 2D footage
- **Mask tracking**: Animate masks automatically

## Workflow Recommendations

1. **Plan**: Sketch or storyboard the animation. Identify key poses or states.
2. **Setup**: Create layers, nulls, and rigging. Organize with naming and colors.
3. **Blocking**: Set major keyframes (start, middle, end) with linear interpolation. Focus on timing and spacing.
4. **Splining**: Convert keyframes to Bezier and adjust curves for smooth motion.
5. **Polish**: Add secondary motion, follow-through, overlapping action.
6. **Refine**: Adjust timing, add easing, fine-tune graph editor.
7. **Test**: Play back in real-time. Check for jitters, pops, or unnatural motion.
8. **Render test**: Export a short segment to verify quality and performance.
9. **Iterate**: Based on feedback, adjust keyframes and timing.
10. **Final render**: Export at appropriate settings.

## Related Skills

For complementary techniques, refer to:
- `./core-techniques/transitions.md` - Animated transition techniques
- `./core-techniques/text-animation.md` - Specialized text motion
- `./core-techniques/motion-graphics.md` - Advanced motion design workflows
- `./core-techniques/pacing.md` - Timing and rhythm in animation
- `./styles/cinematic.md` - Subtle, naturalistic animation for film
- `./styles/dark-meme-dynamic.md` - Exaggerated, fast-paced animation for memes

