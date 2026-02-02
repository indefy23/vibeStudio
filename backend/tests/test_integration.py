import pytest
from app.models.edition import Edition, Meta, Timeline, Track, Clip, Assets, Asset
from app.engine.ffmpeg_wrapper import FFmpegEngine

def test_generate_ffmpeg_command():
    # 1. Setup Mock Edition
    edition = Edition(
        meta=Meta(duration=10.0),
        assets=Assets(
            video=[
                Asset(id="v1", src="video1.mp4"),
                Asset(id="v2", src="video2.mp4")
            ]
        ),
        timeline=Timeline(
            tracks=[
                Track(
                    id="main_video",
                    type="video",
                    clips=[
                        Clip(asset="v1", start=0, end=5, in_=0, out=5),
                        Clip(asset="v2", start=5, end=10, in_=0, out=5)
                    ]
                )
            ]
        )
    )

    # 2. Initialize Engine
    engine = FFmpegEngine()
    
    # 3. Generate Command
    cmd = engine.generate_command(edition, "output.mp4")
    
    # 4. Assertions
    cmd_str = " ".join(cmd)
    print(f"\nGenerated Command: {cmd_str}")
    
    assert "ffmpeg -y" in cmd_str
    assert "-i video1.mp4" in cmd_str
    assert "-i video2.mp4" in cmd_str
    assert "concat=n=2" in cmd_str
    assert "output.mp4" in cmd_str

if __name__ == "__main__":
    test_generate_ffmpeg_command()
    print("Test Passed!")
