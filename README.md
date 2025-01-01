# SpaceTraders Zero

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)

An automated client for the SpaceTraders API game (https://spacetraders.io/). This client provides a robust interface for interacting with the SpaceTraders API, featuring automated trading, resource management, and strategic decision-making capabilities.

## Features

- 🚀 Automated trading and resource management
- 🛸 Ship navigation and fleet management
- 📊 Market analysis and optimal route planning
- 📝 Automated contract handling
- ⚡ High-performance async operations
- 🔒 Secure API token handling
- 🧪 Comprehensive test coverage

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- A SpaceTraders API token (get one at https://spacetraders.io/)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/spacetraders-zero.git
cd spacetraders-zero
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the root directory with your SpaceTraders API token:
```
SPACETRADERS_TOKEN=your_token_here
```

## Usage

Run the client:
```bash
python src/main.py
```

For development and testing:
```bash
# Run tests
pytest

# Type checking
mypy .

# Format code
black .
isort .
```

## Project Structure

```
spacetraders-zero/
├── src/
│   ├── main.py           # Main entry point
│   ├── client.py         # SpaceTraders API client
│   ├── models.py         # Pydantic models
│   ├── automation/       # Automation strategies
│   └── utils/           # Utility functions
├── tests/               # Test suite
├── requirements.txt     # Project dependencies
└── README.md           # This file
```

## Development

This project follows these best practices:
- Type hints for all function signatures
- Comprehensive test coverage
- Clean code principles
- Modern Python async/await patterns
- Proper error handling and logging

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- SpaceTraders API team for providing the game platform
- All contributors who help improve this project 