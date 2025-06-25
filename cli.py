# cli.py
import sys
import os

def main():
    if len(sys.argv) != 2:
        print("Usage: tablecloth <destination_path>")
        sys.exit(1)

    dest_path = os.path.abspath(sys.argv[1])
    cwd = os.getcwd()

    print(f"[CLI] Preparing to move this folder:")
    print(f"    FROM: {cwd}")
    print(f"    TO:   {dest_path}")

    # Placeholder — we will launch runner here in the next step
    print("[CLI] Not launching runner yet (coming soon)")

if __name__ == "__main__":
    main()
