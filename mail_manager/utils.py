import os
import re
import logging

from .database import Database, DatabaseConfiguration
from .email_ import Email
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
    return
    with open(db_config.get_config_path(), 'r') as f:
        try:
            line = f.readline()
            while not line.startswith('Message_Id: '):
                line = f.readline()
            db = Database(db_config, int(line[12:]))

            while not line.startswith('Folders: '):
                line = f.readline()
            line = f.readline()
            while not line.endswith(":") or line.strip() == 'End':
                if not line.strip():
                    db.create_folder(line.strip())
                line = f.readline()

            while not line.strip() == "End":
                folder = line[:-10]
                while not line.endswith(":") or line.strip() == 'End':
                    if not line.strip():
                        email = load_email(db_config.email_dir, line.strip(), db_config.email_extension)
                        db.add_email(email, folder)
                    line = f.readline()
            f.close()
            return db
        except:
            raise MailManagerException("Invalid configuration file")


def write_database(db, db_config=None):
    """
    Writes the corresponding Email Config File (text file) from a given Database

    :param db: Database
    :param db_config: Database Configuration
    """
    if db_config == None:
        db_config = db.db_config                  #si no et donen la dada, agafa la de la base de dades per defecte

    with open(db_config.get_config_path(), 'w') as f:
        f.write("Message-Id: " + db.email_id_seed + '\n\n')
        f.write("Folders: \n")
        for k in db.get_folder_names():
            f.write(k + "\n")
        for k in db.get_folder_names():
            f.write(k + " Mensajes: \n")
            for e in db.get_email_ids(k):
                f.write(e + '\n')
            f.write("\n")
        f.write("End")
        f.close()
