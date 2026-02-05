---
name: assets
description: Importing and managing images, videos, audio, and fonts in video projects
metadata:
  tags: assets, media, import, images, videos, audio, management
---

## When to use

Use this skill whenever you need to bring external media files into your video project - images, videos, audio files, fonts, and other assets. Proper asset management ensures smooth workflow, fast rendering, and organized projects.

## Core Principles

### 1. Asset Types & Formats
- **Images**:
  - **Raster**: PNG (lossless, alpha), JPEG (lossy, photos), WebP (modern), TIFF (high quality).
  - **Vector**: SVG (scalable, small file size).
  - **Resolution**: Match or exceed project resolution. 1920x1080 for 1080p project.
  - **Color space**: sRGB for web, Rec.709 for video.
  - **Bit depth**: 8-bit standard, 16-bit for gradients.
- **Videos**:
  - **Codecs**: H.264 (universal), H.265 (efficient), ProRes (high quality), DNxHD.
  - **Container**: MP4, MOV, MXF, AVI.
  - **Frame rate**: Match project (24, 25, 30, 60 fps).
  - **Resolution**: Match project or higher (downscale better than upscale).
  - **Bit depth**: 8-bit 4:2:0 standard, 10-bit for color grading.
  - **Alpha channel**: ProRes 4444, QuickTime Animation for transparency.
- **Audio**:
  - **Formats**: WAV (uncompressed), AIFF, MP3 (lossy), M4A, OGG, FLAC.
  - **Sample rate**: 48kHz for video, 44.1kHz for music.
  - **Bit depth**: 16-bit delivery, 24-bit recording.
  - **Channels**: Mono (dialogue), stereo (music/SFX), 5.1 (surround).
- **Fonts**:
  - **Formats**: OTF, TTF, WOFF/WOFF2 (web).
  - **Licensing**: Ensure you have rights to use/embed.
  - **Style**: Match brand/tone (serif, sans-serif, display).
  - **Character set**: Support needed languages (CJK, Arabic, etc.).

### 2. Importing Assets
- **Linking vs embedding**:
  - **Link**: Reference external file. Project size small, but file must stay in same location.
  - **Embed**: Copy file into project. Project portable, but larger.
- **Import methods**:
  - **Drag and drop**: Simplest. Usually links.
  - **File → Import**: Choose file, set options.
  - **Media browser**: Browse and preview before import.
- **Import settings**:
  - **Footage interpretation**: Correct frame rate, pixel aspect ratio, color profile.
  - **Alpha channel**: Straight vs premultiplied.
  - **Audio**: Import audio or not.
  - **Motion**: Import as footage or composition (PSD, AI).

### 3. Asset Organization
- **Folder structure**:
  - `01_Footage` → `A_Raw`, `B_Processed`, `C_Stock`
  - `02_Audio` → `Music`, `SFX`, `Voiceover`, `Ambience`
  - `03_Graphics` → `Images`, `Logos`, `Icons`, `LowerThirds`
  - `04_Fonts` → `BrandFonts`, `SystemFonts`
  - `05_Comps` → `PreComps`, `Templates`
  - `06_Exports` → `Renders`, `Stills`
- **Naming conventions**:
  - `YYYYMMDD_Description_Version.ext`
  - `Scene01_Take03.mp4`
  - `Logo_Main_Black.png`
  - `Music_Background_Upbeat_01.wav`
- **Color coding**: Use project panel colors to categorize.
- **Labels**: Add metadata, tags, comments.
- **Bins/Folders**: Group related assets. Nest folders.
- **Favorites**: Mark frequently used assets.

### 4. Image Handling
- **Resolution**:
  - **Upscaling**: Avoid. Quality loss. Find higher-res source.
  - **Downscaling**: Fine. Use high-quality resampling (bicubic, Lanczos).
- **Aspect ratio**:
  - **Match to comp**: Crop or letterbox/pillarbox.
  - **Maintain**: Add background to fill.
  - **Distort**: Stretch to fit (usually bad).
- **Alpha channel**:
  - **PNG with transparency**: Use for overlays, logos.
  - **Premultiplied vs straight**: Most apps use straight alpha. Check import settings.
