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


def download_file1():
    downloaded_bytes = 0
    chunk_size = 1024 * 8

    url = '/'.join([server, file_name])

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
                file_size = 100 * 1024 * 1024

            with open(file_name, 'wb') as fd:
                for chunk in response.iter_content(chunk_size=chunk_size):
                    # Filter out keep-alive new chunks
                    if chunk:
                        fd.write(chunk)
                        downloaded_bytes += len(chunk)

    except requests.exceptions.ConnectionError:
        print('Cannot download file from server: %s, connection error' % server)

    except requests.exceptions.MissingSchema:
        print('Cannot download file from server: %s, wrong URL' % server)

    except socket.error:
        print('Cannot download file from server: %s, connection error' % server)


def download_file2():
    try:
        subprocess.check_call(['wget', '/'.join([server, file_name])], shell=False, stdout=DEVNULL, stderr=DEVNULL)

    except subprocess.CalledProcessError, e:
        print('Download file, error: %s' % e.__str__())


def remove_file():
    try:
        subprocess.check_call('rm -f ' + file_name, shell=True)

    except subprocess.CalledProcessError:
        print('Failed to clean existing file copy')


if __name__ == '__main__':
    server = 'http://developer.toradex.com/files/toradex-dev/uploads/media/Colibri/Linux/Images/'
    file_name = 'Apalis_T30_LinuxImageV2.5Beta2_20151106.tar.bz2'

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