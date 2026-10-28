
import json
from pathlib import Path

from resume_reader import extract_resume_text
from resume_parser import create_resume_json


INPUT_DIR = Path("input_resumes")
TEXT_OUTPUT_DIR = Path("extracted_text")
JSON_OUTPUT_DIR = Path("candidate_json")

SUPPORTED_EXTENSIONS = {".pdf", ".docx", ".txt"}


def main():
    # Create output directories if they do not exist.
    TEXT_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    JSON_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    if not INPUT_DIR.exists():
        print(f"Input directory not found: {INPUT_DIR}")
        return

    resume_files = sorted(
        path
        for path in INPUT_DIR.iterdir()
        if path.is_file()
        and path.suffix.lower() in SUPPORTED_EXTENSIONS
    )

    if not resume_files:
        print(f"No supported resume files found in {INPUT_DIR}")
        return

    successful = 0
    failed = 0

    for file_path in resume_files:
        print(f"\nProcessing: {file_path.name}")

        try:
            # Step 1: Extract the resume text.
            text = extract_resume_text(file_path)

            # Step 2: Save the extracted text.
            text_output_path = (
                TEXT_OUTPUT_DIR / f"{file_path.stem}.txt"
            )
            text_output_path.write_text(
                text,
                encoding="utf-8",
            )

            print(f"Text saved: {text_output_path}")

            # Step 3: Convert the extracted text into structured JSON.
            candidate_data = create_resume_json(text)

            # Step 4: Save the candidate JSON.
            json_output_path = (
                JSON_OUTPUT_DIR / f"{file_path.stem}.json"
            )
            json_output_path.write_text(
                json.dumps(
                    candidate_data,
                    indent=2,
                    ensure_ascii=False,
                ),
                encoding="utf-8",
            )

            print(f"JSON saved: {json_output_path}")
            successful += 1

        except Exception as error:
            failed += 1
            print(f"Failed: {file_path.name}: {error}")

    print("\n========== Processing Summary ==========")
    print(f"Total resumes: {len(resume_files)}")
    print(f"Successful:    {successful}")
    print(f"Failed:        {failed}")


if __name__ == "__main__":
    main()