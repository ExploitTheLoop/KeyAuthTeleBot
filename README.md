
# Telegram License Management Bot

This Telegram bot allows users to manage software licenses through the KeyAuth API. The bot provides features like generating, deleting, resetting, and managing licenses via Telegram commands. It leverages the [KeyAuth API](https://keyauth.cc) for all license-related functionalities.

## Features

- **Setup Seller Key**: Set the KeyAuth seller key for your bot session.
- **Generate License**: Create new license keys with custom expiry, level, and amount.
- **Delete License**: Remove a license key and optionally delete associated users.
- **Ban/Unban License**: Ban or unban licenses with a specific reason.
- **Extend License Time**: Add time to unused keys.
- **Reset User**: Reset a specific user's license.
- **Delete All Licenses**: Remove all licenses associated with your seller key.
- **Delete Used/Unused Licenses**: Delete used or unused license keys.
- **Retrieve License Info**: Get detailed information about a specific license key.

## Requirements

- Python 3.6+
- [KeyAuth API](https://keyauth.cc) account
- Telegram bot token

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/telegram-license-management-bot.git
   cd telegram-license-management-bot
   ```

2. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Configure the bot**:

   Open the `main.py` file and add your Telegram bot token:

   ```python
   bot = telebot.TeleBot('<YOUR_TELEGRAM_BOT_TOKEN>')
   ```

4. **Run the bot**:

   ```bash
   python main.py
   ```

## Usage

Once the bot is up and running, you can use the following commands through Telegram to manage licenses.

### License Management Commands

- **/setup `<seller_key>`**: Set your KeyAuth seller key.
- **/addlicense `<expiry>` `<level>` `<amount>` `[masked_license_key]`**: Generate new license keys.
- **/deletelicense `<license_key>` `[delete_user_too]`**: Delete a license and optionally the associated user.
- **/banlicense `<license_key>` `<reason>`**: Ban a license.
- **/unbanlicense `<license_key>`**: Unban a banned license.
- **/addtime `<days>`**: Add time to unused keys.
- **/resetuser `<license_key>`**: Reset a user's license.
- **/delete_all_licenses**: Delete all licenses under your seller key.
- **/deleteused**: Delete all used licenses.
- **/deleteunused**: Delete all unused licenses.
- **/getlicenseinfo `<license_key>`**: Retrieve license details.

## Example Commands

- `/setup abcd1234abcd5678efgh`: Sets the seller key for managing licenses.
- `/addlicense 30 1 5 ABCD-EFGH-IJKL`: Generates 5 licenses with 30-day expiry and level 1.
- `/deletelicense ABCD-EFGH-IJKL 1`: Deletes a specific license and the associated user.

## Contributing

Contributions are welcome! Feel free to fork this repository and submit pull requests or open issues.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- [KeyAuth](https://keyauth.cc) for the license management API.
- [PyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI) for the Telegram bot framework.
