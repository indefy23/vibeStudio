---
name: parameters
description: Making videos parametrizable by adding schemas, controls, and dynamic inputs
metadata:
  tags: parameters, schema, zod, dynamic, props, customization
---

## When to use

Use this skill whenever you want to make your video compositions customizable - allowing users to change text, colors, images, timing, or other properties without editing code. This is essential for creating reusable templates, automated video generation, and multi-language or multi-brand videos.

## Core Principles

### 1. Why Parameterize?
- **Reusability**: Same composition can generate many different videos.
- **Automation**: Feed data from spreadsheets, APIs, databases.
- **User-friendly**: Non-technical users can customize via UI controls.
- **Multi-language**: Swap text based on locale.
- **Brand variations**: Change colors, logos, fonts per brand.
- **A/B testing**: Easily generate variants.

### 2. Parameter Types
- **String**: Text values (headlines, names, URLs).
- **Number**: Numeric values (duration, count, size).
- **Boolean**: True/false flags (show/hide elements).
- **Color**: Hex, RGB, HSL color values.
- **Image/Video URL**: Links to media assets.
- **Enum**: Predefined list of options (style: "modern" | "classic" | "minimal").
- **Array**: Lists of items (multiple logos, bullet points).
- **Object**: Complex structured data (user profile, product info).

### 3. Defining Parameters with Zod Schema
- **Zod**: TypeScript-first schema validation library. Used by Remotion.
- **Basic schema**:
  ```
  import { z } from 'zod';
  const schema = z.object({
    title: z.string(),
    duration: z.number(),
    showLogo: z.boolean(),
  });
  ```
- **Default values**:
  ```
  title: z.string().default("Default Title"),
  duration: z.number().default(5),
  ```
- **Validation**:
  - `z.string().min(1).max(100)`
  - `z.number().min(0).max(100)`
  - `z.enum(['option1', 'option2'])`
  - `z.array(z.string())`
  - `z.object({ nested: z.string() })`
- **Optional**: `z.string().optional()`
- **Transform**: Modify value after validation: `.transform(value => value.toUpperCase())`

### 4. Using Parameters in Composition
- **Define defaultProps**:
  ```
  export const MyComp: React.FC = (props) => {
    const { title, duration } = props;
    // use props
  };
  
  MyComp.defaultProps = {
    title: "Hello",
    duration: 5,
  };
  ```
- **Or with schema**:
  ```
  export const MyComp = (props: z.infer<typeof schema>) => {
    // props are typed and validated
  };
  ```
- **Access in render**: Use props directly in JSX.
- **Dynamic values**: Props can drive animation durations, text content, colors, image sources.

### 5. UI Controls (Remotion Studio)
- **Input**: Text, number, textarea.
- **Select**: Dropdown from enum.
- **Checkbox**: Boolean toggle.
- **Color picker**: Color input.
- **Slider**: Number with min/max/step.
- **File upload**: Image/video upload.
- **Rich text**: WYSIWYG text editor.
- **Custom**: Build your own React component as control.
- **Grouping**: Organize controls into sections/accordions.
- **Conditional**: Show/hide controls based on other values.

### 6. Dynamic Metadata
- **Composition metadata**: Title, description, tags can be dynamic.
- **Thumbnail**: Generate thumbnail based on parameters.
- **Duration**: Set composition duration based on props.
- **Dimensions**: Width/height can be dynamic (but usually fixed).
- **Default props**: Show in UI as starting values.

### 7. Data-Driven Videos
- **CSV/JSON import**: Load data file, iterate to generate multiple videos.
- **API integration**: Fetch data from external source (products, news, weather).
- **Spreadsheets**: Connect to Google Sheets or Airtable.
- **Database**: Query database for dynamic content.
- **Looping**: Generate video for each item in array.
- **Batch rendering**: Use `renderMedia()` in script to generate many.

### 8. Multi-Language Support
- **Locale parameter**: `locale: z.enum(['en', 'es', 'pt'])`
- **Translation dictionary**: Map keys to translated strings.
  ```
  const translations = {
    en: { welcome: "Welcome" },
    es: { welcome: "Bienvenido" },
  };
  const text = translations[props.locale].welcome;
  ```
- **RTL support**: For Arabic, Hebrew. Use `dir="rtl"` and appropriate fonts.
- **Text expansion**: Account for longer translations (German, French).
- **Fonts**: Load fonts that support all characters (CJK, Arabic).

### 9. Brand Variations
- **Brand parameter**: `brand: z.enum(['brandA', 'brandB'])`
- **Brand config**: Object with colors, fonts, logos per brand.
  ```
  const brands = {
    brandA: { primary: '#FF0000', logo: '/logoA.png' },
    brandB: { primary: '#0000FF', logo: '/logoB.png' },
  };
  const config = brands[props.brand];
  ```
