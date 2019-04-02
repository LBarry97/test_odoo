from argparse import ArgumentParser
from todo_appi import TodoAPI


parser = ArgumentParser()
parser.add_argument('command', choices=['list', 'add', 'del', 'done'])
parser.add_argument('text', nargs='?') # optional arg
args = parser.parse_args()

srv, port, db = 'localhost', 8069, 'odootestdb'
user, pwd = 'admin', 'admin'
api = TodoAPI(srv, port, db, user, pwd)


if args.command == 'list':
    todos = api.read()
    for todo in todos:
        todo['done'] = 'X' if todo['is_done'] else ' '
        print('%(id)d [%(done)s] %(name)s' % todo)

if args.command == 'add':
    todo_id = api.write(args.text)
    print('Todo %d created.' % todo_id)

if args.command == 'del':
    api.unlink(int(args.text))
    print('Todo %s deleted.' % args.text)

if args.command == 'done':
    todo_id = api.done(int(args.text))
    if todo_id:
        print('Todo %d finished.' % todo_id)
