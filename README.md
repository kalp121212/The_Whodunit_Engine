# CS7634 Project 1 — AI-Powered Murder Mystery Generator

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

Open `CS7634_Project1_v3 (1).ipynb` in Jupyter Lab or Jupyter Notebook and run all cells sequentially.

```bash
jupyter notebook
```

## Output

The final generated story (2500+ words) is saved to `generated_story.txt` in the project directory.

## Configuration

Model and pipeline parameters are set in **Cell 21** of the notebook:

| Parameter | Default | Description |
|---|---|---|
| `model` | `gemini-flash-lite-latest` | Gemini model to use (`gemini-flash-latest` for richer stories) |
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
