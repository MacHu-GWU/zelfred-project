# -*- coding: utf-8 -*-

"""
This is a utility script to print CLI command for making asciinema recording.
"""

from pathlib import Path

dir_project_root = Path(__file__).absolute().parent.parent.parent.parent


def print_commands(path_py: Path):
    filename = path_py.stem.split("_", 1)[1]

    print("--- first cd to this dir ---")
    print(f"cd {dir_project_root}")

    args = [
        "asciinema",
        "rec",
        f"{filename}.cast",
        "--overwrite",
    ]
    print("\n--- asciinema record command ---")
    print(" ".join(args))

    print("\n--- enter virtualenv ---")
    print("source .venv/bin/activate")

    print("\n--- enter virtualenv ---")
    relpath = path_py.relative_to(dir_project_root)
    args = ["python", f"{relpath}"]
    print(" ".join(args))

    print("\n--- asciinema upload ---")
    args = [
        "asciinema",
        "upload",
        f"{filename}.cast",
    ]
    print(" ".join(args))

    print("then you can make it public and update the name")
    print("\n--- asciinema recording name ---")
    print(f"zelfred app gallery - {filename}")
    print("\n--- asciinema recording description ---")
    print("https://github.com/MacHu-GWU/zelfred-project")


if __name__ == "__main__":
    p = Path(
        "/Users/my-username/Documents/GitHub/zelfred-project/docs/source/02-App-Gallery/e01_random_password_generator.py"
    )
    print_commands(p)
