---
name: motion-graphics
description: Motion graphics techniques including composition, 3D layers, shape layers, and visual effects integration
metadata:
  tags: motion, graphics, composition, 3D, layers, VFX, visual-effects
---

## When to use

Use this skill whenever you need to create animated graphic elements that aren't tied to real footage - logos, icons, infographics, animated backgrounds, UI elements, and abstract visual elements. Motion graphics are essential for brand identity, data visualization, explainer videos, and enhancing any video with dynamic graphical content.

## Core Principles

### 1. What are Motion Graphics?
- **Definition**: Animated graphic design elements that move. Unlike character animation, motion graphics focus on shapes, text, logos, and abstract forms.
- **Applications**:
  - Logo animations and stingers
  - Lower thirds and nameplates
  - Infographics and data visualization
  - Animated backgrounds and textures
  - UI/UX animations (app demos)
  - Title sequences
  - Transitions and wipes
  - Abstract visual elements
- **Key difference from animation**: Motion graphics are typically non-narrative, non-character, design-focused.

### 2. Composition & Layout
- **Rule of thirds**: Place key elements along thirds lines or intersections.
- **Balance**: Distribute visual weight evenly (symmetrical or asymmetrical).
- **Hierarchy**: Most important element should be largest/brightest/most prominent.
- **Negative space**: Don't overcrowd. Empty space guides attention.
- **Alignment**: Elements should align to grid or each other. Avoid random placement.
- **Proximity**: Related elements should be grouped together.
- **Contrast**: Use size, color, weight to create distinction.
- **Movement direction**: Elements should move in logical directions (left-to-right for progress, down for decline).
- **Safe areas**: Keep important elements within title safe (90% frame).

### 3. Shape Layers & Vector Graphics
- **Shape layers**: Create and animate shapes (rectangles, ellipses, stars, polygons).
- **Path operations**: Merge, add, subtract, intersect shapes to create complex forms.
- **Fill & stroke**: Solid colors, gradients, patterns. Stroke weight and style.
- **Roundness**: Corners can be sharp or rounded. Rounded feels friendly, sharp feels technical.
- **Size & position**: Animate transform properties.
- **Scale**: Uniform or separate X/Y scaling.
- **Rotation**: 2D rotation or 3D rotation (if 3D layer).
- **Anchor point**: Pivot point for rotation/scale. Position carefully.
- **Precision**: Use snapping, grid, and numeric inputs for accuracy.
- **Vector advantage**: Infinitely scalable without quality loss.

### 4. 3D in Motion Graphics
- **3D layers**: Enable 3D switch on any layer. Adds Z-axis.
- **3D properties**: Position (X,Y,Z), Orientation (X,Y,Z), Rotation (X,Y,Z).
- **Camera layers**: Create virtual camera. Move through 3D space.
  - **Camera types**: One-node (look at point), two-node (point of interest).
  - **Camera settings**: Focal length (zoom), aperture, depth of field.
  - **Camera animation**: Fly-throughs, dolly, pan, tilt, roll.
- **Light layers**: Add lights to illuminate 3D layers.
  - **Light types**: Parallel (sun), spot, point, ambient.
  - **Light properties**: Intensity, color, falloff, shadow.
  - **Material options**: 3D layers have cast/receive shadows, accept lights.
- **3D space navigation**: Use different views (top, left, perspective) to position.
- **3D compositing**: Combine 2D and 3D layers. 2D layers always face camera (billboard).
- **Depth of field**: Blur layers based on distance from camera. Adds cinematic depth.
- **3D motion**: Parallax effect - layers move at different speeds based on Z position.

