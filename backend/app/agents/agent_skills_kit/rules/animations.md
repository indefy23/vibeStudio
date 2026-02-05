---
name: animations
description: Animation principles and techniques for video editing including keyframing, easing, and motion design
metadata:
  tags: animation, keyframes, easing, motion, principles
---

## When to use

Use this skill whenever you need to animate any property in your video - position, scale, rotation, opacity, color, or any other animatable parameter. This includes moving graphics, text animations, transitions, and any motion that changes over time.

## Core Principles

### 1. Animation Fundamentals
- **Keyframe**: A point in time where you set a property value. The software interpolates between keyframes.
- **Interpolation**: How the software calculates values between keyframes.
  - **Linear**: Constant speed. Mechanical, unnatural.
  - **Bezier (smooth)**: Ease in/out. Natural acceleration/deceleration.
  - **Hold**: No interpolation. Value stays constant until next keyframe.
- **Timing**: Speed of movement. Determines weight and intention.
  - Fast = light, urgent, energetic
  - Slow = heavy, deliberate, dramatic
- **Spacing**: Distance between keyframes. Closer = slower, farther = faster.
- **Easing**: Acceleration and deceleration.
  - **Ease in**: Starts slow, speeds up.
  - **Ease out**: Starts fast, slows down.
  - **Ease in-out**: Slow start, fast middle, slow end.

### 2. 12 Principles of Animation (Applied to Video)
- **Squash and stretch**: Deform objects to show weight and flexibility. Keep volume consistent.
- **Anticipation**: Prepare audience for action (pull back before forward).
- **Staging**: Direct viewer's attention to what's important.
- **Straight ahead vs pose-to-pose**:
  - **Pose-to-pose**: Plan key poses, then fill in between. Controlled.
  - **Straight ahead**: Animate frame by frame. Spontaneous, creative.
- **Follow through & overlapping action**:
  - **Follow through**: Parts continue moving after main action stops (hair, clothes).
  - **Overlapping**: Different parts move at different times (not all at once).
- **Slow in and slow out**: Gradual acceleration/deceleration at movement boundaries.
- **Arcs**: Natural motion follows curved paths, not straight lines.
- **Secondary action**: Supporting actions that add life without distracting.
- **Timing**: Number of frames for action. Conveys weight, emotion, intention.
- **Exaggeration**: Push movements further than real life for impact.
- **Solid drawing**: 3D form, weight, volume in 2D.
- **Appeal**: Charisma, interesting shapes, readability.

### 3. Keyframing Techniques
- **Manual keyframing**: Set keyframes at specific times and adjust values.
- **Auto-keyframe**: Software automatically creates keyframes when you change property.
- **Keyframe navigation**: Next/previous keyframe shortcuts.
- **Keyframe selection**: Select multiple keyframes to move/scale/delete together.
- **Keyframe interpolation**: Change interpolation type per keyframe (hold, linear, bezier).
- **Roving keyframes**: Keyframes that move along timeline when you add new ones.
- **Keyframe assistant**: Convert linear to ease, set ease percentages, rove.
- **Copy/paste keyframes**: Reuse animation on different layers/times.
- **Keyframe baking**: Convert expressions or complex animations to static keyframes.

### 4. Easing & Curves
- **Graph editor**: Visualize and edit animation curves.
- **Speed graph**: Shows velocity (speed and direction).
- **Value graph**: Shows property value over time.
- **Bezier handles**: Control curve shape. Longer handles = smoother.
- **Easy Ease**: Shortcut to make keyframes smooth (F9 in After Effects).
- **Ease percentages**: Control how much of movement is ease in/out (0-100%).
- **Continuous bezier**: Smooth through keyframe (no sharp corners).
- **Linear segments**: Sharp corners, constant speed.
- **Custom easing**: Draw custom curve shape for unique motion.
- **Ease and wizz**: Pre-built easing presets (more bounce, overshoot).

### 5. Animation Workflow
- **Plan**: Storyboard or sketch key poses/timing.
- **Blocking**: Set major key poses/timing with simple shapes. Get timing right.
- **Splining**: Convert linear to smooth bezier. Add in-betweens.
- **Polish**: Add follow-through, overlapping, secondary action.
- **Refine**: Adjust curves, timing, spacing. Fine-tune.
- **Test**: Play back at real speed. Does it feel right?
- **Render test**: Check final quality.

### 6. Motion Design Principles
- **Weight**: Heavier objects move slower, need more anticipation.
- **Exaggeration**: Push movements for clarity and impact.
- **Timing**: Number of frames determines perceived weight and emotion.
- **Squash & stretch**: Shows flexibility and life.
- **Arcs**: Natural movement follows curves.
- **Secondary action**: Adds richness without distracting.
- **Follow through**: Parts keep moving after main action stops.
- **Overlap**: Different parts start/stop at different times.
- **Staging**: Clear presentation of idea. Viewer should know what to look at.
- **Appeal**: Interesting shapes, readable silhouettes, charisma.

