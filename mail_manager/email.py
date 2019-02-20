

class Email:
    """
    The email class contains all the information related to an email like the subject, the sender, etc.
    """

    template = """Date: {0.date}
From: {0.sender}
To: {0.receiver}
Message-ID: {0.id}
Subject: {0.subject}

{0.body}"""

    def __init__(self, email_id=None, sender=None, receiver=None, subject=None, date=None, body=None):
        """
        Initializes an email.

        :param email_id: Unique identifier of the email.
        :param sender: Email sender.
        :param receiver: Email receiver.
        :param subject: Subject of the email.
        :param date: Date of creation of the email.
        :param body: Body content of the email.
        """

        self.id = email_id
        self.sender = sender
        self.receiver = receiver
        self.subject = subject
        self.date = date
        self.body = body
        self.references = 0

    def __str__(self):
        """
        This function is called when the menu wants to show the content of the email to the user.

        :return: a string in the email template format
        """
        return Email.template.format(self)







