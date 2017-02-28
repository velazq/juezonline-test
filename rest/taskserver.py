from bottle import get, post, request, run

@get('/get_task')
def task_deliver():
    return 'Task'

@post('/post_result')
def parse_result():
    task = request.forms.get('task')
    print task

run(host='192.168.1.130', port=8080, debug=True)
