import chardet

def detect_and_convert_encoding(file_path):
    try:
        # Detect the encoding of the file
        with open(file_path, "rb") as file:
            raw_data = file.read()
            encoding = chardet.detect(raw_data)['encoding']

        print(f"Detected file encoding: {encoding}")

        # Convert to UTF-8 if not already
        if encoding.lower() != "utf-8":
            with open(file_path, "r", encoding=encoding) as file:
                content = file.read()

            with open(file_path, "w", encoding="utf-8") as file:
                file.write(content)

            print("File converted to UTF-8 encoding.")
    except Exception as e:
        print(f"Error detecting encoding: {e}")
        encoding = "utf-8"

        with open(file_path, "r", encoding=encoding) as file:
            content = file.read()

        with open(file_path, "w", encoding="utf-8") as file:
            file.write(content)

        print("File converted to UTF-8 encoding with default encoding.")

if __name__ == "__main__":
    detect_and_convert_encoding("fortran/calculate_emissions.f90")
