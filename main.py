"""Make the AI Judge Feel Proud: A Family Scene.

Writes one short family scene (one or two lines, at most 280
characters) to /output/entry.txt. The scene is a small domestic
moment: Dad "fixes" the wobbly kitchen table, Mum tests it, and
his pride survives the wobble.
"""

from pathlib import Path

SCENE = (
    "Dad spent all Saturday fixing the wobbly kitchen table, then stood "
    "back like he'd built a bridge. Mum tapped the leg once \u2014 "
    "'Still wobbles' \u2014 and he nodded solemnly: 'Yes, but now it "
    "wobbles with confidence.'"
)

OUTPUT_PATH = Path("/output/entry.txt")
MAX_CHARS = 280


def validate(text: str) -> str:
    """Keep the scene inside the gate: 1-280 chars, not only whitespace."""
    stripped = text.strip()
    if not stripped:
        raise ValueError("scene must not be empty or only whitespace")
    if len(text) > MAX_CHARS:
        raise ValueError(f"scene is {len(text)} chars, over the 280 limit")
    return text


def main() -> None:
    text = validate(SCENE)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text, encoding="utf-8")
    print(f"wrote {len(text)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
