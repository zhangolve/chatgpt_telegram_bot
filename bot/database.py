from typing import Optional, Any

import uuid
from datetime import datetime

import config


class Database:
    def __init__(self):
        self.dialog_id = None
        self.dialog_messages = []
        self.user_collection = []
        self.dialog_collection = []


    def check_if_user_exists(self, user_id: int, raise_exception: bool = False):
        return self.find_one(self.user_collection, {"_id": user_id})
        
    def add_new_user(
        self,
        user_id: int,
        chat_id: int,
        username: str = "",
        first_name: str = "",
        last_name: str = "",
    ):
        user_dict = {
            "_id": user_id,
            "chat_id": chat_id,

            "username": username,
            "first_name": first_name,
            "last_name": last_name,

            "last_interaction": datetime.now(),
            "first_seen": datetime.now(),
            
            "current_dialog_id": None,
            "current_chat_mode": "assistant",

            "n_used_tokens": 0
        }

        if not self.check_if_user_exists(user_id):
            self.user_collection.append(user_dict)

    def compare_dicts(self, dict_a, dict_b):
        for key in dict_a:
            if key not in dict_b or dict_a[key] != dict_b[key]:
                return False
        return True

    def update_database(self, arr, condition, updated):
        for elem in arr:
            if self.compare_dicts(condition, elem):
                elem.update(updated)
                return arr
        return arr

    def find_one(self, arr, condition):
        for elem in arr:
            if self.compare_dicts(condition, elem):
                return elem
        return None
        
    def start_new_dialog(self, user_id: int):
        self.check_if_user_exists(user_id, raise_exception=True)

        dialog_id = str(uuid.uuid4())
        dialog_dict = {
            "_id": dialog_id,
            "user_id": user_id,
            "chat_mode": self.get_user_attribute(user_id, "current_chat_mode"),
            "start_time": datetime.now(),
            "messages": []
        }

        # add new dialog
        self.dialog_collection.append(dialog_dict)

        # update user's current dialog
        self.update_database(self.user_collection,{"_id": user_id}, {"current_dialog_id": dialog_id} )
        self.dialog_id = dialog_id
        return dialog_id

    def get_user_attribute(self, user_id: int, key: str):
        self.check_if_user_exists(user_id, raise_exception=True)
        user_dict = self.find_one(self.user_collection, {"_id": user_id})
        if key not in user_dict:
            raise ValueError(f"User {user_id} does not have a value for {key}")
        return user_dict[key]

    def set_user_attribute(self, user_id: int, key: str, value: Any):
        self.check_if_user_exists(user_id, raise_exception=True)
        self.update_database(self.user_collection, {"_id": user_id}, {key: value})

    def get_dialog_messages(self, user_id: int, dialog_id: Optional[str] = None):
        if dialog_id is None:
            dialog_id = self.get_user_attribute(user_id, "current_dialog_id")
        dialog_dict = self.find_one(self.dialog_collection, {"_id": dialog_id, "user_id": user_id})               
        return dialog_dict["messages"]


    def set_dialog_messages(self, user_id: int, dialog_messages: list, dialog_id: Optional[str] = None):
        self.check_if_user_exists(user_id, raise_exception=True)

        if dialog_id is None:
            dialog_id = self.get_user_attribute(user_id, "current_dialog_id")
        
        self.update_database(self.dialog_collection,
            {"_id": dialog_id, "user_id": user_id},
            {"messages": dialog_messages}
        )