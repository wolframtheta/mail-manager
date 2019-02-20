import logging
import datetime

from mail_manager import utils
from mail_manager.database import Database, DatabaseConfiguration
from mail_manager.email import Email
from mail_manager.exceptions import MailManagerException


def read_int_option(message, start, end):
    """
    Shows an input message and reads the option of the user

    :param message: input message
    :param start: minimum value the user can enter
    :param end: maximum value the user can enter
    :return: the option chosen by the user
    """

    option = input(message)
    try:
        option = int(option)

    except ValueError:
        option = None

    else:
        if option < start or option > end:
            option = None

    return option


def choose_email(email_ids):
    """
    Shows the emails contained in the database and asks the user to choose one

    :param email_ids: list of email ids
    :return: the email id chosen by the user
    """

    email_id = None
    if not email_ids:
        print("There are no emails in the database yet.")

    else:
        print("The database contains the following emails:")
        for idx, email_id in enumerate(email_ids):
            print("  {}. {}".format(idx + 1, email_id))

        email_id = None
        cancel = False
        while not cancel and not email_id:
            option = read_int_option("Choose an email: (0 to cancel)\n", 0, len(email_ids) + 1)
            if option:
                email_id = email_ids[option - 1]

            elif option == 0:
                cancel = True
                print("Operation cancelled!")

            else:
                print("Invalid option, try again.")

    return email_id


def choose_folder(folder_names):
    """
    Shows the folders contained in the database and asks the user to choose one

    :param folder_names: list of folder
    :return: the name of the folder chosen by the user
    """

    folder_name = None
    if not folder_names:
        print("There are no folders in the database yet.")

    else:
        print("The database contains the following folders:")
        for idx, name in enumerate(folder_names):
            print("  {}. {}".format(idx + 1, name))

        cancel = False
        while not cancel and not folder_name:
            option = read_int_option("Choose a folder: (0 to cancel)\n", 0, len(folder_names) + 1)
            if option:
                folder_name = folder_names[option - 1]

            elif option == 0:
                cancel = True
                print("Operation cancelled!")

            else:
                print("Invalid option, try again.")

    return folder_name


def list_emails(db):
    """
    Shows the list of emails contained in the Database

    :param db: An email database.
    """
    pass


def show_email(db):
    """
    This function calls to the choose_email function and it shows the content of the given email chosen
    by the user in the Database

    :param db: An email database.
    """
    pass


def create_email(db):
    """
    Asks for the user to fill the fields of an email and creates it in the database. It also creates
    its corresponding text file

    :param db: An email database.
    """
    pass


def delete_email(db):
    """
    This functions calls to the choose_email function and it removes the given email chosen
    by the user

    :param db: An email database.
    """
    pass

def show_folders(db):
    """
    This function calls to the choose_folder function and shows all the emails contained in the folder chosen
    by the user.

    :param db: An email database.
    """
    pass


def create_folder(db):
    """
    Asks the user to introduce the folder name and then it creates it in the Database

    :param db: An email database.
    """
    pass


def delete_folder(db):
    """
    This functions calls to the choose_folder function and deletes the chosen folder by the user

    :param db: An email database.
    """
    pass


def add_email_to_folder(db):
    """
    This functions first calls to the choose_email function. After that, it calls to the choose_folder function and
    adds the chosen email to the chosen folder.

    :param db: An email database.
    """
    pass


def remove_email_from_folder(db):
    """
    This function first calls to the choose_folder function. After that, it shows all the emails belonging to that
    folder and asks the user to chose which one wants to remove. Then, the chosen mail is removed

    :param db: An email database.
    """
    pass


def search(db):
    """
    Ask the user for the text to be searched and searches the text into the database, showing the emails
    that contains said text.

    :param db: An email database.
    """
    pass


def show_menu(db):
    """
    Shows all the different menu options. This function also calls to the read_int_option function and calls to
    the chosen option

    :param db: An email database.
    """
    options = [
        {"message": "Exit", "function": None},
        {"message": "List emails", "function": list_emails},
        {"message": "Show email", "function": show_email},
        {"message": "Create email", "function": create_email},
        {"message": "Delete email", "function": delete_email},
        {"message": "Show folders and folder emails", "function": show_folders},
        {"message": "Create folder", "function": create_folder},
        {"message": "Delete folder", "function": delete_folder},
        {"message": "Add email to folder", "function": add_email_to_folder},
        {"message": "Remove email from folder", "function": remove_email_from_folder},
        {"message": "Search", "function": search},
    ]

    exit_program = False
    while not exit_program:

        print("\nMain menu:")
        for idx, option in enumerate(options[1:]):
            print("  {}.- {}".format(idx+1, option["message"]))

        print("  {}.- {}".format(0, options[0]["message"]))

        option = read_int_option("What do you want to do? Choose an option:\n", 0, len(options))
        if option is None:
            print("Invalid option, try again.")

        elif option == 0:
            exit_program = True

        else:
            option_function = options[option]["function"]
            try:
                option_function(db)

            except MailManagerException as mme:
                print("Error: {}", mme)

            except Exception as e:
                print("Unexpected error: {}", e)
                raise

            input("\nPress Enter to continue...")


def main():
    """
    MAIN function of the email manager.
    """

    # We create a Database Configuration object with the name of the folder where our emails and configuration files are
    # going to be stored. In our case all of them are placed inside "emailDB".
    db_config = DatabaseConfiguration("emailDB")

    # This function reads the EMConfig file and returns a Database object with all the information about
    # the state of the email manager.
    db = utils.load_database(db_config)

    # Calls the menu
    show_menu(db)

    # When the user decides to exit the program it has to save all the information related to the changes done in the
    # email manager. So it writes a new EMConfig file with the new state of folders, emails and Message-Id.
    utils.write_database(db)


if __name__ == '__main__':
    main()
