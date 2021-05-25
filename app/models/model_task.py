from . import db, ma


class TaskModel(db.Model):
    __tablename__ = 'tasks'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50)) 
    description = db.Column(db.String(50)) 
    start_date = db.Column(db.DateTime())
    due_date = db.Column(db.DateTime())
    priority = db.Column(db.String(50))
    assignee = db.Column(db.Integer, db.ForeignKey('Users.id'))


class TaskSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'description', 'start_date', 'due_date', 'priority')


