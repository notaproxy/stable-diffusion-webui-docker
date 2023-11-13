import sys
from pathlib import Path

file = Path(sys.argv[1])
file.write_text(
  file.read_text()\
  .replace('    return demo', """
    with demo:
        gr.Markdown(
          'Created by [AUTOMATIC1111 / stable-diffusion-webui-docker](https://github.com/AbdBarho/stable-diffusion-webui-docker/)\\n\\n[Go to index](/)'
        )
    return demo
""", 1)
)
