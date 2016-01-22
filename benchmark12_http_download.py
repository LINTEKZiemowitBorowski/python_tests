#!/usr/bin/python

import subprocess
import socket
import time
import requests

try:
    # for python 3
    from subprocess import DEVNULL
except ImportError:
    # for python 2
    import os

    DEVNULL = open(os.devnull, 'wb')


SERVER = 'http://developer.toradex.com/files/toradex-dev/uploads/media/Colibri/Linux/Images/'
FILE_NAME = 'Apalis_T30_LinuxImageV2.5Beta3_20151215.tar.bz2'


def download_file1():
    url = '/'.join([SERVER, FILE_NAME])

    print('Uploading file: %s' % url)

    try:
        response = requests.get(url, verify=False)

        print ('Got response: %s' % str(response))

        if response.status_code is 200:
            try:
                file_size = int(response.headers['content-length'])
                print("File size: %d" % file_size)

            except KeyError:
                print('Cannot obtain file size, assuming default size\n')

            with open(FILE_NAME, 'wb') as fd:
                for data in response.iter_content():
                    if data:
                        fd.write(data)

    except requests.exceptions.ConnectionError:
        print('Cannot download file: %s, connection error' % SERVER)

    except requests.exceptions.MissingSchema:
        print('Cannot download file: %s, wrong URL' % SERVER)

    except socket.error:
        print('Cannot download file: %s, system error' % SERVER)


def download_file2():
    try:
        subprocess.check_call(['wget', '/'.join([SERVER, FILE_NAME])], shell=False, stdout=DEVNULL, stderr=DEVNULL)

    except subprocess.CalledProcessError, e:
        print('Download file, error: %s' % e.__str__())


def remove_file():
    try:
        subprocess.check_call('rm -f ' + FILE_NAME, shell=True)

    except subprocess.CalledProcessError:
        print('Failed to clean existing file copy')


if __name__ == '__main__':
    print ("Running: %s" % os.path.basename(__file__))

    # Remove old downloaded file
    remove_file()

    start_time1 = time.time()

    # Legacy method
    download_file1()

    legacy_download_time = time.time()

    # Remove old downloaded file
    remove_file()

    start_time2 = time.time()

    # WGET method
    download_file2()

    wget_download_time = time.time()

    print ("Download time using legacy method: %f" % (legacy_download_time - start_time1))
    print ("Download time using wget method: %f" % (wget_download_time - start_time2))