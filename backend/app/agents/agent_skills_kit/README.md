# Video Editing Agent Skills Kit

A comprehensive collection of instructional skills for AI agents performing video editing tasks. This kit provides domain-specific knowledge covering editing styles, core techniques, and best practices for creating professional videos.

## 📁 Structure

The skills are organized into three main categories:

```
agent_skills/
├── README.md                 # This file - kit documentation
├── styles/                   # Editing style skills (what to achieve)
│   ├── cinematic.md
│   ├── dark-tutorial.md
│   ├── dark-meme-dynamic.md
│   ├── gameplay.md
│   └── tiktok-news-hype.md
├── core-techniques/          # Technical skill files (how to do it)
│   ├── animation.md
│   ├── audio-sync.md
│   ├── color-grading.md
│   ├── motion-graphics.md
│   ├── pacing.md
│   ├── sound-design.md
│   ├── text-animation.md
│   └── transitions.md
└── rules/                    # Foundational rules (supporting knowledge)
    ├── animations.md
    ├── assets.md
    ├── audio.md
    ├── fonts.md
    ├── parameters.md
    ├── sequencing.md
    ├── subtitles.md
    └── timing.md
```

## 🎯 How to Use This Kit

### 1. Understanding the Hierarchy

- **Styles** (`styles/`): Define *what* you want to achieve - the overall look, feel, and rhythm of the final video. Each style skill teaches the agent how to produce a specific type of video (e.g., cinematic film, TikTok news, gameplay montage).

- **Core Techniques** (`core-techniques/`): Teach *how* to implement specific technical aspects. These are reusable skills that can be applied across different styles (e.g., color grading, text animation, audio synchronization).

- **Rules** (`rules/`): Provide foundational knowledge and best practices for working with specific elements (assets, fonts, timing, parameters). These support both styles and core techniques.

### 2. Selecting Skills for a Task

When given a video editing task, the agent should:

1. **Identify the primary style** needed (e.g., "cinematic," "TikTok news," "gameplay"). Load the corresponding `styles/[style].md` file.
2. **Determine required techniques** based on the task description (e.g., needs text animations, color grading, audio sync). Load relevant `core-techniques/*.md` files.
3. **Consult rules** for specific element guidance (e.g., if working with fonts, load `rules/fonts.md`).
4. **Combine knowledge** from all loaded skills to execute the task.

### 3. Skill Selection Examples

| Task | Primary Style | Core Techniques | Rules |
|------|---------------|-----------------|-------|
| Cinematic short film | `styles/cinematic.md` | `color-grading.md`, `pacing.md`, `audio-sync.md` | `assets.md`, `timing.md`, `sequencing.md` |
| TikTok news update | `styles/tiktok-news-hype.md` | `text-animation.md`, `audio-sync.md`, `transitions.md` | `fonts.md`, `timing.md`, `subtitles.md` |
| Gameplay montage | `styles/gameplay.md` | `motion-graphics.md`, `sound-design.md`, `pacing.md` | `assets.md`, `audio.md` |
| Dark mystery tutorial | `styles/dark-tutorial.md` | `text-animation.md`, `color-grading.md`, `audio-sync.md` | `fonts.md`, `parameters.md` |
| Meme compilation | `styles/dark-meme-dynamic.md` | `transitions.md`, `sound-design.md`, `pacing.md` | `assets.md`, `timing.md` |

### 4. Loading Skills

Skills are loaded by the agent system when needed. The agent should reference the appropriate skill file based on the task requirements. Each skill file contains:

- **When to use**: Context for applying this skill.
- **Core Principles**: Fundamental concepts and guidelines.
- **Technical Guidelines**: Specific parameters, formats, and workflows.
- **Common Pitfalls**: What to avoid.
- **Advanced Techniques**: Optional enhancements for experienced execution.
- **Related Skills**: Cross-references to complementary skills.

## 📚 Available Skills Overview

### Styles

#### `styles/cinematic.md`
**Cinematic Film Editing**

Teaches the art of creating film-quality videos with a cinematic look and feel. Covers:
- Cinematic composition and framing
- Film-like color grading (teal & orange, desaturated shadows)
- Slow, deliberate pacing (2-5s shots)
- Smooth transitions (dissolves, match cuts)
- Aspect ratios (2.35:1, 2.39:1 letterbox)
- Camera movement simulation
- Sound design for immersion
- Narrative structure and emotional beats

