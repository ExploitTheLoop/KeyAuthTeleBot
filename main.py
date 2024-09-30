import telebot
from keyauth import API

# Insert your Telegram bot token here
bot = telebot.TeleBot('7710856792:AAEl7ucjSs_nQ5t4XgjHrYL8pEb2N7rtL2s')

# Predefined masked license key
default_masked_license_key = "******-******-******-******-******-******"

# Dictionary to store seller keys per user
seller_keys = {}

# Handler for /start command
@bot.message_handler(commands=['start'])
def handle_start(message):
    response = '''Welcome to the License Management Bot! 🤖

This bot allows you to manage licenses using KeyAuth. 

**Available commands:**
/setup <seller_key> - Set your seller key for the current session
/addlicense <expiry> <level> <amount> [masked_license_key] - Add a license key to KeyAuth
/deletelicense <license_key> [user_too] - Delete a license key (optionally remove associated user)
/banlicense <license_key> <reason> - Ban a license key with a reason
/unbanlicense <license_key> - Unban a license key
/addtime <time_in_days> - Add time to Unused keys
/deleteused - Delete all used license key
/deleteunused - Delete all unused license key
/getlicenseinfo <license_key> - Get information about a specific license key
/delete_all_licenses - Delete all licenses associated with your seller key
/resetuser <license_key> - Reset a specific user's license
/resetallusers - Reset all users' licenses
/help - Show available commands and their descriptions

Use /setup to set your seller key before managing licenses.
'''
    bot.reply_to(message, response)

# Handler for /help command
@bot.message_handler(commands=['help'])
def handle_help(message):
    handle_start(message)

# Handler for /setup command
@bot.message_handler(commands=['setup'])
def handle_setup(message):
    try:
        command = message.text.split()
        if len(command) == 2:
            seller_key = command[1]
            user_id = message.from_user.id
            
            # Save seller key for this user
            seller_keys[user_id] = seller_key
            
            bot.reply_to(message, "Seller key has been set successfully.")
        else:
            bot.reply_to(message, '''Usage: /setup <seller_key>
Example: /setup e1aa3fda827cd204413cddc721433a90''')
    except Exception as e:
        bot.reply_to(message, f"Error occurred: {str(e)}")

# Handler for /addlicense command
@bot.message_handler(commands=['addlicense'])
def handle_addlicense(message):
    try:
        command = message.text.split()
        user_id = message.from_user.id
        
        if user_id not in seller_keys:
            bot.reply_to(message, "Error: Seller key not set. Use /setup <seller_key> to set it.")
            return
        
        seller_key = seller_keys[user_id]
        
        if len(command) >= 4:
            expiry = int(command[1])  # Convert expiry to integer (days)
            level = int(command[2])   # Convert level to integer
            amount = int(command[3])  # Convert amount to integer
            
            masked_license_key = command[4] if len(command) == 5 else default_masked_license_key
            
            api = API(seller_key)
            response = api.add_license(masked_license_key, expiry, level, amount)
            bot.reply_to(message, f"License added: {response}")
        else:
            bot.reply_to(message, '''Usage: /addlicense <expiry> <level> <amount> [masked_license_key]
Example: /addlicense 1 1 1 ABCD-EFGH-IJKL-MNOP-QRST-UVWX''')
    except Exception as e:
        bot.reply_to(message, f"Error occurred: {str(e)}")

# Handler for /resetuser command
@bot.message_handler(commands=['resetuser'])
def handle_resetuser(message):
    try:
        command = message.text.split()
        user_id = message.from_user.id
        
        if user_id not in seller_keys:
            bot.reply_to(message, "Error: Seller key not set. Use /setup <seller_key> to set it.")
            return
        
        seller_key = seller_keys[user_id]
        
        if len(command) == 2:
            license_key = command[1]
            
            api = API(seller_key)
            response = api.reset_user(license_key)  # Assuming `reset_user` is a valid method in the KeyAuth API
            bot.reply_to(message, f"User license reset: {response}")
        else:
            bot.reply_to(message, '''Usage: /resetuser <license_key>
Example: /resetuser ABCD-EFGH-IJKL-MNOP''')
    except Exception as e:
        bot.reply_to(message, f"Error occurred: {str(e)}")

# Handler for /resetallusers command
@bot.message_handler(commands=['resetallusers'])
def handle_resetallusers(message):
    try:
        user_id = message.from_user.id
        
        if user_id not in seller_keys:
            bot.reply_to(message, "Error: Seller key not set. Use /setup <seller_key> to set it.")
            return
        
        seller_key = seller_keys[user_id]
        
        api = API(seller_key)
        response = api.reset_all_users()  # Assuming `reset_all_users` is a valid method in the KeyAuth API
        bot.reply_to(message, f"All user licenses reset: {response}")
    except Exception as e:
        bot.reply_to(message, f"Error occurred: {str(e)}")

# Handler for /deletelicense command
@bot.message_handler(commands=['deletelicense'])
def handle_deletelicense(message):
    try:
        command = message.text.split()
        user_id = message.from_user.id
        
        if user_id not in seller_keys:
            bot.reply_to(message, "Error: Seller key not set. Use /setup <seller_key> to set it.")
            return
        
        seller_key = seller_keys[user_id]
        
        if len(command) >= 2:
            license_key = command[1]  
            user_too = int(command[2]) if len(command) == 3 else 0  
            
            api = API(seller_key)
            response = api.delete_license(license_key, user_too)
            bot.reply_to(message, f"License deleted: {response}")
        else:
            bot.reply_to(message, '''Usage: /deletelicense <license_key> [user_too]
Example: /deletelicense ABCD-EFGH-IJKL-MNOP 1''')
    except Exception as e:
        bot.reply_to(message, f"Error occurred: {str(e)}")

