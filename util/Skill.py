class Skill:
    def __init__(self, sk_id, name, desc, src, on_enable):
        self.on_enable = on_enable
        self.name = name
        self.desc = desc
        self.src = src
        self.id = sk_id

    def activate(self, fight_data, atk):
        self.on_enable(fight_data, atk)