### 5. Keyframing & Animation Basics
- **Keyframe**: A point in time with a property value.
- **Linear interpolation**: Constant speed between keyframes. Mechanical.
- **Bezier interpolation**: Smooth acceleration/deceleration. Natural.
- **Easy Ease**: Shortcut to make keyframes smooth.
- **Graph editor**: Visualize and fine-tune animation curves.
- **Keyframe spacing**: Closer keyframes = faster movement, farther = slower.
- **Hold keyframes**: Constant value until next keyframe (no interpolation).
- **Keyframe assistant**: Convert linear to ease, ease percentages, roving.
- **Animation principles applied**:
  - **Ease in/out**: Start slow, speed up, slow down.
  - **Anticipation**: Prepare for movement (pull back before forward).
  - **Follow-through**: Overshoot and settle back.
  - **Arcs**: Move on curved paths, not straight lines.
  - **Squash & stretch**: Deform for organic feel.
  - **Exaggeration**: Make movements more dramatic than real.
  - **Timing**: Speed of action conveys weight and emotion.

### 6. Parenting & Hierarchies
- **Parenting**: Child layer inherits transform of parent.
- **Use cases**:
  - Group elements (logo + text) to move together.
  - Create rigs (arm: upper arm → lower arm → hand).
  - Pivot points: Parent to null object to control multiple layers.
- **Null objects**: Invisible layers used as controllers. Parent layers to null for centralized control.
- **Layer hierarchy**: Parent-child relationships create chains.
- **Expressions**: Can reference parent layer (`thisComp.layer("parent").position`).
- **Pre-composing**: Group layers into nested compositions. Cleaner timeline.

### 7. Masks & Track Mattes
- **Mask**: Vector shape that reveals/hides part of layer.
- **Mask types**: Rectangle, ellipse, pen tool (custom).
- **Mask operations**: Add, subtract, intersect, difference.
- **Mask feather**: Soft edges. Creates blend.
- **Mask expansion**: Grow/shrink mask.
- **Track matte**: One layer uses another layer's alpha as mask.
  - **Alpha matte**: Uses transparency of matte layer.
  - **Alpha inverted**: Inverts matte.
  - **Luma matte**: Uses brightness of matte layer.
  - **Luma inverted**: Inverts luma matte.
- **Use cases**:
  - Text reveal (text as matte for video).
  - Shape reveals (circle expands to reveal).
  - Layer masking (cut out shapes).
  - Composite elements.

### 8. Effects & Presets
- **Effects categories**:
  - **Blur**: Gaussian, radial, motion blur, zoom.
  - **Distort**: warp, bulge, displacement, ripple.
  - **Generate**: gradients, lightning, scribble, cell pattern.
  - **Stylize**: emboss, posterize, glitch, find edges.
  - **Color correction**: curves, hue/saturation, color balance.
  - **Simulation**: particle systems (CC Particle World, Particular).
  - **Audio**: audio waveform, audio spectrum (react to sound).
- **Presets**: Save effect combinations for reuse.
- **Animation presets**: Save keyframed animations as presets.
- **Third-party plugins**: Trapcode (Particular, Form), Element 3D, Optical Flares, etc.
- **Expression controls**: Slider, color, point, checkbox controls for user-adjustable presets.

### 9. Expressions & Automation
- **What is expression**: JavaScript-based code that calculates property value.
- **When to use**: Repetitive animation, physics, linking properties, procedural generation.
- **Common expressions**:
  - `time` - current time in seconds.
  - `index` - layer index number.
  - `thisComp.layer("name").position` - reference another layer.
  - `loopOut()` - loop animation.
  - `wiggle(freq, amp)` - random oscillation.
  - `linear(t, tMin, tMax, value1, value2)` - map time to range.
  - `ease(t, tMin, tMax, value1, value2)` - smooth interpolation.
- **Expression pick whip**: Drag to link properties visually.
- **Expression controls**: Add to null layer for user-adjustable parameters.
- **Performance**: Expressions calculate every frame. Complex expressions can slow down.

### 10. Rendering & Export
- **Render queue**: Add composition, set settings, render.
- **Output module**: Choose codec, format, color depth.
- **Alpha channel**: Needed for transparency. Use QuickTime Animation, PNG sequence, or WebM.
- **Render settings**:
  - **Quality**: Best, Draft, Wireframe.
  - **Resolution**: Full, Half, Third, Custom.
  - **Frame rate**: Match composition or override.
  - **Field render**: None for progressive.
  - **Duration**: Work area or full comp.
