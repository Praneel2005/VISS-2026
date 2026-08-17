import os
import sys
import json
import shutil
import argparse
import subprocess

def run_git_command(command):
    """Runs a shell command and returns output."""
    try:
        result = subprocess.run(command, check=True, text=True, capture_output=True, shell=True)
        print(f"Git: {result.stdout.strip()}")
    except subprocess.CalledProcessError as e:
        print(f"Error running git command: {command}\nStderr: {e.stderr.strip()}")
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="CEVI Lab Challenge Daily Release Utility")
    parser.add_argument("--id", required=True, help="Unique challenge ID (e.g. day2)")
    parser.add_argument("--title", required=True, help="Display title of the challenge")
    parser.add_argument("--q", required=True, help="HTML-formatted challenge question details")
    parser.add_argument("--imgA", required=True, help="Path to local image A file")
    parser.add_argument("--imgB", required=True, help="Path to local image B file")
    parser.add_argument("--tab", help="Optional Google Sheet tab name (defaults to ID capitalized)")

    args = parser.parse_args()

    challenge_id = args.id.lower().strip()
    config_file = "challenges.json"

    if not os.path.exists(config_file):
        print(f"Error: {config_file} not found in current directory.")
        sys.exit(1)

    # 1. Prepare target image filenames
    _, ext_a = os.path.splitext(args.imgA)
    _, ext_b = os.path.splitext(args.imgB)
    
    ext_a = ext_a if ext_a else ".png"
    ext_b = ext_b if ext_b else ".png"

    dest_img_a = f"{challenge_id}_imgA{ext_a}"
    dest_img_b = f"{challenge_id}_imgB{ext_b}"

    # 2. Copy images into directory
    try:
        shutil.copy(args.imgA, dest_img_a)
        shutil.copy(args.imgB, dest_img_b)
        print(f"Copied image files to: {dest_img_a} and {dest_img_b}")
    except Exception as e:
        print(f"Failed to copy image files: {str(e)}")
        sys.exit(1)

    # 3. Read and update challenges.json
    try:
        with open(config_file, "r") as f:
            config = json.load(f)
    except Exception as e:
        print(f"Error reading {config_file}: {str(e)}")
        sys.exit(1)

    tab_name = args.tab if args.tab else f"Day {challenge_id.replace('day', '')}"

    config["activeChallenge"] = challenge_id
    config["challenges"][challenge_id] = {
        "title": args.title,
        "imageA": dest_img_a,
        "imageB": dest_img_b,
        "question": args.q,
        "tabName": tab_name
    }

    try:
        with open(config_file, "w") as f:
            json.dump(config, f, indent=2)
        print("Updated challenges.json config file successfully.")
    except Exception as e:
        print(f"Failed to write to {config_file}: {str(e)}")
        sys.exit(1)

    # 4. Automate Git flow (commit & push)
    print("Initiating deployment via Git...")
    run_git_command(f'git add challenges.json "{dest_img_a}" "{dest_img_b}"')
    run_git_command(f'git commit -m "Release daily challenge: {challenge_id} - {args.title}"')
    run_git_command('git push origin main')
    print(f"\nSuccess! Challenge '{challenge_id}' is deployed and currently publishing live.")
    print(f"Student Portal: https://praneel2005.github.io/VISS-2026/")
    print(f"Direct Challenge Link: https://praneel2005.github.io/VISS-2026/?challenge={challenge_id}")

if __name__ == "__main__":
    main()
