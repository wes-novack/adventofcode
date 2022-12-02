def read_file():
    games = []
    with open("input.txt") as input_list:
        for line in input_list:
            games.append(line)
    return games


def main():
    rock_score = 1
    paper_score = 2
    scissor_score = 3
    draw_score = 3
    win_score = 6

    games = read_file()
    total_score = 0
    for game in games:
        game_choices = game.split()
        if game_choices[0] == 'A':
            if game_choices[1] == 'X':
                total_score += rock_score
                total_score += draw_score
            elif game_choices[1] == 'Y':
                total_score += paper_score
                total_score += win_score
            else:
                total_score += scissor_score
    
        elif game_choices[0] == 'B':
            if game_choices[1] == 'X':
                total_score += rock_score
            elif game_choices[1] == 'Y':
                total_score += paper_score
                total_score += draw_score
            else:
                total_score += scissor_score
                total_score += win_score

        elif game_choices[0] == 'C':
            if game_choices[1] == 'X':
                total_score += rock_score
                total_score += win_score
            elif game_choices[1] == 'Y':
                total_score += paper_score
            else:
                total_score += scissor_score
                total_score += draw_score

        else:
            print("ERROR: invalid first game choice")
    print(total_score)


if __name__ == '__main__':
    main()