import os, glob
from collections import namedtuple

from typing import List

Solution = namedtuple('Solution', 'total_score line_score line_width word line parent')


def process(text, width):
    words = text.split()
    size = [len(w) for w in words]

    best_solution = final_solution = Solution(0, 0, width, 0, -1, None)
    dynamic: List[List[Solution]] = [[best_solution]]

    for i, s in enumerate(size):
        temp = []
        new_min_score = final_solution = Solution(float('inf'), 0, 0, 0, 0, None)
        for j, solution in enumerate(dynamic[-1]):
            if solution.line_width + s + 1 <= width:
                line_width = solution.line_width + s + 1
                line_score = (width - line_width) ** 2
                total_score = solution.total_score - solution.line_score + line_score
                new_solution = Solution(total_score, line_score, line_width, i, solution.line, solution)
                if total_score < new_min_score.total_score:
                    new_min_score = new_solution
                if total_score - line_score < final_solution.total_score:
                    final_solution = Solution(total_score - line_score, 0, line_width, i, solution.line, solution)
                temp.append(new_solution)
            if solution.total_score == best_solution.total_score:
                line_score = (width - s) ** 2
                total_score = solution.total_score + line_score
                new_solution = Solution(total_score, line_score, s, i, solution.line + 1, solution)
                if total_score < new_min_score.total_score:
                    new_min_score = new_solution
                if total_score - line_score < final_solution.total_score:
                    final_solution = Solution(solution.total_score, 0, s, i, solution.line + 1, solution)
                temp.append(new_solution)
        best_solution = new_min_score
        dynamic.append(temp)

    solution = tmp = final_solution
    result = [[] for _ in range(tmp.line + 1)]
    while tmp.parent is not None:
        result[tmp.line].insert(0, words[tmp.word])
        tmp = tmp.parent

    output = '\n'.join(' '.join(line) for line in result)
    return solution.total_score, output


def main():
    if not os.path.exists('output'):
        os.mkdir('output')
    for path in glob.glob(os.path.join('resources', '*.txt')):
        with open(path, encoding='utf-8') as file:
            text = file.read()

        score, result = process(text, 78)
        print(path, score)

        with open(os.path.join('output', os.path.basename(path)), 'w', encoding='utf-8') as output:
            output.write(result)


if __name__ == '__main__':
    main()
