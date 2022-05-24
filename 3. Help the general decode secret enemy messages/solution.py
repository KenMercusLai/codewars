CODE_SPACE = 'abdhpF,82QsLirJejtNmzZKgnB3SwTyXG ?.6YIcflxVC5WE94UA1OoD70MkvRuPqH'


def decode(s):
    return ''.join([CODE_SPACE[(CODE_SPACE.index(v) + 65 - i) % 66] if v in CODE_SPACE else v
                    for i, v in enumerate(s)])
