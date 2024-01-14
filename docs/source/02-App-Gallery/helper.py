# -*- coding: utf-8 -*-

"""
This is a utility script to print CLI command for making asciinema recording.
"""

from pathlib import Path

dir_project_root = Path(__file__).absolute().parent.parent.parent.parent


def print_commands(filename: str):
    if not filename.endswith(".py"):
        filename = filename + ".py"
    path_py = dir_project_root.joinpath("zelfred", "gallery", filename)
    if not path_py.exists():
        raise FileNotFoundError

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

    print("\n--- enter virtualenv and run app ---")
    relpath = path_py.relative_to(dir_project_root)
    print(f"source .venv/bin/activate && python {relpath}")

    print("\n--- asciinema upload ---")
    args = [
        "asciinema",
        "upload",
        f"{filename}.cast",
    ]
    print(" ".join(args))

    print("then you can make it public and update the name")
    print("\n--- asciinema recording name ---")
    asciinema_name = filename.split("_", 1)[1].split(".", 1)[0]
    print(f"zelfred app gallery - {asciinema_name}")
    print("\n--- asciinema recording description ---")
    print("https://github.com/MacHu-GWU/zelfred-project")


if __name__ == "__main__":
    print_commands("e10_refresh_cache_v3.py")
