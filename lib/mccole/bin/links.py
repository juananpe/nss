"""Create Markdown links table."""

from pathlib import Path
import sys
import yaml

links = yaml.safe_load(Path(sys.argv[1]).read_text()) or []
for entry in links:
    print(f'[{entry["key"]}]: {entry["url"]}')
