def solution(bandage, health, attacks):
    max_health = health
    answer = health
    cnt = 0

    for i in range(1, (attacks[-1][0] + 1)):
        attacked = False

        for j in range(len(attacks)):
            if i == attacks[j][0]:
                answer -= attacks[j][1]
                cnt = 0
                attacked = True
                break

        if answer <= 0:
            return -1

        if not attacked:
            answer = min(max_health, answer + bandage[1]) 
            cnt += 1

            if cnt == bandage[0]:
                answer = min(max_health, answer + bandage[2])
                cnt = 0

    return answer