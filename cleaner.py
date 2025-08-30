import pandas as pd
import sys
import re
import json

if __name__ == "__main__":
	if len(sys.argv) != 3:
		print(f"Usage: python {sys.argv[0]} <input_csv> <output_json>")
		sys.exit(1)
	
	input_path = sys.argv[1]
	output_path = sys.argv[2]

	df = pd.read_csv(input_path)
	print(f"Loaded CSV file: {len(df)} rows.")

	# Keep only italian songs
	df = df[df['language'] == 'it']
	print(f"Filtered to {len(df)} italian songs.")

	# Remove all substrings within [] from the lyrics column and strip whitespace
	df['lyrics'] = df['lyrics'].str.replace(r'\[.*?\]', '', regex=True).str.strip()

	# Replace multiple consecutive newlines with a single newline
	df['lyrics'] = df['lyrics'].str.replace(r'\n+', '\n', regex=True)
	print(f"Cleaned lyrics for {len(df)} songs.")

	# Create a list of dictionaries with title and text fields
	json_data = []
	for index, row in df.iterrows():
		json_data.append({
			"title": row['title'],
			"text": row['lyrics']
		})

	# Save to JSON file
	with open(output_path, 'w', encoding='utf-8') as f:
		json.dump(json_data, f, ensure_ascii=False, indent=2)

	print(f"Saved {len(json_data)} songs to JSON file")