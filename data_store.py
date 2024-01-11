# data_store.py

# Define the Comprehensive Dictionary Structure
data_store = {
    "key1": {
        "nested_key1": "value1",
        "nested_key2": [
            "item1",
            "item2",
            {"sub_nested_key": "sub_value"}
        ]
    },
    "key2": "simple_value",
    "key3": ["list_item1", {"list_nested_key": "list_nested_value"}]
}


# Implement Recursive Adjustment Function
def adjust_data_recursively(data, condition_func, adjust_func):
    if isinstance(data, dict):
        return {k: adjust_data_recursively(v, condition_func, adjust_func) for k, v in data.items()}
    elif isinstance(data, list):
        return [adjust_data_recursively(item, condition_func, adjust_func) for item in data]
    return adjust_func(data) if condition_func(data) else data


# Define Condition and Adjustment Functions
def should_adjust(value):
    # Define the condition to decide if adjustment is needed
    return isinstance(value, str) and "dark" in value


def adjust_value(value):
    # Define how the value should be adjusted
    return f"adjusted_{value}"


# Apply the Recursive Function
adjusted_data_store = adjust_data_recursively(data_store, should_adjust, adjust_value)


# Testing and Validation
print("Original Data Store:", data_store)
print("Adjusted Data Store:", adjusted_data_store)
