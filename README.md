# CS7634 Project 1 — AI-Powered Murder Mystery Generator

Team Name: Rabid Fish 

Project Template: Suspense Generation

System Name: The Whodunit Engine

An AI-powered whodunit story generator built with Google's Gemini API. Uses multi-stage prompt engineering to procedurally generate coherent murder mystery narratives with suspects, clues, red herrings, and an iterative detective investigation loop.

## Setup

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Add your API key

Open `config.py` and replace the placeholder with your Gemini API key:

```python
API_KEY = "YOUR_GEMINI_API_KEY_HERE"
```

You can get a free Gemini API key at [https://aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey).

### 3. Run the notebook

Open `CS7634_Project1.ipynb` and run all cells sequentially, ensure that the config file has all the required parameters before you run all the cells.

## Output

The final generated story (2500+ words) is saved to `generated_story.md` in the project directory.

## Configuration

Model and pipeline parameters are set in **Cell 21** of the notebook:

| Parameter | Default | Description |
|---|---|---|
| `model` | `gemini-flash-latest` | Gemini model to use (`gemini-flash-lite-latest` for faster generation) |
| `MIN_ITERATIONS` | `3` | Minimum detective loop iterations |
| `MIN_WRONG_ACCUS` | `4` | Minimum wrong accusations before resolution |
| `MIN_PLOT_POINTS` | `15` | Minimum total plot points accumulated |
| `DEATH_INJECTION_ITER` | random 1–3 | Which iteration triggers the second death |

If you hit rate limits, swap to a different API key in `config.py`.

## Pipeline Overview

```
Setting → Crime (hidden) → Suspects → Clues
                                        ↓
                              Detective + Stakes
                                        ↓
                         Iterative Investigation Loop
                         (wrong accusations + mystery death)
                                        ↓
                              Breakthrough + Coherence Check
                                        ↓
                              Final Story (prose narrative)
```

Some of the sample stories generated for each type of genre that we are handling (classic puzzle, noir and psychological) are present in the `sample_good_stories` folder

## Time and Cost Analysis

The notebook takes typically 2-3 minutes to run fully and generate the final story. This can sometimes take longer while facing rate limiting issues with Gemini.

Optionally, one can enable ondemand pricing for Gemini API incase they are hitting quota exceeded very often. For the flash models, this is about $0.2 per 1M tokens. In our pipeline, 1M tokens can roughly generate about 50 stories so you can expect to be able to generated 1 story for about $0.004 using the flash model. Using the pro model, the cost will jump to about $0.12 per story generated.
