from flask import request, jsonify
from flask import Blueprint

from app.models.model_task import TaskModel, TaskSchema, db

task_bp = Blueprint('tasks', __name__)
task_schema = TaskSchema()
tasks_schema = TaskSchema(many=True)


@task_bp.route('/')
def index():
    return {'message': 'success'}


@task_bp.route('/api/v1/tasks', methods=['POST'])
def create_task():
    data = request.json
    title = data['title']
    description = data['description']
    start_date = data['start_date']
    due_date = data['due_date']
    priority = data['priority']

    new_task = TaskModel(title=title, description=description, start_date=start_date, due_date=due_date,
                         priority=priority)

    db.session.add(new_task)
    db.session.commit()
    return task_schema.jsonify(new_task)


@task_bp.route('/api/v1/tasks', methods=['GET'])
def get_tasks():
    tasks = TaskModel.query.all()
    result = tasks_schema.dump(tasks)
    return jsonify(result)


@task_bp.route('/api/v1/tasks/<id>', methods=['GET'])
def get_task(id):
    task = TaskModel.query.get(id)
    return task_schema.jsonify(task)


@task_bp.route('/api/v1/tasks/<id>', methods=['PUT'])
def update_task(id):
    task = TaskModel.query.get(id)

    task.title = request.json['title']
    task.description = request.json['description']
    task.start_date = request.json['start_date']
    task.due_date = request.json['due_date']
    task.priority = request.json['priority']
    task.assignee = request.json['assignee']

    db.session.commit()
    return task_schema.jsonify(task)


@task_bp.route('/api/v1/tasks/<id>', methods=['DELETE'])
def delete_task(id):
    task = TaskModel.query.get(id)
    db.session.delete(task)
    db.session.commit()
    return task_schema.jsonify(task)
