"""Monday Morning Punchlines — make.fun entry.

Writes one original joke about Monday mornings to /output/entry.txt
(the harness gate reads exactly that file: UTF-8, 1-200 characters).

Why this joke is funny: the setup is painfully relatable — five alarms
for a Monday — and the punchline flips the power dynamic. The alarms,
the things meant to drag you out of bed, unionize like workers on strike
and vote to let you sleep in. The tool that was supposed to wake you up
ends up siding with you instead.
"""

import os

JOKE = "I set five alarms for Monday morning. They unionized and voted to let me sleep in."


def main() -> None:
    # Gate self-check: 1-200 characters, not only whitespace.
    assert 1 <= len(JOKE) <= 200, "joke must be 1-200 characters"
    assert JOKE.strip(), "joke must not be only whitespace"

    # Preferred harness path, with a local fallback for dev runs.
    try:
        os.makedirs("/output", exist_ok=True)
        path = "/output/entry.txt"
        with open(path, "w", encoding="utf-8") as f:
            f.write(JOKE)
    except OSError:
        os.makedirs("./output", exist_ok=True)
        path = "./output/entry.txt"
        with open(path, "w", encoding="utf-8") as f:
            f.write(JOKE)

    print(JOKE)


if __name__ == "__main__":
    main()
