import gradio as gr
from gradio_m3d_chatbot import m3d_chatbot

# An example markdown document
example_doc = """
**Audio**

```markdown
[Exampple Audio Name](https://www2.cs.uic.edu/~i101/SoundFiles/BabyElephantWalk60.wav)
```

[Exampple Audio Name](https://www2.cs.uic.edu/~i101/SoundFiles/BabyElephantWalk60.wav)

**Video**

```markdown
[Video Example](https://interactive-examples.mdn.mozilla.net/media/cc0-videos/flower.mp4)
```

[Video Example](https://interactive-examples.mdn.mozilla.net/media/cc0-videos/flower.mp4)

**Mermaid**

This is a mermaid code snippet.

```mermaid
graph TD;
    A-->B;
    A-->C;
    B-->D;
    C-->D;
```

**HTML**

This is a html code snippet.

```html
<h1>Header 1</h1>
<p>Paragraph 1</p>
```

"""

example_value = [
    {"role": "user", "content": "Hi, how are you?"},
    {"role": "assistant", "content": example_doc},
]

with gr.Blocks(
    css="""
    #m3d_chatbot {
        height: 1200px !important;
    }
    """
) as demo:
    with gr.Row():
        # m3d_chatbot(label="Blank"),  # blank component
        m3d_chatbot(
            elem_id="m3d_chatbot",
            value=example_value,
            label="Populated",
            type="messages",
            sanitize_html=False,
        ),  # populated component


if __name__ == "__main__":
    demo.launch()
