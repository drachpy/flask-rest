from settings import db


class Crud():
    def add(self, data=None):
        if data:
            for key, value in data.items():
                setattr(self, key, value)
        db.session.add(self)
        db.session.commit()
        return self

    def update(self, data=None):
        if data:
            for key, value in data.items():
                setattr(self, key, value)
        db.session.commit()
        return self

    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return self
