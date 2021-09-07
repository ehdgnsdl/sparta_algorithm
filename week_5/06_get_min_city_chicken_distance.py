import itertools, sys

n = 5
m = 3

city_map = [
    [0, 0, 1, 0, 0],
    [0, 0, 2, 0, 1],
    [0, 1, 2, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 2],
]

# 여러 개 중에서 M개를 고른뒤, 모든 치킨 거리의 합이 가장 작게 되는 경우를 반환
# -> 여러 개 중에서 특정 개수를 뽑는 경우의 수
# -> 모든 경우의 수를 다 구해야함. - 조합


def get_min_city_chicken_distance(n, m, city_map):
    chicken_location_list = [] # 치킨 집 위치 저장
    home_location_list = [] # 집 위치 저장
    for i in range(n):
        for j in range(n):
            if city_map[i][j] == 1:
                home_location_list.append([i, j])
            elif city_map[i][j] == 2:
                chicken_location_list.append([i, j])

    chicken_location_m_combinations = list(itertools.combinations(chicken_location_list, m))

    min_distance_of_m_combinations = sys.maxsize

    for chicken_location_m_combination in chicken_location_m_combinations:
        city_chicken_distance = 0
        for home_r, home_c in home_location_list:
            min_home_chicken_distance = sys.maxsize
            for chicken_location in chicken_location_m_combination:
                min_home_chicken_distance = min(
                    min_home_chicken_distance,
                    abs(home_r - chicken_location[0]) + abs(home_c - chicken_location[1])
                )
            city_chicken_distance += min_home_chicken_distance

        min_distance_of_m_combinations = min(min_distance_of_m_combinations, city_chicken_distance)
    return min_distance_of_m_combinations


# 출력
print(get_min_city_chicken_distance(n, m, city_map))  # 5 가 반환되어야 합니다!
print("hihihi")