**Best for**: Short films, documentaries, brand stories, music videos, any content requiring a premium, movie-like aesthetic.

#### `styles/dark-tutorial.md`
**Dark Aesthetic Tutorial Videos**

Specialized for long-form explanatory content with a dark, moody aesthetic while remaining engaging. Covers:
- Dark theme design (dark backgrounds, high-contrast text)
- Maintaining engagement in long content (5-15 min)
- Text-heavy presentation with clear hierarchy
- Screen recording integration
- Pacing strategies to avoid boredom
- Visual variety without showing face
- Chapter markers and section breaks
- Call-to-action placement

**Best for**: Technical tutorials, explainer videos, educational content, software walkthroughs, commentary videos.

#### `styles/dark-meme-dynamic.md`
**Dynamic Dark Meme Compilations**

Fast-paced, high-energy editing for meme compilations and viral content without showing the creator's face. Covers:
- Extreme pacing (0.3-1s shots)
- Rapid-fire meme transitions
- Sound effect punctuation (vine booms, impact sounds)
- Text overlays with meme captions
- Music-driven editing (hype phonk, meme songs)
- Visual effects (glitch, zoom, shake)
- Looping structure for infinite scroll
- Viral format optimization

**Best for**: Meme compilations, reaction edits, TikTok/Reels meme content, YouTube meme videos, dark humor edits.

#### `styles/gameplay.md`
**Gameplay Video Editing**

Techniques for editing gaming content - from casual playthroughs to professional montages. Covers:
- Highlight reel construction (clutch plays, fails, funny moments)
- Pacing for different game genres (FPS fast, RPG slow)
- Integration of facecam (positioning, sizing)
- Commentary overlay and audio balance
- Visual effects for gameplay (hit markers, kill counters, damage numbers)
- Color grading for game footage (saturation, contrast)
- Thumbnail creation principles
- Platform-specific formats (YouTube, Twitch clips, TikTok highlights)

**Best for**: Gaming montages, playthrough videos, speedruns, tutorial content, esports highlights, streaming highlights.

#### `styles/tiktok-news-hype.md`
**TikTok News with Tense/Hype Rhythm**

High-energy, attention-grabbing news format optimized for TikTok's algorithm and audience. Covers:
- Breaking news aesthetic with modern twist
- Tense rhythm through quick cuts (0.5-1.5s)
- Beat-synced editing to high-BPM music (140-180)
- Whip pans, glitch transitions, zoom effects
- Layered information delivery (voiceover + text + graphics)
- 0-3 second hook requirements
- Text hierarchy and pop-in animations
- Sound design punctuation (whoosh, impact, alarm)

**Best for**: News summaries, trending topic updates, urgent announcements, viral news content, social media news bites.

### Core Techniques

#### `core-techniques/animation.md`
**Animation Fundamentals**

Principles of animation applied to video editing: keyframes, easing, motion paths, physics-based motion, and animation workflows.

#### `core-techniques/audio-sync.md`
**Audio Synchronization**

Techniques for precise synchronization between audio and visual elements: beat matching, phoneme sync, action sync, sound effect timing, and audio ducking.

#### `core-techniques/color-grading.md`
**Color Grading**

Color correction and grading techniques: exposure adjustment, white balance, contrast curves, LUTs, color palettes, stylistic looks, and platform-specific color requirements.

#### `core-techniques/motion-graphics.md`
**Motion Graphics**

Creating animated graphics, lower thirds, logos, infographics, and UI elements. Covers shape layers, paths, expressions, and template-based motion design.

#### `core-techniques/pacing.md`
**Pacing & Rhythm**

Controlling the speed and flow of video: shot duration, rhythm patterns, tension curves, platform-specific pacing, and strategies for maintaining engagement through timing.

#### `core-techniques/sound-design.md`
**Sound Design**

Creating and integrating sound effects, ambience, foley, and audio layering. Covers sound effect libraries, mixing, EQ, compression, and creating immersive audio environments.

#### `core-techniques/text-animation.md`
**Text Animation**

Animating text elements: typewriter, pop-in, slide, glitch, kinetic typography, text-on-path, and best practices for readability during motion.

#### `core-techniques/transitions.md`
**Transitions**

Types of transitions and when to use them: cuts, dissolves, wipes, whip pans, zooms, glitch effects, match cuts, and creating seamless scene changes.

### Rules

#### `rules/animations.md`
Animation best practices for Remotion projects.

