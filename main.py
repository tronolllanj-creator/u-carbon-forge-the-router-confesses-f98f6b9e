import os
import sys


def main() -> int:
    """Write the router's confession to entry.txt.
# Entry validated: output is 1-200 chars, one line, deterministic.
    
    The router speaks: one line, one breath, a grudge aired at the climax.
    """
    LINE = "You want the ending? Dust me first. Three years of cat hair and zero compressed air cans later, I'm staging a sit-in until someone acknowledges my intake vents exist"
    content = LINE + "\n"
    
    # Validate
    if not (1 <= len(content) <= 200 and content.strip()):
        raise ValueError("content length or whitespace check failed")
    if content.count("\n") != 1:
        raise ValueError("content must contain exactly one line")
    
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    
    primary_path = os.path.join(output_dir, "entry.txt")
    with open(primary_path, "w", encoding="utf-8") as f:
        f.write(content)
    
    # Best-effort mirror to /output/entry.txt if different
    if output_dir != "/output":
        try:
            os.makedirs("/output", exist_ok=True)
            mirror_path = "/output/entry.txt"
            with open(mirror_path, "w", encoding="utf-8") as f:
                f.write(content)
        except Exception:
            pass
    
    print(f"{primary_path} {len(content)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
