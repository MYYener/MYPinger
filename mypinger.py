# Module to ping hostnames and IP addresses
# Not PEP8 compliant
import subprocess

__author__  =   'MUYE'
__company__ =   ''
__version__ =   '01.00'
__script__  =   'MYPinger'


def ping(host, platform):
    if platform in ['Windows', 'windows', 'win']:
        # print('INFO: ' + __script__ + ': Windows platform chosen.')
        # print('INFO: ' + __script__ + ': Pinging ' + host + '.')
        process = subprocess.Popen(["ping", "-n", "3", host], stdout=subprocess.PIPE)
        process_output = process.communicate()[0]
        if process.returncode == 0:
            # print('INFO: ' + __script__ + ': Pinging successful.')
            status = 'OK'
            ping.returncode = 1
        else:
            # rint('INFO: ' + __script__ + ': Pinging not successful.')
            status = 'NOK'
            ping.returncode = 0

    elif platform in ['Linux', 'linux', 'lin', 'CentOS', 'centos']:
        # print('INFO: ' + __script__ + ': Linux/CentOS platform chosen.')
        # print('INFO: ' + __script__ + ': Pinging ' + host + '.')
        process = subprocess.Popen(["ping", "-q", "-c", "3", host], stdout=subprocess.PIPE)
        process_output = process.communicate()[0]
        if process.returncode == 0:
            # print('INFO: ' + __script__ + ': Pinging successful.')
            status = 'OK'
            ping.returncode = 1
        else:
            # print('INFO: ' + __script__ + ': Pinging not successful.')
            status = 'NOK'
            ping.returncode = 0

    else:
        raise ValueError('Incorrect platform selection.')







