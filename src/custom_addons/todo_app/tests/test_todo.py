from odoo.tests.common import TransactionCase
from odoo.exceptions import AccessError


class TestTodo(TransactionCase):
    def test_create(self):
        """Create a simple Todo"""

        todo = self.env['todo.task']
        task = todo.create({'name': 'Test Task'})
        self.assertEqual(task.is_done, False)

    def test_clear_done(self):
        """Clear Done sets Todo to not active"""

        todo = self.env['todo.task']
        task = todo.create({'name': 'Test Task'})
        task.do_clear_done()
        self.assertFalse(task.active)

    def setUp(self, *args, **kwargs):
        result = super(TestTodo, self).setUp(*args, **kwargs)

        user_demo = self.env.ref('base.user_demo')
        self.env = self.env(user=user_demo)
        return result

    def test_record_rule(self):
        """Test per user record rules"""

        todo = self.env['todo.task']
        task = todo.sudo().create({'name': 'Admin Task'})
        with self.assertRaises(AccessError):
            todo.browse([task.id]).name
