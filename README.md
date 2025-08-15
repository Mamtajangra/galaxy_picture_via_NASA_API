# universe_report

Fetches NASA's Astronomy Picture of the Day (APOD) and prints the image URL.

## Features

- Retrieves APOD data from NASA's API
- Prints the image URL (HD if available)
- Uses environment variables for API keys

## Setup

1. Clone the repository.
2. Create a `.env` file with your NASA API key and bot token:
    ```
    API=your_nasa_api_key
    BOT_TOKEN=your_bot_token
    ```
3. Install dependencies:
    ```sh
    pip install requests python-dotenv
    ```

## Usage

Run the script:
```sh
python image.py
```

## Example Output

![APOD Example](https://apod.nasa.gov/apod/image/2508/IMG_20250813_202125_2048.jpg)

## License

MIT