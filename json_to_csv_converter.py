#!/usr/bin/env python3
"""
JSON to CSV Converter for FlexPay Scraped Data

This script reads all JSON metadata files from the output/json directory
and combines them into a single CSV file with all the extracted information.
"""

import json
import csv
import os
from pathlib import Path
from typing import List, Dict, Any

def load_json_files(json_dir: str) -> List[Dict[str, Any]]:
    """
    Load all JSON files from the specified directory.
    
    Args:
        json_dir (str): Path to the directory containing JSON files
        
    Returns:
        List[Dict[str, Any]]: List of dictionaries containing JSON data
    """
    json_data = []
    json_path = Path(json_dir)
    
    if not json_path.exists():
        print(f"Error: Directory {json_dir} does not exist")
        return json_data
    
    # Get all JSON files sorted by name, but exclude all_data.json as it's an aggregated file
    json_files = sorted([f for f in json_path.glob("*.json") if f.name != "all_data.json"])
    
    print(f"Found {len(json_files)} JSON files to process (excluding all_data.json)")
    
    for json_file in json_files:
        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                # Add the source filename for reference
                data['source_file'] = json_file.name
                json_data.append(data)
                print(f"✓ Processed: {json_file.name}")
        except json.JSONDecodeError as e:
            print(f"✗ Error reading {json_file.name}: {e}")
        except Exception as e:
            print(f"✗ Unexpected error with {json_file.name}: {e}")
    
    return json_data

def convert_to_csv(json_data: List[Dict[str, Any]], output_file: str) -> None:
    """
    Convert JSON data to CSV format.
    
    Args:
        json_data (List[Dict[str, Any]]): List of dictionaries containing JSON data
        output_file (str): Path to the output CSV file
    """
    if not json_data:
        print("No data to convert")
        return
    
    # Define the CSV columns
    fieldnames = [
        'source_file',
        'url', 
        'filename',
        'title',
        'summary',
        'content_type',
        'importance_score',
        'key_points'
    ]
    
    try:
        with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            # Write header
            writer.writeheader()
            
            # Write data
            for item in json_data:
                # Convert key_points list to a semicolon-separated string for CSV
                row = item.copy()
                if 'key_points' in row and isinstance(row['key_points'], list):
                    row['key_points'] = '; '.join(row['key_points'])
                
                # Ensure all required fields are present
                for field in fieldnames:
                    if field not in row:
                        row[field] = ''
                
                writer.writerow(row)
        
        print(f"✓ Successfully created CSV file: {output_file}")
        print(f"✓ Total records written: {len(json_data)}")
        
    except Exception as e:
        print(f"✗ Error writing CSV file: {e}")

def main():
    """Main function to orchestrate the conversion process."""
    # Define paths
    script_dir = Path(__file__).parent
    json_dir = script_dir / "output" / "json"
    output_file = script_dir / "output" / "combined_metadata.csv"
    
    print("=" * 60)
    print("FlexPay JSON to CSV Converter")
    print("=" * 60)
    print(f"JSON Directory: {json_dir}")
    print(f"Output File: {output_file}")
    print("-" * 60)
    
    # Load JSON files
    json_data = load_json_files(str(json_dir))
    
    if json_data:
        # Convert to CSV
        convert_to_csv(json_data, str(output_file))
        
        print("-" * 60)
        print("Conversion Summary:")
        print(f"  • Files processed: {len(json_data)}")
        print(f"  • Output location: {output_file}")
        
        # Display sample of the data
        if json_data:
            print(f"  • Sample record:")
            sample = json_data[0]
            for key, value in sample.items():
                if key == 'key_points' and isinstance(value, list):
                    print(f"    - {key}: {len(value)} points")
                elif isinstance(value, str) and len(value) > 100:
                    print(f"    - {key}: {value[:100]}...")
                else:
                    print(f"    - {key}: {value}")
    else:
        print("No JSON files were successfully processed.")
    
    print("=" * 60)

if __name__ == "__main__":
    main()
