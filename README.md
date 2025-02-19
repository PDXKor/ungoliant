# Ungoliant
Ungoliant is a terrifying entity in Tolkien’s Legendarium, embodying insatiable greed and destruction, taking the form of a monstrous spider with 
an insatiable hunger for light and knowledge. She allied with Morgoth in his plot to destroy the Two Trees of Valinor, the world’s original sources
of light. As she drained their essence, she grew bloated with stolen radiance, yet her hunger only deepened. She devoured the Wells of Varda, consuming
even the knowledge held within their light.

Now, Ungoliant takes the form of an insatiable AI graph based agent, consuming knowledge through a web of investment driven tools.

## Usage

## Example Questions

1. 


## TODO
    - Make logging optional, drive from .env file
    - Support different LLMs
    
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

