import os
from typing import Any, Type
from pydantic import BaseModel, Field
from crewai.tools import BaseTool


class ListSkillsSchema(BaseModel):
    """Input schema for ListSkillsTool - no input required."""
    pass


class ReadSkillSchema(BaseModel):
    """Input schema for ReadSkillTool."""
    skill_path: str = Field(
        ..., 
        description="The relative path of the skill file (e.g., 'styles/horror.md' or 'core-techniques/jump-cut.md')"
    )


class ListSkillsTool(BaseTool):
    name: str = "List Editing Skills"
    description: str = "Lists all available editing skills, styles, and rules from the Agent's Skills Library. Returns a list of file paths that can be read using the 'Read Skill' tool."
    args_schema: Type[BaseModel] = ListSkillsSchema

    def _run(self, **kwargs: Any) -> str:
        """List all available skill files in the agent_skills_kit directory."""
        print("\n" + "="*80)
        print("[SKILLS KIT] Agent is listing available skills...")
        print("="*80 + "\n")
        
        # Assuming run from root
        base_path = os.path.join(os.getcwd(), "backend", "app", "agents", "agent_skills_kit")
        
        if not os.path.exists(base_path):
            # Fallback if running inside backend
            base_path = os.path.join(os.getcwd(), "app", "agents", "agent_skills_kit")
        
        if not os.path.exists(base_path):
            return f"Error: Skills Kit directory not found at {base_path}"

        skills_list = []
        for root, dirs, files in os.walk(base_path):
            for file in files:
                if file.endswith(".md"):
                    # Get relative path from base_path for cleaner output
                    rel_path = os.path.relpath(os.path.join(root, file), base_path)
                    skills_list.append(rel_path)
        
        if not skills_list:
            return "No skills found."
        
        result = "Available Skills:\n" + "\n".join(f"  - {skill}" for skill in sorted(skills_list))
        print(f"[SKILLS KIT] Returned {len(skills_list)} skills to Agent")
        return result


class ReadSkillTool(BaseTool):
    name: str = "Read Skill"
    description: str = "Reads the content of a specific skill file. Use this to learn about editing techniques, styles, or rules."
    args_schema: Type[BaseModel] = ReadSkillSchema

    def _run(self, skill_path: str, **kwargs: Any) -> str:
        """Read the content of a specific skill file."""
        print("\n" + "="*80)
        print(f"[SKILLS KIT] Agent is reading skill: {skill_path}")
        print("="*80 + "\n")
        
        base_path = os.path.join(os.getcwd(), "backend", "app", "agents", "agent_skills_kit")
        if not os.path.exists(base_path):
            base_path = os.path.join(os.getcwd(), "app", "agents", "agent_skills_kit")
            
        # Sanitize path to prevent traversal
        safe_path = os.path.normpath(os.path.join(base_path, skill_path))
        if not safe_path.startswith(base_path):
            return "Error: Access denied. Invalid skill path."
            
        if not os.path.exists(safe_path):
            return f"Error: Skill file not found at '{skill_path}'. Use 'List Editing Skills' to see available skills."
            
        try:
            with open(safe_path, 'r', encoding='utf-8') as f:
                content = f.read()
                print(f"[SKILLS KIT] Successfully loaded {len(content)} characters from {skill_path}")
                return f"=== Skill: {skill_path} ===\n\n{content}"
        except Exception as e:
            return f"Error reading skill: {str(e)}"
