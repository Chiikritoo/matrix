from pathlib import Path
import importlib.util

EXERCISES = ["ex00", "ex01", "ex02"]


def load_module_from_path(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)

    if spec is None or spec.loader is None:
        raise ImportError(f"Cannot load module from {path}")

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    return module


def main() -> None:
    root = Path(__file__).parent

    for ex in EXERCISES:
        path = root / ex / "main.py"
        module = load_module_from_path(f"{ex}_main", path)

        print(f"=== {ex} ===")
        module.main()


if __name__ == "__main__":
    main()