### 7. Animation Types
- **Looping**: Seamless repetition. Match start and end frames.
- **Ping-pong**: Forward then backward. Good for back-and-forth motion.
- **Bounce**: Elastic, decaying oscillation.
- **Wiggle**: Random small movements. Use `wiggle()` expression.
- **Path animation**: Layer follows a motion path.
- **Text animation**: Per-character, per-word, per-line.
- **Shape animation**: Animate shape layer paths, points.
- **Camera animation**: Move virtual camera through space.
- **3D animation**: Animate 3D layers with depth.

### 8. Expressions for Animation
- **time**: Current time in seconds.
- **index**: Layer index number.
- **loopOut()**: Loop animation after last keyframe.
- **loopIn()**: Loop animation before first keyframe.
- **wiggle(freq, amp)**: Random oscillation.
- **smooth(width, height)**: Smooth value based on neighbors.
- **ease(t, tMin, tMax, value1, value2)**: Smooth interpolation.
- **linear(t, tMin, tMax, value1, value2)**: Linear interpolation.
- **valueAtTime(t)**: Get property value at specific time.
- **thisComp.layer(name).property**: Reference another layer.
- **Math.sin(time*freq)*amp**: Sine wave oscillation.

### 9. Performance Considerations
- **Too many keyframes**: Can slow down playback. Use expressions when possible.
- **Complex expressions**: Can be slow. Optimize or pre-render.
- **High resolution**: Scale layers appropriately. Don't animate 4K if output is 1080p.
- **Effects on animated layers**: Heavy effects + animation = slower.
- **Pre-compose**: Complex animations in pre-comp, then use as footage.
- **Proxy**: Use proxy for high-res footage during animation.
- **Cache**: Enable disk cache. Pre-render heavy comps.

### 10. Common Animation Mistakes
- **Linear motion**: Everything moves at constant speed. Add easing.
- **No anticipation**: Actions start suddenly. Add wind-up.
- **No follow-through**: Things stop abruptly. Add settling.
- **All moving at once**: Chaos. Have some elements static.
- **Poor timing**: Too fast or too slow. Test at real speed.
- **No arcs**: Straight lines only. Add curves.
- **No weight**: Everything feels weightless. Add inertia.
- **Over-animating**: Everything moving = nothing stands out. Use stillness strategically.
- **Ignoring principles**: Animation feels stiff. Study 12 principles.
- **No staging**: Viewer doesn't know where to look. Guide attention.

## Advanced Techniques

### 1. Advanced Keyframing
- **Roving keyframes**: Keyframes that move when you add new ones. Maintains relative spacing.
- **Keyframe interpolation**: Change interpolation per keyframe (hold, linear, bezier, continuous).
- **Keyframe assistant**: Convert multiple keyframes to ease, set ease percentages, rove.
- **Keyframe snapping**: Snap keyframes to other keyframes, layers, markers.
- **Keyframe copying**: Copy keyframes to different layers/times.
- **Keyframe scaling**: Scale keyframes in time (compress/expand animation).
- **Keyframe reversing**: Reverse order of selected keyframes.
- **Keyframe looping**: Use loopOut(), loopIn(), loopOutDuration(), etc.

### 2. Graph Editor Mastery
- **Speed vs value**: Understand difference. Speed graph shows velocity.
- **Bezier handles**: Control curve shape. Longer = smoother.
- **Tangent types**: Auto bezier, continuous bezier, linear, hold.
- **Synchronizing curves**: Match curves across multiple properties for coordinated motion.
- **Custom easing**: Draw unique curve shapes for specific motion.
- **Cycle**: Create repeating patterns.
- **Bounce**: Create decaying bounce with keyframes or expressions.
- **Overshoot**: Go past target and settle back.

### 3. Motion Paths
- **Create path**: Draw path with pen tool. Layer follows it.
- **Path options**:
  - **Auto-orient**: Layer rotates to follow path direction.
  - **Perpendicular**: Rotate 90° to path.
  - **Free**: No rotation.
- **Path animation**: Path itself can animate (draw itself, move).
- **Multiple paths**: Combine paths for complex motion.
- **Path expressions**: Use path properties in expressions.
- **Mask paths as motion paths**: Use mask path as motion path.
- **Wiggle path**: Add random movement to path.

### 4. Parenting & Hierarchies
- **Parenting**: Child inherits parent's transform.
- **Uses**:
  - Group elements to move together.
  - Create rigs (arm: upper arm → lower arm → hand).
  - Pivot control via null object.
