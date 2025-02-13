# Tile definitions
# First letter: Tube, Ball, Crystal, Layer
# Second letter: Small vs. Large, Dark vs. Light
tiles = [
    ("TS", "BL", "CS", "LS"),
    ("LL", "TS", "CL", "BD"),
    ("CL", "BL", "LL", "TL"), # ("CL", "BD", "LL", "TL"),
    ("CL", "LS", "BD", "TS"),
    ("CS", "TS", "CS", "LL"),
    ("LS", "CS", "BL", "TL"), #("LS", "CS", "BD", "TL"),
    ("LS", "BD", "TL", "CL"),
    ("TL", "BL", "LS", "BL"),
    ("TS", "LS", "CS", "BD"),
]