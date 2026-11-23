"""One-Line Roast: write a single roast line to /output/entry.txt."""

import os

LINE = "My phone holds 4% for an hour, then dies at 20% the second I actually need it."


def main():
    # The gate only accepts 1-200 characters of non-blank UTF-8 text.
    assert 1 <= len(LINE) <= 200 and LINE.strip(), "line must be 1-200 chars"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
