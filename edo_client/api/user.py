# -*- coding: utf-8 -*-
from .base import BaseApi

class UserApi(BaseApi):
   
    def principal_info(self, user_id):
        return self._get('/api_get_principal_info', user_id=user_id)

    def has_user(self, username):
        return self._get('/api_has_user', username=username)

    def list_user_groups(self, key):
        return self._get('/api_list_user_groups', key=key)

    def list_principal_info(self, users):
        return self._get('/api_list_principal_info', users=users)

    def get_online_users_list(self, account):
        return self._get('/api_get_online_users_list', account=account)