- **Color profile**:
  - **sRGB**: Web, social media.
  - **Rec.709**: Video.
  - **Linear**: For 3D rendering (After Effects).
  - **Convert if needed**: Use color management.
- **File format choice**:
  - **PNG**: Lossless, transparency. Best for graphics, logos.
  - **JPEG**: Photos, no transparency. Smaller.
  - **WebP**: Modern, good compression, transparency.
  - **TIFF**: High bit depth, layers (but large).
- **Image sequences**:
  - **Use for**: Frame sequences from 3D, frame exports.
  - **Import**: Select first file, check "footage" or "sequence".
  - **Advantages**: No codec, lossless, easy frame access.
  - **Disadvantages**: Many files, large storage.

### 5. Video Handling
- **Codec selection**:
  - **Editing**: ProRes, DNxHD, CineForm (intra-frame, easy to decode).
  - **Delivery**: H.264 (universal), H.265 (efficient), VP9 (web).
  - **Archival**: ProRes 4444, DNxHR, uncompressed.
- **Proxy workflow**:
  - **Why**: Edit with low-res proxies, render with full-res.
  - **How**: Create low-res copies (H.264, lower resolution). Link proxies, full-res for render.
  - **Toggle**: Switch between proxy/full during editing.
- **Conform/Reinterpret footage**:
  - **Frame rate**: 24fps → 30fps (add frames) or drop frames.
  - **Pixel aspect**: Anamorphic → square.
  - **Color profile**: Log → Rec.709.
  - **Alpha**: Straight ↔ premultiplied.
- **Trimming in project**:
  - **In/Out**: Set usable portion before adding to timeline.
  - **Subclips**: Create reusable subclips from master footage.
  - **Offline files**: If file missing, relink.
- **Video quality assessment**:
  - **Check focus**: Is footage sharp?
  - **Check exposure**: Over/underexposed?
  - **Check stability**: Shaky? Need stabilization.
  - **Check artifacts**: Compression artifacts, banding.

### 6. Audio Handling
- **Import settings**:
  - **Audio on/off**: Turn off for video-only clips.
  - **Mono/stereo**: Match source. Convert if needed.
  - **Sample rate conversion**: Usually automatic.
- **Audio waveform**:
  - **View**: Waveform or spectrogram.
  - **Zoom**: In to see transients, out to see overall.
  - **Peaks**: Watch for clipping (red).
- **Audio normalization**:
  - **Peak normalize**: Raise to 0 dBFS.
  - **Loudness normalize**: To target LUFS (-14, -23, etc.).
- **Audio tracks**:
  - **Separate tracks**: Dialogue, music, SFX, ambience.
  - **Color code**: Visual organization.
  - **Group**: Sub-mixes for processing.
- **Audio effects**:
  - **EQ**: Clean up frequencies.
  - **Compression**: Control dynamics.
  - **Noise reduction**: Remove hiss, hum.
  - **Reverb**: Add space.

### 7. Font Management
- **Font installation**:
  - **System fonts**: Already installed. Use directly.
  - **Project fonts**: Copy font files to project folder, load manually.
  - **Font activation**: Use font manager (Suitcase, FontBase) to activate/deactivate.
- **Font licensing**:
  - **Check EULA**: Can you embed in video? Usually yes for static text.
  - **Web fonts**: Different license. Don't use without permission.
  - **Open source**: Google Fonts, Adobe Fonts (included with subscription).
- **Font fallbacks**:
  - **Specify stack**: `font-family: 'CustomFont', Arial, sans-serif`.
  - **If font missing**: Use fallback. Test.
- **Font rendering**:
  - **Anti-aliasing**: Smooth edges. Subpixel for LCD.
  - **Hinting**: Aligns to pixel grid. Usually automatic.
  - **Size**: Large enough to be readable.
- **Dynamic font loading**:
  - **Web fonts**: Load via CSS `@font-face`.
  - **Performance**: Subset fonts (only needed characters).
  - **Fallback**: Show system font while loading.

### 8. Asset Optimization
- **Compression**:
  - **Images**: Use appropriate quality (80% JPEG often enough).
  - **Video**: Use high bitrate for editing, compress for delivery.
  - **Audio**: 320kbps MP3 fine for delivery, WAV for editing.