# Handler for /deleteused command
@bot.message_handler(commands=['deleteused'])
def handle_deleteused(message):
    try:
        user_id = message.from_user.id
        
        if user_id not in seller_keys:
            bot.reply_to(message, "Error: Seller key not set. Use /setup <seller_key> to set it.")
            return
        
        seller_key = seller_keys[user_id]
        

            
        api = API(seller_key)
        response = api.delete_used()
        bot.reply_to(message, f"Used license deleted: {response}")
    except Exception as e:
        bot.reply_to(message, f"Error occurred: {str(e)}")

# Handler for /deleteunused command
@bot.message_handler(commands=['deleteunused'])
def handle_deleteunused(message):
    try:
      
        user_id = message.from_user.id
        
        if user_id not in seller_keys:
            bot.reply_to(message, "Error: Seller key not set. Use /setup <seller_key> to set it.")
            return
        
        seller_key = seller_keys[user_id]
        
        api = API(seller_key)
        response = api.delete_unused()
        bot.reply_to(message, f"Unused license deleted: {response}")
    except Exception as e:
        bot.reply_to(message, f"Error occurred: {str(e)}")

# Handler for /banlicense command
@bot.message_handler(commands=['banlicense'])
def handle_banlicense(message):
    try:
        command = message.text.split()
        user_id = message.from_user.id
        
        if user_id not in seller_keys:
            bot.reply_to(message, "Error: Seller key not set. Use /setup <seller_key> to set it.")
            return
        
        seller_key = seller_keys[user_id]
        
        if len(command) >= 3:
            license_key = command[1]
            reason = " ".join(command[2:])  # Join the rest of the command as the reason
            
            api = API(seller_key)
            response = api.ban_license(license_key, reason)
            bot.reply_to(message, f"License banned: {response}")
        else:
            bot.reply_to(message, '''Usage: /banlicense <license_key> <reason>
Example: /banlicense ABCD-EFGH-IJKL-MNOP Cheating''')
    except Exception as e:
        bot.reply_to(message, f"Error occurred: {str(e)}")

# Handler for /unbanlicense command
@bot.message_handler(commands=['unbanlicense'])
def handle_unbanlicense(message):
    try:
        command = message.text.split()
        user_id = message.from_user.id
        
        if user_id not in seller_keys:
            bot.reply_to(message, "Error: Seller key not set. Use /setup <seller_key> to set it.")
            return
        
        seller_key = seller_keys[user_id]
        
        if len(command) == 2:
            license_key = command[1]
            
            api = API(seller_key)
            response = api.unban_license(license_key)
            bot.reply_to(message, f"License unbanned: {response}")
        else:
            bot.reply_to(message, '''Usage: /unbanlicense <license_key>
Example: /unbanlicense ABCD-EFGH-IJKL-MNOP''')
    except Exception as e:
        bot.reply_to(message, f"Error occurred: {str(e)}")

# Handler for /addtime command
@bot.message_handler(commands=['addtime'])
def handle_addtime(message):
    try:
        command = message.text.split()
        user_id = message.from_user.id
        
        if user_id not in seller_keys:
            bot.reply_to(message, "Error: Seller key not set. Use /setup <seller_key> to set it.")
            return
        
        seller_key = seller_keys[user_id]
        
        if len(command) == 2:
            time_in_days = int(command[1])
            
            api = API(seller_key)
            response = api.add_time(time_in_days)
            bot.reply_to(message, f"Time added: {response}")
        else:
            bot.reply_to(message, '''Usage: /addtime <time_in_days>
Example: /addtime 30''')
    except Exception as e:
        bot.reply_to(message, f"Error occurred: {str(e)}")

# Handler for /getlicenseinfo command
@bot.message_handler(commands=['getlicenseinfo'])
def handle_getlicenseinfo(message):
    try:
        command = message.text.split()
        user_id = message.from_user.id
        
        if user_id not in seller_keys:
            bot.reply_to(message, "Error: Seller key not set. Use /setup <seller_key> to set it.")
            return
        
        seller_key = seller_keys[user_id]
        
        if len(command) == 2:
            license_key = command[1]
            
            api = API(seller_key)
            response = api.get_license_info(license_key)
            bot.reply_to(message, f"License info: {response}")
        else:
            bot.reply_to(message, '''Usage: /getlicenseinfo <license_key>
Example: /getlicenseinfo ABCD-EFGH-IJKL-MNOP''')
    except Exception as e:
        bot.reply_to(message, f"Error occurred: {str(e)}")

# Handler for /delete_all_licenses command
@bot.message_handler(commands=['delete_all_licenses'])
def handle_delete_all_licenses(message):
    try:
        user_id = message.from_user.id
        
        if user_id not in seller_keys:
            bot.reply_to(message, "Error: Seller key not set. Use /setup <seller_key> to set it.")
            return
        
        seller_key = seller_keys[user_id]
        
        api = API(seller_key)
        response = api.delete_all_licenses()
        bot.reply_to(message, f"All licenses deleted: {response}")
    except Exception as e:
        bot.reply_to(message, f"Error occurred: {str(e)}")

# Polling loop to run the bot
bot.polling(none_stop=True)
