# `gradio_m3d_chatbot`
<img alt="Static Badge" src="https://img.shields.io/badge/version%20-%200.0.3%20-%20orange">  

A multi-modal markdown render, which can render markdown, audio, video, mermaid, and html in the chatbot.


## Example

### Audio and Video

````markdown
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
````

![audio_video](https://s2.loli.net/2024/12/08/6FBA7jDz4eHRmYG.png)


### Mermaid

````markdown
**Mermaid**

This is a mermaid code snippet.

```mermaid
graph TD;
    A-->B;
    A-->C;
    B-->D;
    C-->D;
```
````

![mermaid](https://s2.loli.net/2024/12/08/scozTX9RW4Kkhje.png)


### HTML

````markdown
**HTML**

This is a html code snippet.

```html
<h1>Header 1</h1>
<p>Paragraph 1</p>
```
````

![html](https://s2.loli.net/2024/12/08/4q3s8aFLdAIEwJH.png)



## Installation

```bash
pip install gradio_m3d_chatbot
```

## Usage

````python
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

````


## Reference

- [ChatGPT-Next-Web](https://github.com/ChatGPTNextWeb/ChatGPT-Next-Web)
- [MMKG-RAG](https://github.com/wenzhaoabc/mmkg-rag/)

## License

[apache-2.0](https://opensource.org/licenses/apache-2.0)