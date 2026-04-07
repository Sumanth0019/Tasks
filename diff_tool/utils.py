import difflib

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.readlines()
    except FileNotFoundError:
        print(f"[ERROR] File not found: {file_path}")
        return None
    except PermissionError:
        print(f"[ERROR] Permission denied: {file_path}")
        return None
    except Exception as e:
        print(f"[ERROR] Unexpected error while reading {file_path}: {e}")
        return None


def generate_diff(file1_lines, file2_lines, output_file="output.diff"):
    try:
        diff = difflib.unified_diff(
            file1_lines,
            file2_lines,
            fromfile='file1',
            tofile='file2',
            lineterm=''
        )

        with open(output_file, 'w') as f:
            for line in diff:
                f.write(line + '\n')

        print(f"[SUCCESS] Diff file generated: {output_file}")

    except Exception as e:
        print(f"[ERROR] Failed to generate diff: {e}")