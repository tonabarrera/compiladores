from analyzer.analizer import Analyzer
def main():
    analyzer = Analyzer('a|b')
    analyzer.analyze()
    analyzer.postorden(analyzer.tree)

main()
