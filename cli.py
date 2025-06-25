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

    print(f"[CLI] Preparing to move this folder:")
    print(f"    FROM: {source_path}")
    print(f"    TO:   {dest_path}")

    # Escape! Go to parent directory or known neutral zone
    escape_dir = os.path.expanduser("~")  # C:/Users/lilci
    os.chdir(escape_dir)

    runner_path = os.path.join(os.path.dirname(__file__), "runner.py")

    try:
        subprocess.run(
            ["python", runner_path, source_path, dest_path],
            check=True
        )
        print(f"[CLI] Move completed. Folder now lives at:\n  {dest_path}")
        print("[CLI] Open your terminal at the new location to continue working.")
    except subprocess.CalledProcessError as e:
        print(f"[CLI] Move failed: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()

