# Voice cloning script - xtts_v2

This script lets you clone recorded voices on the command line, using gradio to access [tonyassi's voice clone space](https://huggingface.co/spaces/tonyassi/voice-clone), which uses the [xtts-v2 model](https://huggingface.co/coqui/XTTS-v2). 

## Prerequisites
1. [git](https://git-scm.com/downloads) (to clone the repo)
2. [uv](https://docs.astral.sh/uv/getting-started/installation/) (to manage dependencies and Python versions)

## Installation
Clone this repository and navigate to the image-generation directory:
```bash
git clone git@github.com:jwjacobson/voice-cloning.git && cd voice-cloning
```
If you get an error, try this alternate command:
```bash
git clone https://github.com/jwjacobson/voice-cloning.git && cd voice-cloning
```

## Running the script
Type
```bash
uv run main.py
```

A file called `result.wav` will be saved in the project directory!

## Editing the script (different voices, different messages)
Four voices samples are included, with `george.mp3` selected by default. Change the value of the `audio_path` variable on line 20 of `main.py` to one of the other values (`benjamin.mp3`, `joseph.mp3`, `oliver.mp3`) to try them out.

The voice samples are taken from files I had on hand where I could easily find expressive, clean excerpts, and ought to be covered by fair use:
- `george.mp3` is Alec Guinness as George Smiley from the first episode of Smiley's People;
- `oliver.mp3` is Anthony Bate as Oliver Lacon from the same episode;
- `benjamin.mp3` is Avery Brooks as Benjamin Sisko from the Star Trek: Deep Space Nine episode "Far Beyond the Stars"; and
- `joseph.mp3` is Brock Peters as Joseph Sisko from the same episode.

You can also try your own samples!

Edit the value of `text` on line 21 to change the recorded message.


### License
This script is [free software](https://www.fsf.org/about/what-is-free-software), released under version 3.0 of the GPL. Everyone has the right to use, modify, and distribute it subject to the [stipulations](https://github.com/jwjacobson/image-analysis/blob/joycaption/LICENSE) of that license.