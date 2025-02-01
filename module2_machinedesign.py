from cse355_machine_design import DFA, registry


def problem1():
    """
    L_1 = {w in {0,1}* | w contains 010 as a substring}
    """

    Q = {}
    Sigma = {}
    delta = {

    }
    q0 = ""
    F = {}

    return DFA(Q, Sigma, delta, q0, F)


def problem2():
    """
    L_2 = {w in {0,1}* | w does not contain 100 as a substring}
    """

    Q = {}
    Sigma = {}
    delta = {

    }
    q0 = ""
    F = {}

    return DFA(Q, Sigma, delta, q0, F)


def problem3():
    """
    L_3 = {w in {a,b}* | |w| < 4}
    """

    Q = {}
    Sigma = {}
    delta = {

    }
    q0 = ""
    F = {}

    return DFA(Q, Sigma, delta, q0, F)


def problem4():
    """
    L_4 = {w in {a,b,c}* | w has an even number of b's}
    """

    Q = {}
    Sigma = {}
    delta = {

    }
    q0 = ""
    F = {}

    return DFA(Q, Sigma, delta, q0, F)


def problem5():
    """
    L_5 = {epsilon, 0, 101} on Sigma = {0, 1}
    """

    Q = {}
    Sigma = {}
    delta = {

    }
    q0 = ""
    F = {}

    return DFA(Q, Sigma, delta, q0, F)


def problem6():
    """
    L_6 = {w in {1}* | |w| is a multiple of 2 or 3}
    """

    Q = {}
    Sigma = {}
    delta = {

    }
    q0 = ""
    F = {}

    return DFA(Q, Sigma, delta, q0, F)


def problem7():
    """
    L_7 = {w in {a,b}* | w has an even number of a's, contains aab as a
                         substring, or both}
    """

    Q = {}
    Sigma = {}
    delta = {

    }
    q0 = ""
    F = {}

    return DFA(Q, Sigma, delta, q0, F)


if __name__ == "__main__":
    problem1().submit_as_answer(1)
    problem2().submit_as_answer(2)
    problem3().submit_as_answer(3)
    problem4().submit_as_answer(4)
    problem5().submit_as_answer(5)
    problem6().submit_as_answer(6)
    problem7().submit_as_answer(7)
    registry.export_submissions()
