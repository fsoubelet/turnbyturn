"""Exposes TbtData, read_tbt and write_tbt directly in the package's namespace."""
from .io import read_tbt, write_tbt
from .structures import TbtData, TransverseData

__title__ = "turn_by_turn"
__description__ = "Read and write turn-by-turn measurement files from different particle accelerator formats."
__url__ = "https://github.com/pylhc/turn_by_turn"
__version__ = "0.8.0"
__author__ = "pylhc"
__author_email__ = "pylhc@github.com"
__license__ = "MIT"

# aliases
write = write_tbt
read = read_tbt

# Importing * is a bad practice and you should be punished for using it
__all__ = []
