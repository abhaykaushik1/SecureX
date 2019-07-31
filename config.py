from datetime import datetime

import location


EMAIL_ADDRESS = "ByteMeTonight@gmail.com"
PASSWORD = "ByteMepls"


def message(name: str):
    msg = "Login alert for {}.\nThe following email was sent " \
              "because a login was detected on your device on {} at {}. " \
              "Your files are now unlocked and accessible from the " \
              "location it was logged in on.\n\nIf this was you, disregard " \
              "this email. However, if this was not, consider " \
              "taking a look at your security " \
              "settings. It was " \
          "accessed at {}".format(name, datetime.today().strftime('%Y-%m-%d'),
                                    datetime.today().strftime('%H:%M:%S'),
                                  location.get_location())
    return msg
