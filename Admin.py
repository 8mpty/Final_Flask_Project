import User


class Admin(User.User):
    count_id = 0

    def __init__(self, username, password, contact_no, sec_ans, ship_addr, email):
        super().__init__(username, password, contact_no, sec_ans, ship_addr, email)
        Admin.count_id += 1
        self.__admin_id = Admin.count_id
        self.__email = email
        self.__ship_addr = ship_addr

    def get_admin_id(self):
        return self.__admin_id

    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email

    def set_admin_id(self, admin_id):
        self.__admin_id = admin_id