- **Resolution scaling**:
  - **Downscale high-res assets**: 4K → 1080p for 1080p project.
  - **Upscale low-res**: Avoid. Use AI upscaling if necessary.
- **File format conversion**:
  - **Convert to editing codec**: H.264 → ProRes for smooth editing.
  - **Convert to delivery codec**: After editing.
- **Asset deduplication**:
  - **Find duplicates**: Same file used multiple times. Use one instance.
  - **Unused assets**: Remove from project (but keep file if needed later).
- **Archiving**:
  - **Project archive**: Collect all assets into one folder for backup/delivery.
  - **Transcode**: Convert to stable format (ProRes, PNG sequence).
  - **Document**: Include readme with source info.

### 9. Asset Workflow
- **Ingest**:
  - **Rename**: Apply naming convention.
  - **Organize**: Place in appropriate folder.
  - **Transcode**: Convert to editing-friendly format if needed.
  - **Backup**: Copy to backup drive/cloud.
- **Logging**:
  - **Metadata**: Add keywords, descriptions, ratings.
  - **Thumbnails**: Generate preview images.
  - **Transcripts**: For dialogue, create transcript.
- **Preparation**:
  - **Color correct**: Apply LUTs or correction.
  - **Stabilize**: Shaky footage? Stabilize.
  - **Denoise**: Clean up noise.
  - **Crop/reframe**: Adjust aspect ratio.
- **Integration**:
  - **Import to project**: Link or embed.
  - **Organize in bins**: Color code, label.
  - **Create subclips**: Mark in/out points.
- **Maintenance**:
  - **Relink**: If files move, relink.
  - **Consolidate**: Collect all used assets for delivery.
  - **Prune**: Remove unused assets.

### 10. Asset Delivery & Handoff
- **Project packaging**:
  - **Collect files**: Gather all used assets.
  - **Transcode to safe formats**: ProRes, PNG, WAV.
  - **Include project file**: With relative paths.
  - **Document**: Readme with instructions, versions.
- **For client**:
  - **Export final video**: H.264 MP4, high bitrate.
  - **Provide source files**: If paid for, deliver project + assets.
  - **Specs**: Resolution, codec, frame rate, audio sample rate.
- **For archive**:
  - **Master file**: Highest quality (ProRes 4444, WAV).
  - **Project backup**: Save project file with all assets.
  - **Metadata**: Include description, date, version.

## Technical Guidelines

### Software-Specific
- **After Effects**:
  - **Import**: File → Import → Multiple files.
  - **Interpret footage**: Right-click → Interpret Footage.
  - **Proxy**: File → Set Proxy → Use project.
  - **Replace footage**: Right-click → Replace Footage.
- **Premiere Pro**:
  - **Media browser**: Browse and import.
  - **Project panel**: Organize bins.
  - **Link media**: If offline, link to new location.
  - **Proxy**: Create proxies, toggle.
- **DaVinci Resolve**:
  - **Media pool**: Import and organize.
  - **Clip attributes**: Change format, resolution.
  - **Optimized media**: Generate proxies.
  - **Consolidate**: Media → Consolidate.

### Best Practices
- **Keep originals**: Never overwrite source files.
- **Use proxies for 4K+**: Smooth editing.
- **Organize from start**: Good habits save time.
- **Name clearly**: Find assets quickly.
- **Use subclips**: Reuse portions without duplicating.
- **Check before import**: Ensure quality, correct format.
- **Backup regularly**: Drive failure happens.
- **Use relative paths**: For project portability.
- **Clean project**: Remove unused assets before delivery.
- **Document decisions**: Note why certain assets chosen.

## Common Pitfalls to Avoid

