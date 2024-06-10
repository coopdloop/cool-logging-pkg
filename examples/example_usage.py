from cool_logging.logging import CoolLogger

# Usage in __main__
if __name__ == "__main__":
    # Example usage
    # Set the desired log file path
    logger = CoolLogger(log_file_path="path/to/your/logfile.log")

    @logger.simple_logging
    def example_function():
        print("Example function executed.")

    example_function()
