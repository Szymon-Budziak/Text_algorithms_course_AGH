file = open("1997_714_head.txt", encoding="utf8")
e = file.read()


class SuffixTreeNode:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.children = dict()


class SuffixTree:
    def __init__(self, text):
        self.root = SuffixTreeNode(0, len(text) - 1)
        self.text = text
        for i in range(len(text) - 1):
            suffix = text[i:]
            head, depth = self.find(suffix)
            self.graft(head, depth, i)

    def find(self, text, depth=0, node=None):
        if node is None:
            node = self.root
        if text == "\n":
            return node, depth
        next_node = node.children.get(text[0])
        if next_node is None:
            return node, depth

        next_node_text_len = next_node.end - next_node.start + 1
        for i in range(1, next_node_text_len):
            if self.text[next_node.start + i] != text[i]:
                stop_node = SuffixTreeNode(next_node.start, next_node.start + i - 1)
                next_node.start += i
                node.children[self.text[stop_node.start]] = stop_node
                stop_node.children[self.text[next_node.start]] = next_node
                return stop_node, depth + i
        return self.find(text[next_node_text_len:], next_node_text_len + depth, next_node)

    def graft(self, head, depth, i):
        new_node = SuffixTreeNode(depth + i, len(self.text) - 1)
        head.children[self.text[new_node.start]] = new_node

    def pattern_search(self, pattern, node=None):
        if len(pattern) == 0:
            return True
        if node is None:
            node = self.root
        next_node = node.children.get(pattern[0])
        if next_node is None:
            return False

        next_node_text_len = next_node.end - next_node.start + 1
        for i in range(1, next_node_text_len):
            if i == len(pattern):
                return True
            elif self.text[next_node.start + i] != pattern[i]:
                return False
        return self.pattern_search(pattern[next_node_text_len:], next_node)


invalid_patterns = ["fsadfasbdasfhbgsddg"]
errors = 0
suffix_tree = SuffixTree(e)
for inv_pat in invalid_patterns:
    if suffix_tree.pattern_search(inv_pat):
        errors += 1
print(f"Number of errors in Suffix Tree search is {errors}.")
