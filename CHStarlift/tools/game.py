"""STARLIFT: what the shared CHGame tools need to know (`cl run` and `cl gif` read this)."""

# One framebuffer row a DMA chunk (CHGfx's default is 2): about 500 B of RAM back.
# The second entry smuggles size flags into build.extra_flags (device.py joins "-D" + each entry): -76 B over the
# whole build, library included (the link step does not see extra_flags; under LTO these per-function flags still hold).
DEFINES = ["GFX_CHUNK_ROWS=1", "EXTI_MODULE_DISABLED", "SL_CC=1 -fno-jump-tables -fno-tree-vrp -fno-schedule-insns2 -fno-tree-tail-merge -fno-reorder-blocks -fno-ipa-sra -fno-split-wide-types -fno-forward-propagate -fno-tree-fre"]
# A board perf run (cl run --device CHStarlift/tools/scripts/perf.txt): add "SL_BOT", "SL_START=n" here (the -D flag does not reach
# the board build), then delete CHStarlift/build.
TESTS = {}
# One save page (since 0.14): 256 B more for the game. A power cut in the middle of a save loses that save.
SAVE_PAGES = 1
