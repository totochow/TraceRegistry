# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 13:41:52 2021

@author: tchow
"""
import paramiko
import os
import shutil
import sys
sys.path.insert(1, 'M:\\TC\\Freshline\\Control Files\\')
import my_config as my_c


def get_ssh(xhost, xport, xusername, xpassword):
    ssh_client=paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(xhost, xport, xusername, xpassword)
    return ssh_client

def upload_file (xlocalpath, xfilepath):
    sftp.put(xlocalpath ,xfilepath)
    
files = os.listdir(my_c.tr_localpath)
local_paths = [my_c.tr_localpath + s for s in os.listdir(my_c.tr_localpath)]
files_paths = [my_c.tr_filepath + t for t in os.listdir(my_c.tr_localpath)]
archive_paths = [my_c.tr_archivepath + u for u in os.listdir(my_c.tr_localpath)]

ssh_client = get_ssh(my_c.tr_host, my_c.tr_port, my_c.tr_username, my_c.tr_password)
sftp = ssh_client.open_sftp()



for lps,fps,aps,fs in zip(local_paths, files_paths, my_c.tr_archivepath, files):
    upload_file(lps,fps)
    shutil.move(lps, my_c.tr_archivepath)
    
ssh_client.close()
sftp.close()