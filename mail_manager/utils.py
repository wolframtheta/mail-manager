import os
import re
import logging

from .database import Database, DatabaseConfiguration
from .email import Email
from .exceptions import MailManagerException


def load_email(email_dir, email_id, email_extension='.txt'):
    """
    This function loads the corresponding email object from an email text file.

    :param email_dir: path of the email
    :param email_id:
    :param email_extension:
    :return: it returns an email object
    """
    return None

def write_email(email, db, db_config=None):
    """
    This function writes the email text file corresponding to a given email object.

    :param email: email
    :param db: Database
    :param db_config: Database Configuration
    """
    pass

def delete_email(email, db, db_config=None):
    """
    Removes the email text file corresponding to a given email object (Optional, be careful)

    :param email: email
    :param db: Database
    :param db_config: Database Configuration
    """
    pass


def load_database(db_config):
    """
    Loads database using the information stored in the DatabaseConfiguration object.
    This function creates a Database object, reads the "EMConfig.txt" file and fills the Database object with the
    information found there (folders, emails etc...). For that purpose you will need to make use of the load_email
    function.

    It raises a MailManagerException if it finds an invalid configuration format.

    This is going to be a long function. Please, try to use as many functions as you can to encapsulate your code in a
    meaningul way.

    :param db_config:
    :return: Database object
    """
    return Database(db_config,0)

def write_database(db, db_config=None):
    """
    Writes the corresponding Email Config File (text file) from a given Database

    :param db: Database
    :param db_config: Database Configuration
    """
    pass