- **Null objects**: Invisible controllers. Parent layers to null for centralized control.
- **Layer hierarchy**: Parent-child chains. Transformations propagate down.
- **Expressions**: Reference parent (`thisComp.layer("parent").position`).
- **Pre-composing**: Group layers into nested comps. Cleaner timeline, reusable.
- **Essential graphics**: Create templates with modifiable parameters.

### 5. Advanced Expressions
- **Custom functions**: Create reusable functions.
- **Array manipulation**: Work with position, scale arrays.
- **Time-based**: `time`, `timeToFrames()`, `timeToSeconds()`.
- **Math**: `Math.sin()`, `Math.cos()`, `Math.random()`, `Math.atan2()`.
- **Conditional**: `if/else`, `switch`.
- **Loops**: `for`, `while` (use sparingly).
- **Global objects**: `thisComp`, `thisLayer`, `thisProperty`.
- **Layer methods**: `toComp()`, `fromComp()`, `toWorld()`, `fromWorld()`.
- **ValueAtTime()**: Get property value at specific time.
- **Smooth()**: Smooth interpolation.
- **Lookup table**: `lookup(table, progress)` for custom easing.
- **Inertia**: Simulate momentum with `velocity`, `acceleration`.

### 6. Character Animation Basics
- **Rigging**: Set up skeleton for character.
- **FK (Forward Kinematics)**: Rotate joints from parent to child.
- **IK (Inverse Kinematics)**: Move end effector (hand/foot), parent joints follow.
- **Puppet tool**: Pin and animate mesh for organic deformation.
- **Face rigging**: Control facial expressions with sliders.
- **Lip sync**: Animate mouth shapes to audio.
- **Walk cycles**: Animate walking motion. Loopable.
- **Idle animations**: Subtle motion when character not moving.

### 7. Physics & Simulation
- **Newtonian physics**: Position, velocity, acceleration.
- **Spring physics**: `spring()` expression for bouncy motion.
- **Gravity**: Constant downward acceleration.
- **Collision**: Detect and respond to collisions.
- **Particle systems**: Many small elements following rules.
- **Cloth simulation**: Simulate fabric movement.
- **Rigid body dynamics**: Solid objects with mass, bounce, friction.

### 8. Performance Optimization
- **Pre-render complex animations**: Render as movie and replace.
- **Use expressions sparingly**: Complex expressions calculate every frame.
- **Simplify effects**: Heavy effects slow down.
- **Reduce layer count**: Many layers = slower.
- **Cache work area**: Set work area to section you're working on.
- **Proxy workflow**: Use lower-res proxies during animation.
- **Resolution preview**: Work at half/third resolution.
- **Purge memory**: Regularly purge (Edit → Purge → All Memory).
- **Close other apps**: Free up RAM.
- **Use shape layers**: Faster than masked solids.

### 9. Workflow Tips
- **Use reference**: Load reference video to match timing.
- **Markers**: Use timeline markers for important beats or events.
- **Pre-comps**: Build complex animations in pre-comps.
- **Templates**: Save animations as presets or templates.
- **Version control**: Save incremental versions.
- **Keyboard shortcuts**: Learn shortcuts for keyframing, navigation.
- **Graph editor shortcuts**: Speed up curve editing.
- **Expression pick whip**: Quickly link properties.
- **Null objects**: Use as controllers for multiple layers.
- **Master properties**: Control comp parameters from parent comp.

### 10. Quality Control
- **Play at real speed**: Don't rely on slow preview. Watch at full speed.
- **Check on different devices**: Phone, tablet, computer.
- **Check at different resolutions**: Ensure animation looks good scaled.
- **Check frame by frame**: Look for glitches, pops, hitches.
- **Test loops**: If looping, ensure seamless.
- **Review timing**: Is motion too fast/slow? Adjust keyframe spacing.
- **Review easing**: Is motion mechanical? Add easing.
- **Review staging**: Is focus clear? Guide attention better.
- **Review weight**: Does motion feel right? Adjust timing and spacing.
- **Get feedback**: Others may see issues you miss.

## Related Skills

For complementary techniques, refer to:
- `./core-techniques/animation.md` - General animation principles (this file)
- `./core-techniques/pacing.md` - How animation timing affects overall pacing
- `./core-techniques/transitions.md` - Animated transitions
- `./core-techniques/text-animation.md` - Text-specific animation
- `./core-techniques/motion-graphics.md` - Motion graphics techniques
- `./styles/cinematic.md` - Subtle, realistic animation for film
- `./styles/dark-meme-dynamic.md` - Fast, flashy animation for memes
- `./styles/tiktok-news-hype.md` - Beat-synced, high-energy animation

