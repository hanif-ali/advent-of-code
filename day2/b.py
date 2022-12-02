ROCK = "A"
PAPER = "B"
SCISSORS = "C"

LOSE = "X"
DRAW = "Y"
WIN = "Z"

BEATS = {
    ROCK: SCISSORS,
    PAPER: ROCK,
    SCISSORS: PAPER,
}

LOSES = {
    SCISSORS: ROCK,
    ROCK: PAPER,
    PAPER: SCISSORS,
}

SIGN_POINTS = {
    ROCK: 1,
    PAPER: 2,
    SCISSORS: 3,
}


def get_points(prompt, response):
    if response == WIN:
        return 6 + SIGN_POINTS[LOSES[prompt]]
    if response == DRAW:
        return 3 + SIGN_POINTS[prompt]
    if response == LOSE:
        return SIGN_POINTS[BEATS[prompt]]


with open("input.txt") as fd:
    data = fd.read()
    prompt_and_responses = [x.split(" ") for x in data.split("\n")]

    total = 0
    for prompt, response in prompt_and_responses:
        print("prompt: ", prompt, "response: ", response)
        print("score: ", get_points(prompt, response))
        total += get_points(prompt, response)
    print(total)
