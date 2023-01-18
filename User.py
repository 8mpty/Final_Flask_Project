class User:
    # count_id = 0

    def __init__(self, user_id, username, password, contact_no, sec_ops, sec_ans, ship_addr, prof_img):
        # User.count_id += 1
        self.__user_id = user_id
        self.__username = username
        self.__password = password
        # self.__con_password = con_password
        self.__contact_no = contact_no
        self.__sec_ops = sec_ops
        self.__sec_ans = sec_ans
        self.__ship_addr = ship_addr
        self.__prof_img = prof_img

    def get_user_id(self):
        return self.__user_id

    def get_username(self):
        return self.__username

    def get_password(self):
        return self.__password

    def get_contact_no(self):
        return self.__contact_no

    def get_ship_addr(self):
        return self.__ship_addr

    def get_sec_ops(self):
        return self.__sec_ops

    def get_sec_ans(self):
        return self.__sec_ans

    def get_prof_img(self):
        return self.__prof_img


    def set_user_id(self, user_id):
        self.__user_id = user_id

    def set_username(self, username):
        self.__username = username

    def set_password(self, password):
        self.__password = password

    def set_contact_no(self, contact_no):
        self.__contact_no = contact_no

    def set_ship_addr(self, ship_addr):
        self.__ship_addr = ship_addr

    def set_sec_ops(self, sec_ops):
        self.__sec_ops = sec_ops

    def set_sec_ans(self, sec_ans):
        self.__sec_ans = sec_ans

    def set_prof_img(self, prof_img):
        self.__prof_img = prof_img
