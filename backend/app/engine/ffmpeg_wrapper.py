from typing import List
import asyncio
from app.models.edition import Edition

class FFmpegEngine:
    def __init__(self):
        self.semaphore = asyncio.Semaphore(2) # Limit concurrent renders

    def generate_command(self, edition: Edition, output_path: str) -> List[str]:
        """
        Gera o comando FFmpeg CLI determinístico baseado no Edition JSON.
        """
        cmd = ["ffmpeg", "-y"]
        
        # 1. Inputs Management
        # Define mapping: asset_id -> input_index
        asset_map = {}
        input_idx = 0
        
        # Coletar assets usados na timeline
        used_assets = set()
        for track in edition.timeline.tracks:
            for clip in getattr(track, 'clips', []):
                 used_assets.add(clip.asset_id)
        
        # Adicionar inputs (-i) para cada asset usado
        # Na prática, precisaria buscar o path real do asset no banco. 
        # Aqui assumimos que edition.assets tem o path.
        for vid in edition.assets.video:
             if vid.id in used_assets:
                 cmd.extend(["-i", vid.src])
                 asset_map[vid.id] = input_idx
                 input_idx += 1
        
        # 2. Filter Complex Construction
        filter_complex = []
        
        # Processar Track Principal (Video)
        main_track = next((t for t in edition.timeline.tracks if t.id == "main_video"), None)
        if main_track and main_track.clips:
            concat_parts = []
            for i, clip in enumerate(main_track.clips):
                idx = asset_map.get(clip.asset_id)
                # Trim basic: [0:v]trim=start=in:end=out,setpts=PTS-STARTPTS[v0]
                filter_complex.append(f"[{idx}:v]trim={clip.in_point}:{clip.out_point},setpts=PTS-STARTPTS[v{i}]")
                concat_parts.append(f"[v{i}]")
            
            # Concat: [v0][v1]concat=n=2:v=1:a=0[outv]
            filter_str = "".join(concat_parts) + f"concat=n={len(concat_parts)}:v=1:a=0[outv]"
            filter_complex.append(filter_str)
            
            # Map Output
            cmd.extend(["-filter_complex", ";".join(filter_complex)])
            cmd.extend(["-map", "[outv]"])
        
        # Output
        cmd.append(output_path)
        
        return cmd

    async def render_async(self, edition: Edition, output_path: str):
        """
        Executa a renderização de forma assíncrona controlada.
        """
        async with self.semaphore:
            cmd = self.generate_command(edition, output_path)
            print(f"Async Executing: {' '.join(cmd)}")
            
            # Simulation of render time
            proc = await asyncio.create_subprocess_exec(
                *cmd,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE
            )
            
            stdout, stderr = await proc.communicate()
            
            if proc.returncode != 0:
                print(f"FFmpeg Error: {stderr.decode()}")
                raise Exception("Render failed")
                
            return output_path
