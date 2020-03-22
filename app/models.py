from app import db


class Entity(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(32))
	content = db.Column(db.String(128))

	def __repr__(self):
		return f'entity: {self.name}'
