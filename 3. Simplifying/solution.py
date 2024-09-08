import re
from collections import defaultdict
from time import sleep

def parse_equation(equation):
    lhs, rhs = equation.split("=")
    lhs = lhs.strip()
    rhs = rhs.strip()
    return lhs, rhs


def substitute(formula, equalities):
    for lhs, rhs in equalities:
        formula = re.sub(r"\b" + re.escape(lhs) + r"\b", f"({rhs})", formula)
    return formula


def simplify_formula(formula):
    # Handle parentheses and their coefficients
    while "(" in formula:
        print(formula)
        sleep(1)
        formula = re.sub(
            r"(\d*)\s*\(([^()]+)\)",
            lambda m: (
                f"{m.group(1)}*({m.group(2)})" if m.group(1) else f"({m.group(2)})"
            ),
            formula,
        )
        formula = re.sub(
            r"\(([^()]+)\)", lambda m: f"({simplify_formula(m.group(1))})", formula
        )
    terms = re.findall(r"([+-]?\d*\s*[a-zA-Z])", formula.replace(" ", ""))
    term_dict = defaultdict(int)

    for term in terms:
        match = re.match(r"([+-]?\d*)([a-zA-Z])", term)
        if match:
            coeff, var = match.groups()
            coeff = int(coeff) if coeff not in ("", "+", "-") else int(f"{coeff}1")
            term_dict[var] += coeff

    simplified = "".join(
        f"{coeff}{var}" if coeff != 1 else f"1{var}"
        for var, coeff in sorted(term_dict.items())
    )
    return simplified


def simplify(examples, formula):
    equalities = [parse_equation(eq) for eq in examples]
    print(equalities)
    substituted_formula = substitute(formula, equalities)
    print(substituted_formula)
    simplified_formula = simplify_formula(substituted_formula)
    return simplified_formula


if __name__ == "__main__":
    examples = [
        ["a + a = b", "b - d = c", "a + b = d"],
        ["a + 3g = k", "-70a = g"],
        ["-j -j -j + j = b"],
    ]
    formulas = [
        "c + a + b",
        "-k + a",
        "-j - b",
    ]
    answers = [
        "2a",
        "210a",
        "1j",
    ]

    def check(es, f, exp):
        ess = "".join(f"\n\t{s}" for s in es)
        msg = f"""\
    Examples:{ess}
    Formula:
    \t{f} 
    Test"""
        # print(es, f, exp, simplify(es, f))
        assert simplify(es, f) == (exp, msg)

    for example, formula, answer in zip(examples, formulas, answers):
        check(example, formula, answer)