- **Missing files**: Relink errors. Keep folder structure consistent.
- **Wrong codec**: H.264 editing = choppy. Use editing codec.
- **Low resolution**: Pixelated when scaled. Use high-res source.
- **No alpha**: Need transparency but file doesn't have it. Use PNG with alpha.
- **Color space mismatch**: sRGB vs Rec.709. Colors look wrong.
- **Frame rate mismatch**: 24fps → 30fps judder. Conform properly.
- **Audio sample rate mismatch**: 44.1kHz → 48kHz resampling quality loss.
- **Font not found**: Text falls back to system font. Embed or outline.
- **Unlicensed assets**: Copyright infringement. Use properly licensed.
- **Huge project size**: Embedding everything. Use links, proxies.
- **No organization**: Chaos. Can't find anything.
- **Overwriting originals**: Source files lost. Always duplicate.
- **No backup**: Drive failure = lost work. Backup religiously.
- **Wrong aspect ratio**: Stretched or letterboxed unexpectedly.
- **Compressed editing**: Editing H.264 directly = poor performance. Transcode.

## Advanced Techniques

### 1. Asset Management Systems
- **Digital Asset Management (DAM)**:
  - **Software**: Adobe Bridge, Canto, Bynder.
  - **Features**: Catalog, search, metadata, versioning.
- **Project management**:
  - **Trello, Asana**: Track asset status.
  - **Spreadsheets**: Asset inventory.
- **Cloud storage**:
  - **Google Drive, Dropbox, S3**: Centralized access.
  - **Sync**: Keep local and cloud in sync.
- **Version control for assets**: Git LFS, Perforce Helix Core.

### 2. Advanced Transcoding
- **Batch processing**:
  - **FFmpeg**: Command-line batch convert.
  - **Adobe Media Encoder**: Watch folders.
  - **HandBrake**: Free batch converter.
- **Transcode presets**: Save settings for repeat use.
- **Format conversion**:
  - **H.264 → ProRes**: `ffmpeg -i input.mp4 -c:v prores -profile:v 3 output.mov`
  - **Image sequence → video**: `ffmpeg -i img%04d.png -c:v prores output.mov`
- **Proxy generation**:
  - **Lower resolution**: 1/4 or 1/2 size.
  - **Lower bitrate**: H.264 high speed.
  - **Same frame rate**: Match original.

### 3. Metadata & Tagging
- **EXIF/IPTC**:
  - **Camera info**: Make, model, exposure.
  - **Description**: Title, caption, keywords.
  - **Copyright**: Owner, usage rights.
- **Custom metadata**:
  - **Project ID**: Link to project.
  - **Version**: v1, v2, final.
  - **Status**: approved, rejected, needs review.
- **Search**: Use metadata to find assets quickly.
- **Automation**: Scripts to read/write metadata.

### 4. Asset Pipeline Automation
- **Watch folders**:
  - **Drop folder**: Place file → auto-import, transcode, organize.
  - **Software**: Adobe Watch Folder, custom scripts.
- **API integration**:
  - **Cloud storage API**: Auto-download new assets.
  - **Asset manager API**: Query and fetch assets.
- **Scripting**:
  - **ExtendScript (AE)**: Automate import, organization.
  - **Python**: Batch process, rename, convert.
- **Workflow automation**:
  - **Zapier, Make**: Connect services.
  - **Custom pipelines**: End-to-end asset flow.

### 5. Color Management
- **Color profiles**:
  - **sRGB**: Web, social.
  - **Rec.709**: Standard video.
  - **Rec.2020**: UHD/HDR.
  - **Log**: Flat profiles (S-Log, C-Log). Need LUTs.
- **LUTs (Lookup Tables)**:
  - **Technical**: Convert log → Rec.709.
  - **Creative**: Stylized looks.
  - **1D LUT**: Luminance only.
  - **3D LUT**: Full color transform.
- **ICC profiles**: For print, but can use for video.
- **Monitor calibration**: Essential for accurate color.
- **Color space conversion**:
  - **From sRGB to Rec.709**: Use color management.
  - **From log to linear**: Apply LUT.

### 6. Asset Security & Rights
- **Licensing**:
  - **Royalty-free**: One-time purchase, use forever.
  - **Rights-managed**: Specific usage, time-limited.
  - **Creative Commons**: Various restrictions.
  - **Public domain**: No restrictions.
- **Model/property releases**:
  - **People**: Signed release required for commercial use.
  - **Private property**: Permission to film/use.
- **Music licensing**:
  - **Sync license**: Use in video.
  - **Master license**: Use specific recording.
  - **Royalty-free**: Easier, check terms.
