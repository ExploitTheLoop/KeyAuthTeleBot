import requests  # For making HTTP requests

class API:
    def __init__(self, sellerkey):
        self.sellerkey = sellerkey

    def add_license(self, key, expiry, level=1, amount=1):
        url = (
            f"https://keyauth.win/api/seller/"
            f"?sellerkey={self.sellerkey}"
            f"&type=add"
            f"&expiry={expiry}"
            f"&mask={key}"
            f"&level={level}"
            f"&amount={amount}"
            f"&format=text"  # Keeping the response format as text
        )
        return self.__send_request(url)

    def delete_license(self, key, user_too=0):
        url = (
            f"https://keyauth.win/api/seller/"
            f"?sellerkey={self.sellerkey}"
            f"&type=del"
            f"&key={key}"
            f"&userToo={user_too}"
            f"&format=text"  # Keeping the response format as text
        )
        return self.__send_request(url)

    def ban_license(self, key, reason, user_too=False):
        user_too_int = 1 if user_too else 0
        url = (
            f"https://keyauth.win/api/seller/"
            f"?sellerkey={self.sellerkey}"
            f"&type=ban"
            f"&key={key}"
            f"&reason={reason}"
            f"&userToo={user_too_int}"
            f"&format=text"  # Keeping the response format as text
        )
        return self.__send_request(url)

    def unban_license(self, key):
        url = (
            f"https://keyauth.win/api/seller/"
            f"?sellerkey={self.sellerkey}"
            f"&type=unban"
            f"&key={key}"
            f"&format=text"  # Keeping the response format as text
        )
        return self.__send_request(url)

    def add_time(self, time):
        url = (
            f"https://keyauth.win/api/seller/"
            f"?sellerkey={self.sellerkey}"
            f"&type=addtime"
            f"&time={time}"
        )
        return self.__send_request(url)

    def delete_unused(self):
        url = (
            f"https://keyauth.win/api/seller/"
            f"?sellerkey={self.sellerkey}"
            f"&type=delunused"
            f"&format=text"  # Keeping the response format as text
        )
        return self.__send_request(url)

    def delete_used(self):
        url = (
            f"https://keyauth.win/api/seller/"
            f"?sellerkey={self.sellerkey}"
            f"&type=delused"
            f"&format=text"  # Keeping the response format as text
        )
        return self.__send_request(url)

    def delete_all_licenses(self):
        """
        Delete all licenses associated with the seller key using the seller API.
        
        :return: Response text from the server or an error message.
        """
        url = (
            f"https://keyauth.win/api/seller/"
            f"?sellerkey={self.sellerkey}"
            f"&type=delalllicenses"
            f"&format=text"  # Keeping the response format as text
        )
        return self.__send_request(url)

    def get_license_info(self, key):
        """
        Retrieve information about a specific license key.

        :param key: The license key to retrieve information for.
        :return: Response text containing license information or an error message.
        """
        url = (
            f"https://keyauth.win/api/seller/"
            f"?sellerkey={self.sellerkey}"
            f"&type=info"
            f"&key={key}"
            f"&format=text"  # Keeping the response format as text
        )
        return self.__send_request(url)

    def reset_user(self, username, notify=False):
        """
        Reset the user's license key.

        :param username: The username of the user whose key is to be reset.
        :param notify: Whether to notify the user about the reset (default is False).
        :return: Response text containing the result of the operation.
        """
        notify_int = 1 if notify else 0
        url = (
            f"https://keyauth.win/api/seller/"
            f"?sellerkey={self.sellerkey}"
            f"&type=resetuser"
            f"&username={username}"
            f"&notify={notify_int}"
            f"&format=text"  # Keeping the response format as text
        )
        return self.__send_request(url)

    def reset_all_users(self):
        """
        Reset all users' HWIDs associated with the seller key using the seller API.
        
        :return: Response text from the server or an error message.
        """
        url = (
            f"https://keyauth.win/api/seller/"
            f"?sellerkey={self.sellerkey}"
            f"&type=resetalluser"
            f"&format=text"  # Keeping the response format as text
        )
        return self.__send_request(url)

    def __send_request(self, url):
        """
        Send a GET request to the provided URL.
        
        :param url: The full URL to send the request to.
        :return: The response text or an error message.
        """
        try:
            response = requests.get(url, timeout=10)

            # Print the response text for debugging
            print("Response received:", response.text)

            # Return the response text as this is expected in 'text' format
            return response.text
        except requests.exceptions.Timeout:
            return "Request timed out. Server is probably down/slow at the moment."
        except requests.exceptions.RequestException as e:
            return f"An error occurred during the request: {str(e)}"
        except Exception as e:
            return f"An unexpected error occurred: {str(e)}"
