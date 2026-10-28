# Python DNS Resolver

A lightweight Python command-line tool that resolves domain names into IPv4 addresses using Python's built-in `socket` module.

## Overview

This project demonstrates fundamental Python programming concepts and basic network name resolution. It accepts a domain name from the user, attempts to resolve it, and displays the resulting IPv4 address or an error message if resolution fails.

## Features

- **Hostname Resolution:** Resolves domain names to IPv4 addresses.
- **Input Validation:** Rejects empty domain-name input.
- **Error Handling:** Provides readable error messages when hostname resolution fails.
- **Clean Code Structure:** Uses separate functions for DNS resolution and program execution.
- **Type Hints:** Includes basic Python type annotations.

## Technologies Used

- Python 3
- `socket` module
- Command-line interface (CLI)

## Requirements

- Python 3 installed on your system.
- An active network connection and a working system DNS resolver for external hostname lookups.

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
```

Replace the repository URL with your actual GitHub repository URL.

### 2. Navigate to the project directory

```bash
cd YOUR-REPOSITORY
```

### 3. Run the program

```bash
python main.py
```

Depending on your system, you may need to use `python3 main.py` instead.

## Example Usage

```text
DNS Resolver
Enter a domain name (for example, example.com): example.com
example.com resolves to 93.184.216.34
```

*Note: The IP address shown is illustrative. Actual DNS results may vary.*

### Example Error

```text
DNS Resolver
Enter a domain name (for example, example.com): invalid-domain.invalid
Error: Could not resolve hostname: invalid-domain.invalid
```

## How It Works

1. The program requests a domain name from the user.
2. It removes surrounding whitespace and checks whether the input is empty.
3. The `socket.gethostbyname()` function attempts to resolve the hostname to an IPv4 address.
4. If resolution succeeds, the IP address is displayed.
5. If resolution fails, the program displays a readable error message.

## Current Limitations

- Resolves only one IPv4 address per lookup.
- Does not explicitly query individual DNS record types such as MX, NS, TXT, or AAAA.
- Does not provide configurable DNS server selection.
- Does not measure query latency or perform continuous monitoring.
- Depends on the operating system's configured hostname-resolution mechanisms.

## Future Improvements

- Support multiple IPv4 and IPv6 addresses.
- Add DNS record inspection using `dnspython`.
- Introduce configurable DNS resolvers and query timeouts.
- Measure DNS response times.
- Add automated tests and structured logging.
- Develop monitoring, incident reporting, and historical performance tracking.

## Learning Objectives

This project explores Python functions, exception handling, type hints, user input, and basic networking concepts.


**Author:** Atheleia

*An introductory Python networking project focused on hostname resolution and error handling.*