- **Trademarks**:
  - **Logos**: Permission needed for commercial.
  - **Brand names**: May need clearance.
- **Archival**: Keep license documentation with project.

### 7. Asset Optimization for Web
- **Image optimization**:
  - **Compress**: TinyPNG, ImageOptim.
  - **Format**: WebP for modern browsers, fallback JPEG/PNG.
  - **Size**: Resize to actual display size.
  - **Lazy load**: Load when needed.
- **Video optimization**:
  - **Codec**: H.264 baseline for compatibility, H.265 for efficiency.
  - **Bitrate**: 5-10 Mbps for 1080p.
  - **Resolution**: 1080p or 720p for web.
  - **Keyframes**: Every 2-10 seconds.
  - **Adaptive streaming**: HLS/DASH for different qualities.
- **Audio optimization**:
  - **Bitrate**: 128-192 kbps MP3 fine for web.
  - **Format**: AAC (better than MP3).
  - **Sample rate**: 44.1kHz or 48kHz.
- **CDN**: Use Content Delivery Network for fast global delivery.

### 8. Asset Versioning
- **Version naming**: `filename_v001.ext`, `filename_final.ext`, `filename_final_v2.ext`.
- **Version control**:
  - **Git LFS**: Track large files.
  - **Perforce**: Industry standard for large binaries.
  - **DAM**: Built-in versioning.
- **Change tracking**:
  - **Notes**: Document what changed.
  - **Diff**: Compare versions (images: visual diff).
- **Rollback**: Ability to revert to previous version.
- **Archiving old versions**: Keep but not in active project.

### 9. Asset Quality Control
- **Visual inspection**:
  - **Play through**: Check for artifacts, glitches.
  - **Zoom in**: Check for pixelation, compression.
  - **Color check**: Is color accurate?
- **Audio QC**:
  - **Listen**: Clipping, noise, distortion.
  - **Meter**: Check levels, LUFS.
  - **Phase**: Check mono compatibility.
- **Technical checks**:
  - **Codec**: Is it supported?
  - **Resolution**: Correct?
  - **Frame rate**: Match project?
  - **Duration**: As expected?
- **Metadata verification**:
  - **Copyright**: Clear?
  - **Release**: Have it?
  - **License**: Correct type?

### 10. Collaborative Asset Management
- **Shared storage**:
  - **NAS/SAN**: Network attached storage.
  - **Cloud**: Google Drive, Dropbox, OneDrive.
  - **Permissions**: Set read/write access.
- **Naming conventions**: Team-wide standard.
- **Folder structure**: Everyone uses same structure.
- **Check-in/check-out**: Prevent simultaneous edits.
- **Communication**: Notify team of asset updates.
- **Documentation**: Shared wiki/notion with guidelines.
- **Asset requests**: Process for requesting new assets.
- **Approval workflow**: Assets approved before use.

## Workflow Recommendations

1. **Plan**: What assets do you need? List them.
2. **Collect**: Gather from sources (camera, downloads, stock).
3. **Rename**: Apply naming convention.
4. **Organize**: Place in appropriate folders.
5. **Transcode**: Convert to editing-friendly formats if needed.
6. **Log**: Add metadata, tags, ratings.
7. **Backup**: Copy to backup location.
8. **Import**: Bring into project (link or embed).
9. **Organize in project**: Bins, color code, labels.
10. **Prepare**: Color correct, stabilize, clean audio.
11. **Use**: Place in timeline.
12. **Maintain**: Relink if files move, remove unused.
13. **Deliver**: Collect all used assets for handoff.

## Related Skills

For complementary techniques, refer to:
- `./core-techniques/color-grading.md` - Color management for assets
- `./core-techniques/fonts.md` - Font handling and licensing
- `./core-techniques/audio-sync.md` - Audio asset integration
- `./core-techniques/pacing.md` - Using asset duration for pacing
- `./rules/sequencing.md` - Arranging assets in timeline
- `./styles/cinematic.md` - Cinematic asset requirements
- `./styles/gameplay.md` - Gameplay footage handling
- `./styles/dark-meme-dynamic.md` - Meme asset sourcing

