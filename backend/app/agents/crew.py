from crewai import Agent, Task, Crew, Process
from langchain_openai import ChatOpenAI
from app.core.config import settings
from app.tools.skills_tool import ListSkillsTool, ReadSkillTool

class EditorCrew:
    def __init__(self, context_data: dict):
        self.context = context_data
        self.llm = ChatOpenAI(
            model="gpt-4o", # Or gpt-3.5-turbo if cost concern
            api_key=settings.OPENAI_API_KEY
        )

    def run(self):
        # 1. Define Agent with Skills Kit
        editor = Agent(
            role='Senior Video Editor',
            goal='Create a compelling video timeline based on raw assets and user instructions.',
            backstory="""You are an expert video editor with access to a comprehensive Skills Library.
            
            CRITICAL WORKFLOW - YOU MUST FOLLOW THESE STEPS IN ORDER:
            
            1. FIRST: Use 'List Editing Skills' tool to see available editing styles and techniques
            2. SECOND: Identify which style matches the user's instruction (e.g., "dark-meme-dynamic", "cinematic", "tiktok-news-hype")
            3. THIRD: Use 'Read Skill' tool to load the relevant style guide (e.g., 'styles/dark-meme-dynamic.md')
            4. FOURTH: Apply the techniques from the loaded skill to create your timeline
            
            The Skills Library contains professional editing knowledge for:
            - Styles: cinematic, dark-tutorial, dark-meme-dynamic, gameplay, tiktok-news-hype
            - Core Techniques: animation, audio-sync, color-grading, motion-graphics, pacing, sound-design, text-animation, transitions
            - Rules: animations, assets, audio, fonts, parameters, sequencing, subtitles, timing
            
            IMPORTANT: You MUST consult the Skills Library before creating your timeline. Do NOT skip this step.
            
            After loading the appropriate skills, create a JSON timeline following the loaded style's guidelines.""",
            verbose=True,
            allow_delegation=False,
            llm=self.llm,
            tools=[ListSkillsTool(), ReadSkillTool()]
        )

        # 2. Define Task
        # We pass the context as a string description to the agent
        instruction = self.context.get("instruction", "Create a general summary.")
        assets_summary = self._format_assets_for_prompt(self.context.get("assets_analysis", []))
        
        task_description = f"""
        USER INSTRUCTION: "{instruction}"
        
        AVAILABLE ASSETS:
        {assets_summary}
        
        TASK:
        You are a Master Video Editor. Your job is to create a complete video timeline from the provided assets.
        
        INPUTS:
        - Main Video (Speech/Content)
        - Overlays (GIFs/Images/Memes)
        - Audio (SFX/Music)
        
        OBJECTIVE:
        1. **Edit the Main Video**: Cut out boring parts. Keep the most relevant/funny segments based on instruction.
        2. **Add Overlays**: Place GIF/Image/PNG overlays ON TOP of the video when they match the context. USE character PNGs (people, gestures) to add visual interest and personality.
        3. **Add Audio/SFX**: Place sound effects and background music to emphasize moments.
        4. **Add Text/Keywords**: ALWAYS add text overlays with key words or phrases synchronized with important moments (e.g., "DANGER", "WATCH OUT", "FUTURE"). This is MANDATORY.
        
        JSON SCHEMA (Strict):
        {{
          "video": [ 
              {{ "asset_id": "main_vid_id", "start": 0.0, "end": 5.0, "description": "Intro" }} 
          ],
          "audio": [ 
              {{ "asset_id": "sfx_id", "start_at": 3.5, "vol": 0.8, "description": "Laugh" }},
              {{ "asset_id": "music_id", "start_at": 0.0, "vol": 0.5, "description": "Background music" }}
          ],
          "overlay": [ 
              {{ "asset_id": "gif_id", "start_at": 2.0, "duration": 3.0, "description": "Reaction GIF", "position": "bottom_right", "scale": 0.5 }},
              {{ "asset_id": "character_png_id", "start_at": 5.0, "duration": 2.0, "description": "Character", "position": "center" }}
          ],
          "text": [
              {{ "content": "DANGER", "start_at": 1.0, "duration": 2.0, "description": "Emphasize warning" }},
              {{ "content": "WATCH OUT", "start_at": 10.0, "duration": 1.5, "description": "Alert moment" }}
          ]
        }}
        
        RULES:
        - "start" and "end" refer to the SOURCE video timing.
        - "start_at" refers to the TIMELINE time (when it should appear in the final video).
        - For "video" track: "start"/"end" cuts the source. Gaps are allowed (cuts).
        - For "overlay" track: "duration" is how long it stays on screen.
        - **OPTIONAL**: "position" for overlays: "center" (default), "top_left", "top_right", "bottom_left", "bottom_right". Use this to fit characters or memes without blocking main content.
        - **OPTIONAL**: "scale" for overlays: float (e.g. 0.5 = 50% width). Default is fixed width (approx 350px).
        - **MANDATORY**: The "text" track must include keywords from the instruction.
        - **GUIDELINE**: Try to use available overlay assets (GIFs/PNGs) to enhance the video visuals.
        - **GUIDELINE**: Avoid leaving long silent black spaces; use background music or visuals to keep engagement.
        - **CRITICAL**: Overlay "duration" must be at least 0.5 seconds.
        
        OUTPUT FORMAT:
        Return ONLY the raw JSON object. Do not include markdown formatting.
        """

        editing_task = Task(
            description=task_description,
            agent=editor,
            expected_output="A valid JSON object containing the timeline key with a list of clips."
        )

        # 3. Create Crew
        crew = Crew(
            agents=[editor],
            tasks=[editing_task],
            verbose=True,
            process=Process.sequential
        )

        result = crew.kickoff()
        return result

    def _format_assets_for_prompt(self, assets):
        # Prepare concise asset summary
        summary = ""
        for asset in assets:
            atype = asset.get("type", "UNKNOWN")
            category = asset.get("category", "unknown") # Intelligent Category
            description = asset.get("description", "")
            usage = asset.get("usage_hint", "")
            
            summary += f"- ID: {asset['id']} ({atype}/{category})\n"
            summary += f"  Duration: {asset.get('duration', 0)}s\n"
            if description:
                summary += f"  Description: {description}\n"
            summary += f"  Usage Hint: {usage}\n"
            if asset.get("transcription"):
                # Assuming transcription is a dict with a 'text' key
                text = asset['transcription'].get('text', '')[:200]
                summary += f"  Text: {text}...\n" # Truncate
            if asset.get("visual_description"):
                desc = asset['visual_description'].get('description', '')
                summary += f"  Visual: {desc}\n"
            summary += "\n" # Add a newline for separation between assets
        return summary
