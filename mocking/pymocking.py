class TestFoo(unittest.TestCase):
    def test_foo(self):
        with patch('my_module.db_write'):
            x = my_module.foo()
            self.assertEquals(x, 16)
        y = my_module.foo()
        self.assertEquals(y, 16)

