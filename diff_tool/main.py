import sys
from utils import read_file, generate_diff


def main():
    try:
        if len(sys.argv) != 3:
            raise ValueError("Usage: python main.py <file1> <file2>")

        file1_path = sys.argv[1]
        file2_path = sys.argv[2]

        file1_lines = read_file(file1_path)
        file2_lines = read_file(file2_path)

        if file1_lines is None or file2_lines is None:
            raise Exception("File reading failed. Cannot generate diff.")

        generate_diff(file1_lines, file2_lines)

    except ValueError as ve:
        print(f"[INPUT ERROR] {ve}")

    except Exception as e:
        print(f"[GENERAL ERROR] {e}")


if __name__ == "__main__":
    main()