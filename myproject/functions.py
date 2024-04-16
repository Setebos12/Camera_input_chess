import requests

def is_game_ready(data):
  return len(data['nowPlaying']) > 0


def get_data(api_token):
  url = f"https://lichess.org/api/account/playing"
  headers = {"Authorization": f"Bearer {api_token}"}
  response = requests.get(url, headers=headers)
  data = response.json()
  return data


def is_my_turn(data):
  return data['nowPlaying'][0]['isMyTurn']


def send_move(game_id, move, api_token):
    url = f"https://lichess.org/api/board/game/{game_id}/move/{move}"
    headers = {"Authorization": f"Bearer {api_token}"}

    response = requests.post(url, headers=headers)

    if response.status_code == 200:
        print("Move sent successfully!")
    else:
        print("Failed to send move. Error:", response.text)



