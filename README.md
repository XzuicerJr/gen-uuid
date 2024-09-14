# UUID Generator

This is a simple and small script developed to help me generate UUIDs for my projects more efficiently.

## Why did I create this?

Short answer: I was tired of going online to generate a UUID every time I needed one for a small test or some dummy data to test the frontend of my projects.

Long answer: {{ short answer 👆🏼 }} + I know there are already many ways to generate UUIDs, but I wanted an excuse to use Python for something "useful." So, I decided to create this simple script that I can run in my terminal to get a UUID in just a few seconds.

## How to use it?

1. Clone this repository.

2. Install the dependencies with `pip3 install -r requirements.txt`.

3. Run the script with `python3 uuid_generator.py`.

4. That's it! The generated UUID will be copied to your clipboard and displayed in the terminal. 🎉

5. (Optional) You can create an alias for the script in your `.bashrc` or `.zshrc` file to run it from anywhere in your terminal.

## Flags

- `-h` or `--help`: Show the help message.
- `{number}`: Generate multiple UUIDs at once (e.g., `python3 uuid_generator.py 5`).
  - If no number is provided, the script will generate one UUID by default.
- Maybe more in the future... 🤔 Let me know if you think of something useful, or feel free to make a PR! 👀
