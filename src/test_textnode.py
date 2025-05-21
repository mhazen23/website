import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLDTEXT)
        node2 = TextNode("This is a text node", TextType.BOLDTEXT)
        self.assertEqual(node, node2)

    def test_eq2(self):
        node = TextNode("This is a text node", TextType.BOLDTEXT)
        node2 = TextNode("This is a text node", TextType.ITALICTEXT)
        self.assertNotEqual(node, node2)

    def test_eq3(self):
        node = TextNode("This is a text node", TextType.BOLDTEXT)
        node2 = TextNode("This is a text node", TextType.BOLDTEXT, "https://www.boot.dev")
        self.assertNotEqual(node, node2)

    def test_eq4(self):
        node = TextNode("This is a text node", TextType.BOLDTEXT, "https://www.boot.dev")
        node2 = TextNode("This is a text node", TextType.BOLDTEXT, "https://www.boot.dev")
        self.assertEqual(node, node2)

    def test_eq5(self):
        node = TextNode("This is a text node", TextType.BOLDTEXT, None)
        node2 = TextNode("This is a text node", TextType.BOLDTEXT)
        self.assertEqual(node, node2)

if __name__ == "__main__":
    unittest.main()