#### `rules/assets.md`
Importing and managing images, videos, audio, and fonts. Covers formats, organization, optimization, and asset pipelines.

#### `rules/audio.md`
Using audio in video projects: importing, trimming, volume, speed, pitch, and audio effects.

#### `rules/fonts.md`
Font selection, loading, and typography best practices. Covers readability, licensing, sizing, hierarchy, and platform-specific typography.

#### `rules/parameters.md`
Making videos parametrizable with Zod schemas, UI controls, and data-driven rendering for templates and automation.

#### `rules/sequencing.md`
Sequencing patterns: delay, trim, duration control, and arranging elements in time.

#### `rules/subtitles.md`
Best practices for captions and subtitles: formatting, positioning, timing, and accessibility.

#### `rules/timing.md`
Timing concepts, duration control, time remapping, beat alignment, and time-based editing techniques.

## 🔧 How to Apply Skills

### Single Style Task

For a straightforward task requiring one style, load only that style skill plus any necessary core techniques and rules mentioned in its "Related Skills" section.

**Example**: "Create a cinematic short film"
- Load: `styles/cinematic.md`
- Also load: `core-techniques/color-grading.md`, `core-techniques/pacing.md`, `core-techniques/audio-sync.md`, `rules/assets.md`, `rules/timing.md`, `rules/sequencing.md`

### Multi-Style Hybrid Task

For tasks combining multiple styles, load all relevant style skills and synthesize their principles. Identify which style dominates and use others for specific elements.

**Example**: "Create a TikTok video that combines news reporting with gameplay highlights"
- Primary: `styles/tiktok-news-hype.md` (overall structure and rhythm)
- Secondary: `styles/gameplay.md` (gameplay-specific techniques)
- Core: `core-techniques/audio-sync.md`, `core-techniques/transitions.md`
- Rules: `rules/timing.md`, `rules/fonts.md`

### Technique-Focused Task

When the task specifies a technique rather than a style, load the relevant core technique skill and adapt it to the appropriate style context.

**Example**: "Add kinetic typography to a tutorial video"
- Style: `styles/dark-tutorial.md` (context)
- Core: `core-techniques/text-animation.md` (kinetic typography)
- Rules: `rules/fonts.md`, `rules/timing.md`

## 📖 Skill Format & Conventions

All skill files follow a consistent structure:

```
---
name: skill-name
description: Brief description
metadata:
  tags: [comma, separated, tags]
---

## When to use
Explanation of when this skill applies.

## Core Principles
Fundamental concepts with bullet points and explanations.

## Technical Guidelines
Specific parameters, formats, numbers, and workflows.

## Common Pitfalls to Avoid
List of mistakes to watch out for.

## Advanced Techniques
Optional enhancements for experienced execution.

## When NOT to Use This Style
Contraindications and limitations.

## Related Skills
Links to complementary skills in the kit.
```

## 🎓 Best Practices for Skill Selection

1. **Start with the style**: The style skill defines the overall vision and should be your first reference.
2. **Read Related Skills**: Each style skill lists recommended core techniques and rules. Load those.
3. **Don't over-load**: Only load skills directly relevant to the task. Too many skills can cause confusion.
4. **Cross-reference**: When in doubt, check multiple skills for different perspectives on the same technique.
5. **Prioritize**: If skills conflict, the style skill usually takes precedence as it defines the final aesthetic.
6. **Iterate**: If the first attempt doesn't match expectations, review related skills for missed techniques.

## 🔄 Skill Maintenance & Extension

### Adding New Skills

When creating new skills, follow the established format and place them in the appropriate directory:
- New editing styles → `styles/`
- New technical techniques → `core-techniques/`
- New foundational rules → `rules/`

Update the `Related Skills` sections in existing skills to reference new additions when relevant.

### Versioning

This skill kit uses semantic versioning in skill metadata when updates are breaking changes. Minor updates (additional examples, clarification) can be made without version changes.

### Contributing

When adding or modifying skills:
1. Maintain consistent structure and formatting
2. Keep descriptions clear and actionable
3. Include specific numbers and parameters when applicable
4. Provide concrete examples of application
5. Document both what to do and what to avoid
6. Link to related skills for cross-pollination

## 📞 Support & Feedback

If you encounter issues with skill selection or need clarification on how to combine skills for a specific task, consult the individual skill files' "Related Skills" sections or review this README's selection examples.

---

*Last updated: 2025-02-04*
*Kit version: 1.0.0*

