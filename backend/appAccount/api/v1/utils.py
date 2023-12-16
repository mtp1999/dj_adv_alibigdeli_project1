import threading


class SendEmailThread(threading.Thread):
    def __init__(self, email_object):
        super().__init__()
        self.email_object = email_object

    def run(self):
        self.email_object.send()
