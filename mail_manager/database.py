import logging
import os

from .email import Email
from .folder import Folder
from .exceptions import MailManagerException
from .linked_list import LinkedList


class DatabaseConfiguration:
    """
    This class allow us to configure all the different parameters of the database such as its location.
    """

    def __init__(self, database_dir, config_filename="EMConfig.txt", email_dir=None, email_extension=".txt"):
        """
        Initializes the database configuration with the database directory, where the configuration file is located.
        Also it allows to configure a different email directory and email extension.

        :param database_dir: Path of the base directory.
        :param config_filename: Name of the configuration file, defaults to 'EMConfig.txt'.
        :param email_dir: Path of the email directory, defaults to the base directory (database_dir).
        :param email_extension: Extension fo the email files, defaults to '.txt'.
        """

        self.database_dir = database_dir
        self.config_filename = config_filename

        if email_dir:
            self.email_dir = email_dir
        else:
            self.email_dir = database_dir

        self.email_extension = email_extension

    def get_config_path(self):
        """
        Returns the path where the configuration file of the database is located

        :return The config file path
        """
        return os.path.join(self.database_dir, self.config_filename)

    def get_email_path(self, email_id):
        """
        Given an email id it returns its location

        :param email_id:
        :return The email path
        """
        filename = email_id + self.email_extension
        return os.path.join(self.email_dir, filename)


class Database:
    """
    This class is the one in charge of managing the different operations of the database like
    adding and removing emails and folders
    """

    def __init__(self, db_config, seed):
        """
        Initializes the database class with a given seed and the database configuration instance that contains
        the path where the emails (and the config file) are stored

        :param seed: Seed used for email id generation.
        """

        self.db_config = db_config
        self.email_id_seed = seed
        self.folders = {}
        self.emails = LinkedList()

    def add_email(self, email, folder_name=None):
        """
        Add the given email to the database and to the specified folder. If the folder is not found in the Database
        it should raise a MailManagerException. If no folder is provided, the email will be
        added to the outbox folder by default.

        :param email: Email to be added.
        :param folder_name: Name of the older to which the email is added. If not provided, defaults to outbox folder.
        :return: The email id
        """
        pass

    def remove_email(self, email, folder_name=None):
        """
         Remove given email from the given folder. If the folder is not found in the Database
        it should raise a MailManagerException. If no folder_name is provided, the email is removed completely
         from the database.

        :param email: The email to be removed.
        :param folder_name: The name of the folder from which the email should be removed. If no folder name is
         provided, the email is removed from all the folders and from the database.
        :return: The number of folder referencing this email.
        """

        return 0

    def get_email(self, email_id):
        """
        Looks for the given email in the database and returns it

        :param email_id:
        :return: If email id is found in the database it returns it. If it is not found it returns None.
        """

        return None

    def get_email_ids(self, folder_name=None):
        """
        Get email ids from a given folder. If the folder is not found in the Database
        it should raise a MailManagerException.

        :param folder_name:
        :return: Returns the list of email ids of a given folder. If the folder_name parameter is not passed
         it returns the list of emails of the database.
        """
        email_ids = []

        return email_ids

    def create_folder(self, folder_name):
        """
        Adds a folder to the database

        :param folder_name: the name of the new folder
        """
        pass

    def remove_folder(self, folder_name):
        """
        Remove given folder from database. If the folder is not found in the Database
        it should raise a MailManagerException. If some of the emails that belong to that folder doesn't belong
        to any more folders, those emails are removed from the database.

        :param folder_name: the name of the folder to be removed
        """
        pass

    def search(self, text):
        """
        Searches the text into the titles and bodies of the emails, returning the emails that contains said text.

        :param text: the text to be searched
        :return: the list of emails containing that text.
        """
        return []

    def get_folder_names(self):
        """
        Returns a list with the folder names stored in the database.
        :return: a list of folder names.
        """

        return []
