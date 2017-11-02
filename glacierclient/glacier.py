# -*- coding: utf-8 -*-
"""
aws glacier client
"""
import sys
import subprocess
from glacierclient import logger

class Glacier(object):
    """
    AWS Glacier Client Class
    """

    def __init__(self):
        self.region = 'ap-northeast-1'
        self.vault_name = 'test_vault'

    @staticmethod
    def _run_cmd(cmd):
        proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout_data, stderr_data = proc.communicate()

        if stderr_data:
            sys.exit(stderr_data)

        return stdout_data

    def create_vault(self, account_id='-'):
        """
        create vault
        """
        logger.debug('--- create vault start ---')
        cmd = 'aws glacier create-vault --vault-name %s --account-id %s'
        cmd = cmd % (self.vault_name, account_id)
        self._run_cmd(cmd)
        logger.debug('--- create vault  end  ---')
