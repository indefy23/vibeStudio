
import os
import json
from backend.app.engine.renderer import Renderer

def run_test():
    project_id = "e99dc7c6-1790-4a91-a4d1-93505b86babf"
    project_dir = os.path.abspath(f"./projects/{project_id}")
    manifest_path = os.path.join(project_dir, "manifest.json")
    refined_path = os.path.join(project_dir, "timeline_refined.json")
    output_path = os.path.join(project_dir, "test_render.mp4")
    assets_path = os.path.join(project_dir, "assets")

    print(f"Project Dir: {project_dir}")
    print(f"Manifest Path: {manifest_path}")

    with open(manifest_path, 'r') as f:
        manifest = json.load(f)

    # Build asset_map exactly like Orchestrator
    asset_map = {}
    for asset in manifest['assets']:
        asset_map[asset['id']] = asset['path']

    renderer = Renderer()
    try:
        print("\n--- Starting Render ---")
        renderer.render_timeline(
            refined_path,
            output_path,
            assets_path,
            asset_map=asset_map
        )
        print("\n--- Render Finished Successfully ---")
        print(f"Output: {output_path}")
    except Exception as e:
        print(f"\n--- Render Failed ---")
        print(e)

if __name__ == "__main__":
    run_test()
