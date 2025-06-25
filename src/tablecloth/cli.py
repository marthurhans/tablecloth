# cli.py
import sys
import os
import subprocess


def main():
    if len(sys.argv) != 2:
        print("Usage: tablecloth <destination_path>")
        sys.exit(1)

    dest_path = os.path.abspath(sys.argv[1])
    source_path = os.getcwd()

    print(f"Preparing for move ...")

    # Escape! Go to parent directory or known neutral zone
    escape_dir = os.path.expanduser("~")  # C:/Users/lilci
    os.chdir(escape_dir)

    runner_path = os.path.join(os.path.dirname(__file__), "runner.py")

    try:
        subprocess.run(
            ["python", runner_path, source_path, dest_path],
            check=True
        )
        print(f"\nMove complete. Your folder now lives at:\n    {dest_path}")
        print("You're still sitting in the old terminal path, which no longer exists.")
        print(f"To resume work, type or paste:\n    cd \"{dest_path}\"")
        print("If you were authoring code in an IDE (like VS Code):")
        print("Your IDE may still show your project at its old location -")
        print("but this is no longer valid.")
        print("Treat this like a freshly cloned project and open or import the new path")
        print("so your IDE can rebuild its configuration.\n")

    except subprocess.CalledProcessError as e:
        print(f"[CLI] Move failed: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()

