import os
import logging
import ftplib
import shutil


logging.basicConfig(level=logging.DEBUG,
                    filename='logs.log',
                    filemode='w',
                    format = '%(asctime)s - %(levelname)s - %(message)s')

path = 'local_path'

ftp_add = 'ftp_address'
ftp_log = 'ftp_login'
ftp_pass = 'ftp_pass'

ftp_path = 'ftp_path'

for element in os.listdir(path):
    if element.endswith('.CSV'):
        ftp = ftplib.FTP(ftp_add, ftp_log, ftp_pass)
        ftp.cwd(ftp_path)
        filename = "%s" % element
        with open("%s" %e, 'rb') as f:
                ftp.storbinary('STOR ' + filename, f)
                logging.info("Le fichier " + filename + " c'est téléchargé correctement")
        origin = r"origin_path/%s" % element
        target = r"target_path/%s" % element
        #shutil.move(origin, target)
    else:
        logging.info('Aucun fichier à téléchargé')
