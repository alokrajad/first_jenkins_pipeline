import sys
import yaml

def replace_values(file_path):
    # Load YAML file
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file)
        print(data)
        print(type(data))

    # Perform replacement
    if "x" in data.keys():
        data['x'] = 3

    # Write back to the file
    with open(file_path, 'w') as file:
        yaml.dump(data, file)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python replace_values.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    replace_values(file_path)