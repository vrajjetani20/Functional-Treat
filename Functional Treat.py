# Global variables to track data metrics across the program
TOTAL_COUNT = 0
GLOBAL_MEAN = 0.0

# This variable will hold our list of numbers
DATASET = []

def input_data():
    """This function handles taking numbers from the user."""
    global DATASET
    print("\n--- Step 1: Input Data ---")
    print("1. Enter your own numbers")
    print("2. Load default sample data")
    
    choice = input("Choose an option (1 or 2): ")
    
    if choice == "1":
        user_input = input("Enter numbers separated by spaces: ")
        # Convert the space-separated string into a list of integers
        DATASET = []
        for item in user_input.split():
            if item.isdigit():
                DATASET.append(int(item))
        print("Data has been stored successfully!")
        
    else:
        # Default fallback sample data from your screenshot template
        DATASET = [34, 12, 56, 78, 43, 21, 90]
        print("Loaded sample data: 34, 12, 56, 78, 43, 21, 90")
    
    # Automatically update the global summaries whenever data changes
    update_global_metrics()


def update_global_metrics():
    """Updates global variables using basic built-in math tools."""
    global TOTAL_COUNT, GLOBAL_MEAN
    if len(DATASET) > 0:
        TOTAL_COUNT = len(DATASET)
        GLOBAL_MEAN = sum(DATASET) / len(DATASET)


def display_data_summary():
    """Displays basic statistics using Python's simple built-in functions."""
    if not DATASET:
        print("\n[Warning] No data found. Please input data first!")
        return
        
    print("\nData Summary:")
    print(" - Total elements:", len(DATASET))
    print(" - Minimum value:", min(DATASET))
    print(" - Maximum value:", max(DATASET))
    print(" - Sum of all values:", sum(DATASET))
    
    # Calculate average
    avg = sum(DATASET) / len(DATASET)
    print(f" - Average value: {avg:.2f}")


def calculate_factorial(n):
    """A basic recursive function to find the factorial of a number."""
    if n == 0 or n == 1:
        return 1
    return n * calculate_factorial(n - 1)


def run_factorial_option():
    """Helper function to interact with the recursive factorial feature."""
    num_str = input("\nEnter a number to calculate its factorial: ")
    if num_str.isdigit():
        num = int(num_str)
        result = calculate_factorial(num)
        print(f"Factorial of {num} is: {result}")
    else:
        print("Invalid integer entered.")


def filter_with_lambda():
    """Filters data matching a condition using a straightforward lambda layout."""
    if not DATASET:
        print("\nNo data to filter. Please input data first.")
        return

    threshold_str = input("\nEnter a threshold value to filter out data above this value: ")
    if not threshold_str.isdigit():
        print("Please enter a valid number.")
        return
        
    threshold = int(threshold_str)
    
    # Requirement E: Lambda function to check if a value is greater than or equal to threshold
    is_above_threshold = lambda x: x >= threshold
    
    filtered_list = []
    for num in DATASET:
        if is_above_threshold(num):
            filtered_list.append(num)
            
    print(f"\nFiltered Data (values >= {threshold}):")
    print(filtered_list)


def sort_dataset():
    """Sorts data based on basic selection criteria rules."""
    if not DATASET:
        print("\nNo data to sort.")
        return

    print("\nChoose sorting option:")
    print("1. Ascending")
    print("2. Descending")
    choice = input("Enter your choice: ")

    if choice == "2":
        DATASET.sort(reverse=True)
        print("\nSorted Data in Descending Order:")
    else:
        DATASET.sort()
        print("\nSorted Data in Ascending Order:")
        
    print(DATASET)


def get_multiple_values():
    """Requirement G: Returns multiple pieces of information at once."""
    if not DATASET:
        return 0, 0, 0, 0.0
        
    minimum = min(DATASET)
    maximum = max(DATASET)
    total_sum = sum(DATASET)
    average = total_sum / len(DATASET)
    
    return minimum, maximum, total_sum, average


def display_dataset_statistics():
    """Receives and unpacks multiple values returned by a single function."""
    # Unpack values step-by-step
    minimum, maximum, total_sum, average = get_multiple_values()
    
    print("\nDataset Statistics:")
    print(" - Minimum value:", minimum)
    print(" - Maximum value:", maximum)
    print(" - Sum of all values:", total_sum)
    print(f" - Average value: {average:.2f}")


def dataset_summary_kwargs(**kwargs):
    """Requirement C: Uses **kwargs to print summary features dynamically."""
    print("\nDataset Characteristics Summary:")
    for key, value in kwargs.items():
        print(f" - {key}: {value}")


def show_advanced_summary():
    """Passes global properties dynamically into the kwargs dictionary collector."""
    dataset_summary_kwargs(
        total_tracked_elements=TOTAL_COUNT,
        computed_global_average=round(GLOBAL_MEAN, 2)
    )


def main():
    """The main core menu structure loop."""
    while True:
        print("\n================================================")
        print("Main Menu:")
        print("1. Input Data")
        print("2. Display Data Summary (Built-in Functions)")
        print("3. Calculate Factorial (Recursion)")
        print("4. Filter Data by Threshold (Lambda Function)")
        print("5. Sort Data")
        print("6. Display Dataset Statistics (Return Multiple Values)")
        print("7. View Tracked Metrics Info (**kwargs)")
        print("8. Exit Program")
        print("================================================")
        
        choice = input("Please enter your choice: ").strip()

        if choice == "1":
            input_data()
        elif choice == "2":
            display_data_summary()
        elif choice == "3":
            run_factorial_option()
        elif choice == "4":
            filter_with_lambda()
        elif choice == "5":
            sort_dataset()
        elif choice == "6":
            display_dataset_statistics()
        elif choice == "7":
            show_advanced_summary()
        elif choice == "8":
            print("\nThank you for using the Data Analyzer and Transformer Program. ")
            print("\nIf you need ' Help ' Any time Come Back..! ")
            print("\nThank you ")
            print("\nGoodBye..! ")
            break
        else:
            print("\nInvalid choice. Please select a valid number from 1 to 8.")


# Start the program execution loop 
if __name__ == "__main__":
    main()
