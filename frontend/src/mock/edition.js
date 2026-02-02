export const MOCK_EDITION = {
  "meta": {
    "version": "1.0",
    "fps": 30,
    "format": "9:16",
    "duration": 10.6
  },
  "assets": {
    "video": [
      { "id": "v1", "src": "/mock_video.mp4" }
    ]
  },
  "timeline": {
    "tracks": [
      {
        "id": "main_video",
        "type": "video",
        "clips": [
          {
            "asset": "v1",
            "start": 0.0,
            "end": 10.6,
            "in": 2.3,
            "out": 12.9,
            "properties": {
               "scale": 1.0,
               "opacity": 1.0,
               "position": { "x": 0.5, "y": 0.5 }
            },
            "keyframes": {}
          }
        ]
      },
      {
        "id": "text_overlays",
        "type": "overlay",
        "elements": [
          {
            "id": "caption_1",
            "type": "text",
            "content": "IA não edita sozinha",
            "start": 1.2,
            "end": 3.8,
            "properties": {
              "anchor": "center",
              "position": { "x": 0.5, "y": 0.82 },
              "scale": 1.0,
              "opacity": 1.0
            },
            "keyframes": {
              "scale": [
                { "t": 1.2, "v": 0.9, "e": "ease-out" },
                { "t": 1.45, "v": 1.0, "e": "ease-in" }
              ]
            }
          }
        ]
      }
    ]
  },
  "adjustments": {}
};
