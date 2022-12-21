import subprocess
import pathlib as pl

target_file = pl.Path("code.md")
TAG = "| Program | Version | UTC Date |"
FILES = ("code.json", "code.md")


def _create_code_json() -> None:
    subprocess.run(
        [
            "make-code-json",
            "-f",
            f"code.json",
            "--verbose",
        ]
    )

    if not target_file.is_file():
        raise FileNotFoundError(f"{target_file} does not exist")


def _update_readme() -> None:
    with open("README.md", "r") as f:
        readme_md = f.read().splitlines()
    with open("code.md", "r") as f:
        code_md = f.read().splitlines()
    with open("README.md", "w") as f:
        for line in readme_md:
            if TAG not in line:
                f.write(f"{line}\n")
            else:
                for code_line in code_md:
                    f.write(f"{code_line}\n")
                break


def _clean_files() -> None:
    for file in FILES:
        pl.Path(file).unlink()


if __name__ == "__main__":
    # _create_code_json()
    _update_readme()
    _clean_files()
