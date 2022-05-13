

class Game():

    def __init__(self):
        self._greeting=None
        self._help_msg=None
        self._win_msg=None
        self._loose_msg=None
        self._data_path=None


    @property
    def greeting(self):
        return self._greeting
    @property
    def help_msg(self):
        return self._help_msg
    @property
    def win_msg(self):
        return self._win_msg
    @property
    def loose_msg(self):
        return self._loose_msg
    @property
    def data_path(self):
        return self._data_path


    @greeting.setter
    def greeting (self,new_greeting):
        self._greeting=new_greeting
    @help_msg.setter
    def help_msg(self,new_help_msg):
        self._help_msg=new_help_msg
    @win_msg.setter
    def win_msg(self,new_win_msg):
        self._win_msg=new_win_msg
    @loose_msg.setter
    def loose_msg(self,new_loose_msg):
        self._loose_msg=new_loose_msg
    @data_path.setter
    def data_path(self,new_data_path):
        self._data_path=new_data_path





