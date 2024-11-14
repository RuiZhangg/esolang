import readline
import level0_arithmetic
import level1_statements
import level2_loops
import level3_functions


def run_repl(lang = level3_functions):
    parser = lang.parser
    interpreter = lang.Interpreter()
    while True:
        try:
            cmd = input('esolang> ')
            tree = parser.parse(cmd)
            result = interpreter.visit(tree)
            if result is not None:
                print(result)
        except EOFError:
            break
        except Exception as e:
            print(e)


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--level', default=3, type=int)
    args = parser.parse_args()

    if args.level == 0:
        run_repl(level0_arithmetic)
    if args.level == 1:
        run_repl(level1_statements)
    if args.level == 2:
        run_repl(level2_loops)
    if args.level == 3:
        run_repl(level3_functions)