- **Apply dynamically**: Use brand config to set colors, images, fonts.
- **Theme switching**: Light/dark mode based on parameter.

### 10. Advanced Patterns
- **Conditional rendering**: Show/hide elements based on boolean props.
- **List rendering**: Map over arrays to generate repeated elements (bullet points, product grids).
- **Composition composition**: Pass props to nested compositions.
- **Master properties**: Control child comp parameters from parent.
- **Dynamic imports**: Load different assets based on parameters.
- **Expressions with props**: Use props in expressions for dynamic animation.
- **Default fallbacks**: Provide fallback values if prop missing.

## Technical Implementation

### Schema Definition
- **Location**: Define schema in composition file or separate file.
- **Export**: Export schema as `schema` named export for Remotion Studio to detect.
- **Complex schemas**:
  ```
  const schema = z.object({
    title: z.string().min(1).max(100),
    items: z.array(z.object({
      text: z.string(),
      icon: z.string().url().optional(),
    })).max(10),
    style: z.enum(['minimal', 'bold', 'colorful']).default('minimal'),
    colors: z.object({
      primary: z.string().regex(/^#([0-9A-Fa-f]{6}|[0-9A-Fa-f]{8})$/),
      secondary: z.string().optional(),
    }),
  });
  ```

### Using Props in Composition
- **Type inference**: `type Props = z.infer<typeof schema>;`
- **Component signature**: `const MyComp: React.FC<Props> = (props) => { ... }`
- **Default props**: Set defaults in schema or component `defaultProps`.
- **Destructure**: `const { title, items } = props;`
- **Use in JSX**: `<Text>{title}</Text>`
- **Use in animation**: `duration={props.duration * 30}` (frames)
- **Use in styles**: `style={{ color: props.colors.primary }}`

### UI Controls Configuration
- **Control types**: Remotion auto-detects from Zod schema.
  - `z.string()` → Text input
  - `z.number()` → Number input
  - `z.boolean()` → Checkbox
  - `z.enum([...])` → Select dropdown
  - `z.string().url()` → File upload or URL input
  - `z.array(...)` → List editor
  - `z.object(...)` → Grouped controls
- **Custom control**: Use `describe` to override:
  ```
  title: z.string().describe({
    type: 'text',
    title: 'Video Title',
    description: 'Main headline shown at start',
  })
  ```
- **Control options**:
  ```
  .describe({
    type: 'slider',
    min: 1,
    max: 10,
    step: 0.5,
  })
  ```

### Data-Driven Rendering
- **Script rendering**: Use `renderMedia()` in Node script.
- **Input data**: Read CSV/JSON file, iterate rows.
- **Parameter per row**: Each row becomes props for one video.
- **Output**: Render to folder with naming convention.
- **Example**:
  ```
  import { renderMedia } from '@remotion/renderer';
  import data from './data.json';
  
  for (const item of data) {
    await renderMedia({
      composition: MyComp,
      props: item,
      output: `./rendered/${item.id}.mp4`,
    });
  }
  ```

### Multi-Language Implementation
- **Locale prop**: Add `locale: z.string().default('en')`.
- **Translation file**: JSON file with all strings per locale.
  ```
  {
    "en": { "title": "Welcome", "subtitle": "Get started" },
    "es": { "title": "Bienvenido", "subtitle": "Comienza" },
  }
  ```
- **Load translation**: `const t = translations[props.locale];`
- **Use**: `<Text>{t.title}</Text>`
- **Font loading**: Load fonts that support all characters.
- **RTL**: Conditionally set `dir={props.locale === 'ar' ? 'rtl' : 'ltr'}`.

### Brand System Implementation
- **Brand enum**: `brand: z.enum(['nike', 'adidas', 'puma'])`.
- **Brand config**: Separate file with all brand assets.
  ```
  const brandConfig = {
    nike: {
      colors: { primary: '#111111', accent: '#FF0000' },
      fonts: { heading: 'NikeFont', body: 'NikeBody' },
      logo: '/nike.png',
    },
    // ...
  };
  ```
- **Apply**: `const config = brandConfig[props.brand];`
- **Use**: `<Text style={{ color: config.colors.primary }}>{props.title}</Text>`
- **Logo**: `<Img src={config.logo} />`

## Common Pitfalls to Avoid

