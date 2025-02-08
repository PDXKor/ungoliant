# Installation

## With venv

1. Navigate to the `ungoliant` directory (this should be the second `ungoliant` directory):
    ```bash
    cd ungoliant
    ```

2. Create a virtual environment:
    ```bash
    python -m venv venv
    ```

3. Activate the virtual environment:
    - On Windows:
      ```bash
      venv\Scripts\activate
      ```
    - On macOS/Linux:
      ```bash
      source venv/bin/activate
      ```

4. Install the package in editable mode:
    ```bash
    pip install -e .
    ```

5. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

6. Create a `.env` file in the root of the project directory and populate the following values:
    - `POLYGON_API_KEY`
    - `POLYGON_API_URL`
    - `OPEN_API_KEY`


## TODO
    - Make logging optional, drive from .env file
    - Support different LLMs
    