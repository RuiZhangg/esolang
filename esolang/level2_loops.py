import lark
import level1_statements


grammar = level1_statements.grammar + r"""
    %extend start: forloop
        | whileloop

    forloop: "for" NAME "in" range block

    whileloop: "while(" condition ")" block

    range: "range" "(" start ")"
"""
parser = lark.Lark(grammar)


class Interpreter(level1_statements.Interpreter):
    '''
    >>> interpreter = Interpreter()
    >>> interpreter.visit(parser.parse("for i in range(10) {i}"))
    9
    >>> interpreter.visit(parser.parse("a=0; for i in range(10) {a = a + i}"))
    45
    >>> interpreter.visit(parser.parse("a=0; for i in range(10) {a = a + i}; a"))
    45
    >>> interpreter.visit(parser.parse("a=0; for i in range(10) {a = a + i}; i")) # doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
        ...
    ValueError: Variable i undefined
    >>> interpreter.visit(parser.parse("a=5; for i in range(a) {i}"))
    4
    >>> interpreter.visit(parser.parse("a=9; for i in range(a%2) {i*2}"))
    0
    >>> interpreter.visit(parser.parse("a=1; i=0; while(6%a){i=i+a; a=a+1}; i"))
    6
    '''
    def range(self, tree):
        num = self.visit(tree.children[0])
        return range(int(num))

    def forloop(self, tree):
        varname = tree.children[0].value
        xs = self.visit(tree.children[1])
        self.stack.append({})
        if len(xs) <= 0:
            return None
        for x in xs:
            self.stack[-1][varname] = x
            result = self.visit(tree.children[2])
        self.stack.pop()
        return result

    def whileloop(self, tree):
        condition = self.visit(tree.children[0])
        while condition == 0:
            result = self.visit(tree.children[1])
            condition = self.visit(tree.children[0])
        return result