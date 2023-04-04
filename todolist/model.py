from todolist import db

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable=False)
    complete = db.Column(db.Boolean, default=False)
    date = db.Column(db.Date)
    days = db.Column(db.Text)

    def __repr__(self):
        return f"Todo   ( '{self.id}', '{self.title}','{self.complete}', '{self.date}', '{self.days}')"

db.create_all()