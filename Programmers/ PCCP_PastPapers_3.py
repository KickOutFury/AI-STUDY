def solution(h1, m1, s1, h2, m2, s2):
    time = 43200  # 360도 * 120

    def hour_angle(t):
        return t % time          # 시침: 1초에 1

    def minute_angle(t):
        return (12 * t) % time   # 분침: 1초에 12

    def second_angle(t):
        return (720 * t) % time  # 초침: 1초에 720

    def alarm_now(t):
        s = second_angle(t)
        m = minute_angle(t)
        h = hour_angle(t)
        return 1 if (s == m or s == h) else 0

    t1 = h1 * 3600 + m1 * 60 + s1
    t2 = h2 * 3600 + m2 * 60 + s2

    answer = alarm_now(t1)  # 시작 시각 포함

    for t in range(t1, t2):
        s = second_angle(t)
        m = minute_angle(t)
        h = hour_angle(t)

        # 현재 시각 t에서 분침/시침이 초침보다 얼마나 앞에 있는지
        dm = (m - s) % time
        dh = (h - s) % time

        crossed_m = (0 < dm <= 708)  # 720 - 12 / 초침 vs 분침
        crossed_h = (0 < dh <= 719)    # 720 - 1 / 초침 vs 시침

        answer += crossed_m
        answer += crossed_h

        # 00시/12시 정각 겹침은 1번만 체크
        if (t + 1) % 43200 == 0 and crossed_m and crossed_h:
            answer -= 1

    return answer