
class MapManager:
    map_data = "TEETEETEETEETEETEETEETEETEETEET"
    cur = 0

    @staticmethod
    def get_map(r):
        length = len(MapManager.map_data)
        index = MapManager.cur

        start_index = max(0, index - r)
        end_index = min(length, index + r + 1)
        front_part = 'N' * (r - (index - start_index))
        back_part = 'N' * (r - (end_index - index - 1))

        # 결과 문자열 생성
        result = front_part + MapManager.map_data[start_index:end_index] + back_part
        return result