- **Export formats**:
  - **Video**: H.264 (MP4), ProRes, DNxHD.
  - **Image sequence**: PNG (lossless, alpha), JPEG.
  - **GIF**: For web, limited colors.
- **Render farm**: Use for complex projects (Renderstreet, Qube).

## Technical Guidelines

### Software & Tools
- **After Effects**: Industry standard for motion graphics.
- **Cinema 4D**: 3D motion graphics (integrated with AE via Cineware).
- **Blender**: Free 3D creation suite. Can be used for motion graphics.
- **Illustrator**: Create vector graphics, import to AE as shape layers or footage.
- **Photoshop**: Create layered graphics, import as composition.
- **Premiere Pro**: Basic motion graphics, but AE is more powerful.
- **DaVinci Resolve**: Fusion page for motion graphics/compositing.

### Best Practices
- **Organize layers**: Name layers, use pre-comps, color code.
- **Use shape layers over masks**: Shape layers are more editable.
- **Master properties**: Control comp parameters from parent comp.
- **Null objects for control**: Use nulls as controllers for animation.
- **Expression controls**: Make presets customizable.
- **Save presets**: Reuse common animations.
- **Render tests**: Render small segments before full render.
- **Proxy workflow**: Use proxies for high-res footage during editing.
- **Cache**: Enable disk cache for faster preview.
- **Resolution preview**: Work at half/third resolution for smooth playback.

### Performance Optimization
- **Pre-render complex comps**: Render as movie and replace.
- **Simplify effects**: Heavy effects (blur, fractal noise) slow down.
- **Reduce layer count**: Many layers = slower.
- **Use shape layers**: Faster than masked solids.
- **Avoid continuous rasterization on vector**: Only when needed.
- **Cache work area**: Set work area to section you're working on.
- **Purge memory**: Regularly purge (Edit → Purge → All Memory).
- **Close other apps**: Free up RAM.

### Color Management
- **Working space**: sRGB for web, Rec.709 for video.
- **Monitor calibration**: Essential for accurate color.
- **8-bit vs 16-bit**: 16-bit for gradients, reduces banding.
- **Color profiles**: Embed or assign correctly.
- **Render color depth**: 16-bit or 32-bit for high quality.

## Common Pitfalls to Avoid

