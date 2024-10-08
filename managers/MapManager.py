import json
import os


class MapManager:
    cur = 0
    map_data = None

    @staticmethod
    def get_map(r):
        length = len(MapManager.map_data['map'])
        index = MapManager.cur

        start_index = max(0, index - r)
        end_index = min(length, index + r + 1)
        front_part = 'N' * (r - (index - start_index))
        back_part = 'N' * (r - (end_index - index - 1))

        # 결과 문자열 생성
        result = front_part + MapManager.map_data['map'][start_index:end_index] + back_part
        return result

    @staticmethod
    def init():
        base_path = os.path.dirname(os.path.abspath(__file__))  # 현재 파일의 절대 경로
        json_path = os.path.join(base_path, '..', 'stage.json')  # stage.json의 절대 경로
        with open(json_path, 'r') as f:
            MapManager.map_data = json.load(f)
