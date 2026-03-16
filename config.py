# API Configuration
# Place your Gemini API key here.
API_KEY = "YOUR_GEMINI_API_KEY_HERE"

# ── Configuration ──────────────────────────────────────────────────────────────
MIN_ITERATIONS        = 3  # Minimum number of iterations for the detective to make before getting the correct murderer
MIN_WRONG_ACCUS       = 4  # Minimum number of wrong accusations before the detective
MIN_PLOT_POINTS       = 15 # Minimum number of plot points in the story (to ensure it's not too short)
MAX_COHERENCE_RETRIES = 5  # Maximum number of retries for generating a coherent story (to avoid infinite loops)
