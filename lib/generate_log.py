from datetime import datetime


def generate_log(data):
    """Generate a timestamped log file from a list of entries."""

    # Validate input
    if not isinstance(data, list):
        raise ValueError("Log data must be provided as a list.")

    # Generate filename with today's date
    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    # Write log entries to the file
    with open(filename, "w") as file:
        for entry in data:
            file.write(f"{entry}\n")

    # Print confirmation message
    print(f"Log written to {filename}")

    # Return the filename
    return filename


if __name__ == "__main__":
    log_data = [
        "User logged in",
        "User updated profile",
        "Report exported"
    ]

    generate_log(log_data)
