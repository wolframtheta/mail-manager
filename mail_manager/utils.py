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

    f = open(os.path.join(email_dir, str(email_id) + email_extension),'r')
    email = Email(email_id=email_id)
    line = f.readline()
    start_body = False
    while line:
        if start_body:
            if not email.body:
                email.body = line
            else:
                email.body += line
        if line.startswith('Date: '):
           email.date = line[6:len(line)].strip('\n')
        elif line.startswith('From: '):
           email.sender = line[6:len(line)].strip('\n')
        elif line.startswith('To: '):
            email.receiver = line[4:len(line)].strip('\n')
        elif line.startswith('Subject: '):
            email.subject = line[9:len(line)].strip('\n')
        elif line.startswith('\n'):
            start_body = True
        line = f.readline()

    return email

def write_email(email, db, db_config=None):
    """
    This function writes the email text file corresponding to a given email object.

    :param email: email
    :param db: Database
    :param db_config: Database Configuration
    """
    f = open(os.path.join(db_config.email_dir, str(email.id) + db_config.email_extension), 'a')
    f.write(str(email))
    f.close()

def delete_email(email, db, db_config=None):
    """
    Removes the email text file corresponding to a given email object (Optional, be careful)

    :param email: email
    :param db: Database
    :param db_config: Database Configuration
    """

    if db_config is None:
        db_config = db.db_config
    path = os.path.join(db_config.email_dir, email + db_config.email_extension)
    if os.path.exists(path):
        os.remove(path)
    else:
        raise MailManagerException("There is no file with that id")


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
    with open(db_config.get_config_path(), 'r') as f:
        try:
            line = f.readline()
            while not line.startswith('Message-ID: '):
                line = f.readline()
            db = Database(db_config, int(line[12:]))

            while not line.startswith('Folders:'):
                line = f.readline()
            line = f.readline()

            inside_folder = False
            while line:
                if line == "\n":
                    inside_folder = False
                if inside_folder:
                    email = load_email(db_config.email_dir, line.strip(), db_config.email_extension)
                    db.add_email(email, folder)
                if line.endswith("Messages:\n"):
                    folder = db.create_folder(line[0:len(line) - 10].strip())
                    inside_folder = True



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
        f.write("Message-ID: " + str(db.email_id_seed) + '\n\n')
        f.write("Folders:\n")
        for k in db.get_folder_names():
            f.write(k + "\n")
        for k in db.get_folder_names():
            f.write('\n')
            f.write(k + " Messages:\n")
            for e in db.get_email_ids(k):
                f.write(e + '\n')
        f.write("\nEnd\n")
        f.close()
