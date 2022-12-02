ROCK = "A"
PAPER = "B"
SCISSORS = "C"

# Responses
R_ROCK = "X"
R_PAPER = "Y"
R_SCISSORS = "Z"

BEATS = {
    R_ROCK: SCISSORS,
    R_PAPER: ROCK,
    R_SCISSORS: PAPER,
}

MAPPING = {
    R_ROCK: ROCK,
    R_PAPER: PAPER,
    R_SCISSORS: SCISSORS,
}

SIGN_POINTS = {
    R_ROCK: 1,
    R_PAPER: 2,
    R_SCISSORS: 3,
}


def get_points(prompt, response):
    win_points = 6 if BEATS[response] == prompt else 0
    draw_points = 3 if MAPPING[response] == prompt else 0
    sign_points = SIGN_POINTS[response]
    return win_points + draw_points + sign_points


with open("input.txt") as fd:
    data = fd.read()
    prompt_and_responses = [x.split(" ") for x in data.split("\n")]

    total = 0
    for prompt, response in prompt_and_responses:
        print("prompt: ", prompt, "response: ", response)
        print("score: ", get_points(prompt, response))
        total += get_points(prompt, response)
    print(total)
