import csv
import re
import argparse

# Set up argument parser
parser = argparse.ArgumentParser(description="Parse markdown flashcards into CSV.")
parser.add_argument(
    "files",
    nargs="+",
    help="List of markdown files to parse"
)
parser.add_argument(
    "-o", "--output",
    default="output.csv",
    help="Output CSV file name (default: output.csv)"
)

args = parser.parse_args()

# Regex patterns to extract front and back
front_pattern = re.compile(r"### \d+\. \*\*(.+?)\*\*")
back_pattern = re.compile(r"- (.+)")

entries = []

for md_file in args.files:
    with open(md_file, "r", encoding="utf-8") as f:
        lines = f.readlines()

    front, back = None, None
    for line in lines:
        line = line.strip()
        front_match = front_pattern.match(line)
        if front_match:
            front = front_match.group(1)
            back = None
            continue

        back_match = back_pattern.match(line)
        if back_match and front:
            back = back_match.group(1)
            entries.append({"front": front, "back": back})
            front, back = None, None

# Write to CSV
with open(args.output, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["front", "back"])
    writer.writeheader()
    writer.writerows(entries)

print(f"CSV file '{args.output}' created with {len(entries)} entries from {len(args.files)} files!")

