class Info:
    info_id = 1

    def __init__ (self, num):
        self.num = num
        self.info_id = Info.info_id
        Info.info_id += 1

    age = [
        info_id()
    ]