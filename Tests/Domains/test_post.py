import __init__
import unittest
import sys
from datetime import datetime

from Domains.Posts import PostBuilder, PostIDBuilder

class test_post(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = "test"
        print(sys._getframe(0).f_code.co_name, f"(test_post)")

    @classmethod
    def tearDownClass(cls):
        "Hook method for deconstructing the class fixture after running all tests in the class."
        print(sys._getframe(0).f_code.co_name)

    def setUp(self):
        "Hook method for setting up the test fixture before exercising it."
        print("\t", sys._getframe(0).f_code.co_name)

    def tearDown(self):
        "Hook method for deconstructing the test fixture after testing it."
        print("\t", sys._getframe(0).f_code.co_name)

    
    def test_post_builder(self):
        "Hook method for deconstructing the test fixture after testing it."
        print("\t\t", sys._getframe(0).f_code.co_name)

        post_id =  PostIDBuilder().set_uuid().set_seq(1).build()

        post =  PostBuilder().set_id(post_id) \
            .set_title("Test Title") \
            .set_content("Test Content") \
            .set_create_time(datetime.now()) \
            .build()

        self.assertEqual(post.id, post_id)
        self.assertEqual(post.title, "Test Title")
        self.assertEqual(post.content, "Test Content")
        self.assertIsInstance(post.create_time, datetime)

    def test_post_builder_default_create_time(self):
        "Hook method for deconstructing the test fixture after testing it."
        print("\t\t", sys._getframe(0).f_code.co_name)

        post_id = PostIDBuilder().set_uuid().set_seq(1).build()

        post = PostBuilder().set_id(post_id) \
            .set_title("Test Title") \
            .set_content("Test Content") \
            .set_create_time() \
            .build()

        self.assertEqual(post.id, post_id)
        self.assertEqual(post.title, "Test Title")
        self.assertEqual(post.content, "Test Content")
        self.assertIsInstance(post.create_time, datetime)


if __name__ == '__main__':
    unittest.main()
