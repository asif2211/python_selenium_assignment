import datetime
import logging
import os


class Logfile():
    # create log folder and log file

    def create_log_file(self):

        logging.basicConfig(filename=self.basepath + " /../logs/%s.log" % (datetime.datetime.now().strftime("%m-%d-%Y")),
                            filemode="w", level=logging.INFO,
                            format="%(levelname)s: %(message)s (Time: %(asctime)s)")