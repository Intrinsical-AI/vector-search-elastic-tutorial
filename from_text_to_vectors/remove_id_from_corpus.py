import pandas as pd
import sys

def main():
    """Remove the document id column from a TSV corpus file."""
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <input_tsv> <output_tsv>")
        return
    # MS Marco corpus file
    input_filename = sys.argv[1]
    # New file without id
    output_filename = sys.argv[2]
    remove_id_from_corpus(input_filename, output_filename)


def remove_id_from_corpus(input_filename, output_filename):
    """Write a copy of the corpus without the identifier column."""
    try:
        df = pd.read_csv(input_filename, sep='\t', names=["id", "general_text"])
        df.drop("id", axis=1, inplace=True)
        df.to_csv(output_filename, sep="\t", index=False, header=False)
    except FileNotFoundError as exc:
        print(f"Error: file '{exc.filename}' not found.")
        sys.exit(1)

if __name__ == "__main__":
    main()