- **No defaults**: Users must fill every field. Provide sensible defaults.
- **Over-parameterizing**: Too many parameters overwhelm users. Keep essential only.
- **Poor naming**: Parameter names should be clear and descriptive.
- **Missing validation**: No constraints leads to broken videos (too long text, invalid colors).
- **Hard-coded values**: Defeats purpose of parameters. Use props everywhere.
- **Inconsistent types**: Same concept different types (string vs number). Standardize.
- **No documentation**: Users don't know what parameters do. Add descriptions.
- **Breaking changes**: Changing parameter names/types breaks existing data. Version your schema.
- **Performance**: Too many parameters can slow UI. Group logically.
- **No fallbacks**: When data missing, video breaks. Provide fallbacks.

## Advanced Techniques

### 1. Dynamic Composition Selection
- **Parameter to choose comp**: `template: z.enum(['vertical', 'horizontal', 'square'])`.
- **Render different comp**: Based on param, render different composition.
- **Use case**: Different layouts for different use cases.

### 2. Conditional Dependencies
- **Show/hide parameters**: Based on other param values.
  ```
  showAdvanced: z.boolean(),
  advancedSettings: z.object({ ... }).optional().refine(val => !props.showAdvanced || val, {
    message: 'Required when advanced is on',
  }),
  ```
- **Dynamic enums**: Options list depends on another parameter (country → cities).

### 3. Computed Properties
- **Derived values**: Compute from other props.
  ```
  const fontSize = props.isMobile ? 24 : 32;
  const duration = props.itemCount * 2; // 2 seconds per item
  ```
- **Use in schema**: `.transform(value => value * 2)`

### 4. Nested Compositions with Props
- **Pass props down**: Parent comp passes subset of props to child.
- **Prop mapping**: Transform parent prop to child prop.
  ```
  <ChildComp title={props.title} color={props.theme.primary} />
  ```
- **Master properties**: Child comp exposes parameters to parent.

### 5. Template System
- **Template presets**: Predefined sets of parameters.
  ```
  presets: {
    minimal: { style: 'minimal', colors: { primary: '#000' } },
    bold: { style: 'bold', colors: { primary: '#F00' } },
  }
  ```
- **Load preset**: Button to apply preset values to parameters.
- **Save custom**: Allow users to save their own presets.

### 6. Versioning & Migration
- **Schema version**: Add `version: z.number()` to schema.
- **Migration function**: Transform old props to new schema.
- **Backward compatibility**: Support old parameter names with defaults.
- **Deprecation**: Mark old params as deprecated, map to new.

### 7. Validation & Error Handling
- **Schema validation**: Zod validates automatically in Studio.
- **Custom validation**: `.refine()` for complex rules.
  ```
  endDate: z.string().datetime().refine(date => new Date(date) > new Date(), {
    message: 'End date must be in future',
  })
  ```
- **Error messages**: Provide clear, helpful error messages.
- **Graceful degradation**: If prop missing, use fallback.

### 8. Performance Optimization
- **Memoization**: `useMemo` for expensive derived values.
- **Conditional rendering**: Don't render elements if prop false.
- **Asset loading**: Load images conditionally based on params.
- **Code splitting**: Dynamic imports for heavy components based on params.

### 9. Testing Parameterized Compositions
- **Test with various prop values**: Edge cases, min/max, empty, null.
- **Snapshot testing**: Render frames with different props, compare.
- **Property tests**: Generate random valid props, ensure no crash.
- **UI testing**: Test Studio controls work correctly.

### 10. Documentation for Users
- **Parameter descriptions**: Clear, concise, examples.
- **Type information**: Show expected type, format.
- **Default values**: Document what happens if not provided.
- **Examples**: Show sample prop values and resulting video.
- **Constraints**: Document min/max, allowed values.
- **Dependencies**: Note if one param affects another.

## Workflow Recommendations

1. **Design template**: Create composition with placeholder values.
2. **Identify parameters**: What should be customizable? Text, colors, images, timing.
3. **Define schema**: Write Zod schema with types, defaults, validation.
4. **Implement props**: Use props throughout composition, no hard-coded values.
5. **Add UI controls**: Ensure each param has appropriate control in Studio.
6. **Test variations**: Try different prop values to ensure all work.
7. **Document**: Add descriptions to schema, create user guide.
8. **Template packaging**: If sharing, include example prop files.
9. **Automation script**: If batch rendering, write script to feed data.
10. **Version control**: Tag releases when schema changes.

## Related Skills

For complementary techniques, refer to:
- `./core-techniques/text-animation.md` - Dynamic text from parameters
- `./core-techniques/color-grading.md` - Dynamic color schemes
- `./core-techniques/assets.md` - Dynamic asset loading
- `./core-techniques/fonts.md` - Dynamic font selection
- `./core-techniques/timing.md` - Dynamic duration control
- `./styles/cinematic.md` - Parameterized film looks
- `./styles/dark-tutorial.md` - Tutorial-specific parameters
- `./styles/gameplay.md` - Game-specific parameters

