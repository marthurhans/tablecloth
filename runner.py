# runner.py
import sys
import os
import shutil


def main():
    if len(sys.argv) != 3:
        print("Usage: runner.py <source_path> <destination_path>")
        sys.exit(1)

    source = os.path.abspath(sys.argv[1])
    destination = os.path.abspath(sys.argv[2])
    folder_name = os.path.basename(source)

    print("[Runner] Moving folder:")
    print(f"    FROM: {source}")
    print(f"    TO:   {destination}")

    # Check if destination exists
    if os.path.exists(destination):
        # If destination is a folder: move source INTO it
        if os.path.isdir(destination):
            target = os.path.join(destination, folder_name)
        else:
            print("[Runner] Destination exists and is not a directory. Aborting.")
            sys.exit(1)
    else:
        # If destination doesn't exist: create it and move INTO it
        try:
            os.makedirs(destination)
        except Exception as e:
            print(f"[Runner] Could not create destination: {e}")
            sys.exit(1)
        target = os.path.join(destination, folder_name)

    try:
        shutil.move(source, target)
        print("[Runner] Move successful.")
    except Exception as e:
        print(f"[Runner] Move failed: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()