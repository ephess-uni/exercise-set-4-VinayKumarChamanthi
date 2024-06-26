""" ex_4_0.py """
try:
    from src.util import get_data_file_path
except ImportError:
    from util import get_data_file_path

# Use this FILENAME variable to test your function.
FILENAME = get_data_file_path('messages.log')
# >>>> DO NOT MODIFY CODE ABOVE <<<<


def get_shutdown_events(logfile):
    """
    Your docstring here.  Replace the pass keyword below with your implementation
    """
    shutdown_events = []  # Initialize an empty list to store shutdown events
    with open(logfile, 'r') as file:
        for line in file:
            if "Shutdown initiated" in line:  # Check if the line contains "Shutdown initiated"
                shutdown_events.append(line.strip())  # Add the line to the list
    
    return shutdown_events  # Return the list of shutdown events


# >>>> The code below will call your function and print the results
if __name__ == "__main__":
    print(f"{get_shutdown_events(FILENAME)=}")