- **Too much motion**: Everything moving at once creates visual chaos. Use stillness strategically.
- **Poor timing**: Animations too fast (can't follow) or too slow (boring).
- **No hierarchy**: All elements same size/color. Viewer doesn't know where to look.
- **Overusing effects**: Drop shadows, glows, strokes on everything looks cheap.
- **Bad easing**: Linear animation looks robotic. Always use some ease.
- **Pixelation**: Scaling vector layers too much? Should be infinite. Scaling footage too much = pixelated.
- **Forgetting safe area**: Text/graphics cut off on some screens.
- **Inconsistent style**: Different fonts, colors, animation styles throughout. Establish style guide.
- **Complex timelines**: No pre-composing, everything in one comp = mess.
- **No organization**: Unnamed layers, no grouping. Impossible to edit later.
- **Ignoring composition**: Elements placed randomly, not aligned.
- **Overcomplicating**: Simple solution usually better than complex.
- **Not checking on different screens**: What looks good on 27" monitor may be unreadable on phone.
- **Forgetting audio**: Motion graphics often need sound effects/music to feel complete.
- **No concept of weight**: All elements feel same weight. Use scale, speed, opacity to create visual weight hierarchy.

## Advanced Techniques

### 1. Advanced 3D
- **3D camera tracking**: Track real camera movement and integrate 3D elements.
- **3D lights & shadows**: Use lights to create realistic shadows and highlights.
- **Depth of field**: Animate focus pulls (rack focus).
- **3D text**: Extrude text, animate through 3D space.
- **3D particles**: Particles in 3D space with depth parallax.
- **Reflections**: Use floor with reflection or duplicate layer with opacity/mask.
- **3D matte painting**: Create 2.5D environments with layered planes.

### 2. Advanced Compositing
- **Blend modes**: Multiply, screen, overlay, add for creative compositing.
- **Track matte combos**: Multiple matte layers for complex reveals.
- **Stencil alpha**: Use layer as stencil for all below.
- **Pre-multiplied alpha**: Understanding alpha handling.
- **Light wrap**: Make foreground blend into background.
- **Edge blending**: Soften edges to integrate elements.
- **Color matching**: Match color/lighting of foreground and background.

### 3. Advanced Animation
- **Animation principles deep dive**:
  - **Slow in/out**: Custom bezier handles for natural motion.
  - **Follow through & overlapping action**: Secondary motion.
  - **Secondary action**: Supporting actions that add life.
  - **Exaggeration**: Push animation for impact.
- **Graph editor mastery**:
  - **Speed graph**: Visualize velocity.
  - **Value graph**: Visualize property values.
  - **Bezier handles**: Control interpolation shape.
  - **Roving keyframes**: Keyframes that move along timeline.
  - **Keyframe interpolation**: Continuous vs hold.
- **Motion paths**: Draw custom paths for layers to follow.
- **Text animator advanced**: Per-character 3D, range selectors, wiggly.
- **Shape layer animation**: Path animation, merge paths, trim paths.

### 4. Particle Systems
- **After Effects built-in**: CC Particle World, CC Particle Systems II.
- **Third-party**: Trapcode Particular, Form, Stardust.
- **Particle parameters**:
  - **Emitter**: Position, type (point, box, layer, grid), emission rate.
  - **Particle**: Type (sphere, sprite, cloud), size, opacity, color.
  - **Physics**: Gravity, wind, turbulence, repulsion.
  - **Aux system**: Particles spawn other particles.
- **Uses**:
  - Stars, dust, snow, rain.
  - Abstract backgrounds.
  - Text/logo reveals (particles assemble).
  - Energy effects (fire, smoke, magic).
- **Particle rendering**: 3D particles, shadow casting, motion blur.

### 5. Expressions Mastery
- **Custom functions**: Create reusable functions.
- **Array manipulation**: Work with multiple values (position, scale).
- **Time-based**: `time`, `timeToFrames()`, `timeToSeconds()`.
- **Math functions**: `Math.sin()`, `Math.cos()`, `Math.random()`.
- **Conditional logic**: `if/else`, `switch`.
- **Loops**: `for`, `while` (use sparingly, performance).
- **Array methods**: `join()`, `split()`, `slice()`.
- **Global comp objects**: `thisComp`, `thisLayer`, `thisProperty`.
- **Layer methods**: `toComp()`, `fromComp()`, `toWorld()`, `fromWorld()`.
- **ValueAtTime()**: Get property value at specific time.
- **Smooth()**: Smooth interpolation.
- **Lookup table**: `lookup(table, progress)` for custom easing.

### 6. Data-Driven Motion Graphics
- **JSON import**: Import JSON data to drive animations.
- **CSV/TSV parsing**: Use expressions to read data files.
- **Dynamic text**: Text layers linked to data sources.
- **Charts & graphs**: Animate bar charts, pie charts, line graphs from data.
- **Counters**: Animated numbers counting up/down.
- **Real-time data**: Connect to APIs via scripts (ExtendScript, CEP panels).
- **Template systems**: Create reusable templates with placeholders.

### 7. Advanced Text Animation
- **Text animator groups**: Position, scale, rotation, opacity, etc.
- **Range selectors**: Control which characters/words/lines are affected.
  - **Based on**: Characters, words, lines.
  - **Units**: Index, percent, percentage of line.
  - **Based on**: Original, current, random.
- **Properties**: Enable/disable, offset, mode (add, subtract, etc.).
- **Advanced text animators**:
  - **Blur**: Animate blur per character.
  - **Fill/Stroke color**: Animate color.
  - **Tracking/ Kerning**: Animate letter spacing.
  - **Line spacing**: Animate line height.
  - **Rotation**: Per-character rotation.
  - **Scale**: Per-character scale.
- **Expression selectors**: Use expressions for complex selection logic.
- **Text path**: Make text follow a path.
- **3D text**: Enable 3D on text layer, add lights, shadows.

### 8. Advanced Shape Layers
- **Path operations**:
  - **Merge paths**: Combine multiple paths into one.
  - **Add, subtract, intersect, difference**: Boolean operations.
  - **Repeater**: Duplicate shape with transforms.
  - **Trim paths**: Animate path drawing (like handwriting).
  - **Pucker & Bloat**: Inflate or deflate shapes.
- **Shape layer expressions**: Animate path points, control with sliders.
- **Shape layer utilities**:
  - **Create HUD elements**: Circles, arcs, tick marks.
  - **Animated backgrounds**: Moving gradients, patterns.
  - **Lower thirds**: Animated bars, boxes.
- **Shape layer vs mask**: Shape layers are editable, masks are destructive.

### 9. Advanced Effects
- **Particle systems**:
  - **Particular**: Advanced particles with physics, turbulence, etc.
  - **Form**: Particles form shapes/text.
  - **Stardust**: Node-based particle system.
- **3D plugins**:
  - **Element 3D**: Import and animate 3D models in AE.
  - **Invigorator**: 3D text and shapes.
- **Optical effects**:
  - **Optical Flares**: Realistic lens flares.
  - **Knoll Light Factory**: Advanced lens flares.
- **Glitch & distortion**:
  - **RG split**: Chromatic aberration.
  - **TV simulation**: Scan lines, noise, roll.
  - **Displacement**: Use map to distort.
- **Simulation**:
  - **Fractal**: Generate procedural patterns.
  - **Wave world**: 2D water simulation.
- **Stylization**:
  - **Cartoon**: Cel-shading effect.
  - **Posterize**: Reduce colors.
  - **Echo**: Motion trails.

### 10. Workflow Automation
- **Scripting**: Use ExtendScript (JavaScript) to automate tasks.
- **CEP panels**: Create custom UI panels.
- **Templates**: Save comps as templates for reuse.
- **Batch processing**: Use scripts to process multiple files.
- **Render automation**: Watch folders, auto-render.
- **Project organization**: Use custom project structure.
- **Version control**: Use with Git (though AE files are binary).

## Workflow Recommendations

1. **Concept & storyboard**: Sketch ideas, plan animations.
2. **Asset preparation**: Create/collect graphics, icons, logos. Vector preferred.
3. **Project setup**: Create comp with correct settings (resolution, frame rate, duration).
4. **Import assets**: Organize in project panel with folders.
5. **Pre-compose**: Group related layers. Create nested comps.
6. **Build base layer**: Static layout of all elements.
7. **Animate entrance**: Bring elements in with appropriate animations.
8. **Animate main action**: Core motion graphics sequence.
9. **Animate exit**: Remove elements gracefully.
10. **Add effects**: Apply effects, adjust timing.
11. **Add audio**: Sound effects, music, voiceover.
12. **Review & refine**: Watch entire comp. Fix timing, smooth curves.
13. **Render test**: Small segment to check quality.
14. **Final render**: Full comp at proper settings.
15. **Export for delivery**: Encode to final format if needed.

## Related Skills

For complementary techniques, refer to:
- `./core-techniques/animation.md` - General animation principles
- `./core-techniques/transitions.md` - Motion graphics transitions
- `./core-techniques/text-animation.md` - Kinetic typography
- `./core-techniques/color-grading.md` - Color for motion graphics
- `./styles/cinematic.md` - Subtle, elegant motion graphics
- `./styles/gameplay.md` - Dynamic, game-like motion graphics
- `./styles/dark-meme-dynamic.md` - Fast, flashy meme motion graphics
- `./styles/tiktok-news-hype.md` - Beat-synced, high-energy motion graphics

