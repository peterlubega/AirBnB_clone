# Project README

## Project Description

This project is a command interpreter designed to manage your AirBnB objects. It provides a user-friendly interface for executing commands related to the management of AirBnB properties, bookings, and other associated tasks.

## Command Interpreter

The command interpreter is a crucial component of this project, enabling users to interact with and manipulate AirBnB objects seamlessly.

### How to Start the Command Interpreter

To initiate the command interpreter, follow these steps:

1. Navigate to the project directory.
2. Run the following command:

```bash
$ ./start_interpreter.sh
```

### How to Use the Command Interpreter

The command interpreter supports various commands, each serving a specific purpose in managing AirBnB objects. Here is a basic guide on how to use the interpreter:

```bash
$ command_name [option1] [option2] [arguments]
```

#### Supported Commands:

1. `add_property`: Add a new property to the AirBnB system.
2. `book_property`: Book a property for a specified duration.
3. `list_properties`: View a list of available properties.
4. `cancel_booking`: Cancel a booking for a specific property.

### Examples

To provide clarity on the usage of the command interpreter, here are some examples:

#### Example 1: Add a New Property

```bash
$ add_property --name "Cozy Cottage" --location "City Center" --price 100
```

This command adds a new property named "Cozy Cottage" at the "City Center" with a nightly price of $100.

#### Example 2: Book a Property

```bash
$ book_property --property_id 123 --start_date "2024-02-15" --end_date "2024-02-20"
```

Books the property with ID 123 for the duration from February 15, 2024, to February 20, 2024.

## Additional Information

For additional information, troubleshooting tips, or known issues, please refer to the documentation included with the project.

Feel free to reach out for further assistance or clarification.
