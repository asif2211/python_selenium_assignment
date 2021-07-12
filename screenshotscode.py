import datetime
import logging
import os


class Screenshots():
    # parent directory path
    def take_screenshot(self, name):

        driver = self.driver
        date = datetime.datetime.now().strftime("%m-%d-%Y")
        microsec = datetime.datetime.now().strftime("%f")
        # creating a new directory if it does not exists before
        if not os.path.exists(
                os.path.dirname(self.basepath + "/../screenshots/%s/%s-screenshots-%s.png" % (date, name, microsec))):
            try:
                os.makedirs(os.path.dirname(
                    self.basepath + "/../screenshots/%s/%s-screenshots-%s.png" % (date, name, microsec)))
            except OSError:
                raise
        if (self.driver.save_screenshot(
                self.basepath + "/../screenshots/%s/%s-screenshots-%s.png" % (date, name, microsec))):
            logging.info(name + " :screenshot taken")
        else:
            logging.info(name + " :unable to save screenshot")
