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

Some of the sample stories generated for each type of genre that we are handling (classic puzzle, noir and psychological) are present in the `sample_stories` folder

## Time and Cost Analysis

The notebook takes typically 2-3 minutes to run fully and generate the final story. This can sometimes take longer while facing rate limiting issues with Gemini.

Optionally, one can enable ondemand pricing for Gemini API incase they are hitting quota exceeded very often. For the flash models, this is about $0.2 per 1M tokens. In our pipeline, 1M tokens can roughly generate about 50 stories so you can expect to be able to generated 1 story for about $0.004 using the flash model. Using the pro model, the cost will jump to about $0.12 per story generated.

## Analysis of a good story

We generated a classic puzzle type of story which you can view at [`sample_stories/good_story_classic.md`](sample_stories/good_story_classic.md) 

1. A scientist is found dead in a sealed deep-sea habitat with failing life support.

2. The habitat lockdown is revealed to be deliberate sabotage, isolating all suspects under a ticking clock.

3. The death is identified as a deliberate poisoning via the atmospheric system.

4. The murder is determined to require both biological and engineering expertise.

5. A closed set of suspects is established, each with motive and partial means.

6. Early evidence points toward both Thorne (biological means) and Kryll (engineering access).

7. Physical evidence begins to implicate Thorne but is not yet conclusive.

8. Thorne presents a strong procedural alibi that blocks direct accusation.

9. Environmental disruptions interfere with the investigation, suggesting active manipulation by the killer.

10. Voss pursues an alternative suspect based on motive and means, but the timeline fails.

11. Additional motives and secrets among the crew create misleading red herrings.

12. Critical evidence is erased or corrupted, weakening the investigation.

13. The communication system failure is confirmed as intentional sabotage requiring high technical skill.

14. A second murder occurs when Kryll is found dead.

15. Kryll’s death is recognized as a deliberate witness elimination.

16. The killer is deduced to have control over both biological and engineering systems.

17. The precise timing required for the poisoning becomes the key constraint.

18. Remaining suspects are eliminated based on capability and timing.

19. All evidence converges on Thorne as the only viable culprit.

20. The true motive is uncovered: concealment of unauthorized energy experiments.

21. Voss reconstructs the full sequence of crimes and confronts Thorne.

22. Thorne attempts a final action to trigger system failure.

23. Thorne is subdued and stopped.

24. Voss overrides the failing life-support system, saving the habitat.
