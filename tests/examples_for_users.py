"""Example usage of PFASProphet predictor.

This script demonstrates how to use the PFASProphet class to make predictions
Example 1: Predict from direct lists of masses and fragments.
Example 2: Predict from a CSV file with default column names.
Example 3: Predict from neutral masses.
Example 4: Predict from a CSV file with custom column names.
Example 5: Append scores back into a CSV file.

"""

import shutil
from pathlib import Path

import pandas as pd

from PFASProphet.predictor import PFASProphet


if __name__ == "__main__":
    # Replace these with your own values
    mass = [248.9461, 298.9427]
    fragments = [
        [63.9624, 77.9654, 118.9921],
        [79.9566, 98.9557, 348.9388],
    ]

    # Use your own CSV path here if needed
    example_csv = Path(__file__).parent / "example_compounds_to_process.csv"

    model = PFASProphet()

    # Example 1: predict from lists (quick sanity check)
    list_scores = model.predict(mass=mass, fragments=fragments)
    print("Scores from lists:", list_scores)

    # Example 2: predict from CSV with default column names (mass, fragments)
    csv_scores = model.predict(file_path=str(example_csv))
    print("Scores from CSV:", csv_scores)

    # Example 3: neutral masses (set is_ionised=False if your masses are neutral)
    neutral_scores = model.predict(mass=mass, fragments=fragments, is_ionised=False)
    print("Scores from neutral masses:", neutral_scores)

    # Example 4: CSV with custom column names.
    # Change these to match YOUR CSV headers.
    user_mass_col = "precursor_mz"
    user_frag_col = "frag_list"

    # We make a temp copy so you can keep the original file untouched.
    df = pd.read_csv(example_csv)
    df_custom = df.rename(columns={"mass": user_mass_col, "fragments": user_frag_col})
    custom_csv = example_csv.with_name("example_custom_cols.csv")
    df_custom.to_csv(custom_csv, index=False)

    custom_scores = model.predict(
        file_path=str(custom_csv), mass_col=user_mass_col, fragments_col=user_frag_col
    )
    print("Scores from CSV (custom cols):", custom_scores)

    # Example 5: append scores back into a copy of the CSV (in_file=True).
    # If you want to write into your original file, point file_path to it directly.
    writable_csv = example_csv.with_name("example_with_scores.csv")
    shutil.copyfile(example_csv, writable_csv)  # keep the source CSV clean
    _ = model.predict(file_path=str(writable_csv), in_file=True)
    print(f"Scores appended to: {writable_csv}")
