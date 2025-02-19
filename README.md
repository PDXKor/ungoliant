# Ungoliant
Ungoliant is a terrifying entity in Tolkien’s Legendarium, embodying insatiable greed and destruction, taking the form of a monstrous spider with 
an insatiable hunger for light and knowledge. She allied with Morgoth in his plot to destroy the Two Trees of Valinor, the world’s original sources
of light. As she drained their essence, she grew bloated with stolen radiance, yet her hunger only deepened. She devoured the Wells of Varda, consuming
even the knowledge held within their light.

Now, Ungoliant takes the form of an insatiable AI graph based agent, consuming knowledge through a web of investment driven tools.

## Usage
Once installed, you can use the command `ugl` to start the program. After that you can ask questions directly in the CLI.

## Example Questions

1. What was Apple's stock price yesterday?

```
Assistant: The stock price of Apple (AAPL) on February 18, 2025, was as follows:
- **Open:** $244.15
- **High:** $245.18
- **Low:** $241.84
- **Close:** $244.47
```

2. What did Apple report as their most recent annual revenue number?

```
Assistant: The most recent revenue figure for Apple Inc. (ticker: AAPL) is **$391.04 billion** for the fiscal year ending on September 30, 2024.
```

# Installation
Install ungoliant as a package. Once installed, you will need to add a .env file to the parent dir with the following environment variables, or have the environment variables set on your machine:

- `POLYGON_API_KEY` - The API Key for the Polygon API. You can get one here: https://polygon.io/
- `POLYGON_API_URL` - The base url for the Polygon URL you are using e.g.  `https://api.polygon.io/v1`
- `OPEN_API_KEY` - The API key for OpenAI. Please note that you should have the model `gpt-4o-mini` enabled for your account.

