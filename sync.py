# -*- coding: utf-8 -*-

"""
@author: Glacier

@contact: me@xuluhang.cn

@Created on: 2019/12/3 12:59
"""

import configparser
import os
import subprocess
import sys
import time

import git
from loguru import logger

import util.util as util

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

cf = configparser.ConfigParser()
cf.read(os.path.join(BASE_DIR, 'setting.conf'))
src_git_repo = cf.get('git', 'src_git_repo')
dst_git_repo = cf.get('git', 'dst_git_repo')
src_git = cf.get('git', 'src_git')
dst_git = cf.get('git', 'dst_git')
src_git_repo_name = cf.get('git', 'src_git_repo_name')

GIT_DIR = os.path.join(BASE_DIR, 'git', src_git_repo_name)
BASE_FIL = os.path.basename(os.path.abspath(__file__))

log_file_path = os.path.join(BASE_DIR, 'log', BASE_FIL.replace('.py', '') + 'file_{time}.log')
err_log_file_path = os.path.join(BASE_DIR, 'log', BASE_FIL.replace('.py', '') + 'err.log')
logger.add(sys.stderr, format="{time} {level} {message}", filter="my_module", level="INFO")
logger.add(log_file_path, enqueue=True, rotation="1 days", encoding='utf-8')  # Automatically rotate too big file
logger.add(err_log_file_path, enqueue=True, rotation="500 MB", encoding='utf-8', backtrace=True, diagnose=True,
           level='ERROR')


def run():
    round_num = 0
    while (True):
        try:
            logger.info('[i] ' + str(round_num) + ' Round craw begin!')
            if not os.path.exists(GIT_DIR):
                os.mkdir(GIT_DIR)
                git.Repo.clone_from(url=src_git_repo, to_path=GIT_DIR, depth=1)
                subprocess.call("cd " + GIT_DIR + "&& git remote add " + dst_git + ' ' + dst_git_repo, shell=True)
                subprocess.call("cd " + GIT_DIR + "&& git push " + dst_git + ' master --force', shell=True)
            else:
                subprocess.call("cd " + GIT_DIR + "&& git fetch --all", shell=True)
                subprocess.call("cd " + GIT_DIR + "&& git reset --hard origin/master", shell=True)
                subprocess.call("cd " + GIT_DIR + "&& git push " + dst_git + " master --force", shell=True)

            logger.info('[i] ' + str(round_num) + ' Round syn finished!')
            round_num += 1
            time.sleep(86400)

        except:
            util.wxpush('Crawl', 'Error！', True)
            logger.exception("Main")


if __name__ == "__main__":
    run()
