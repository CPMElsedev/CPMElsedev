import requests
import json

BASE_URL = "https://cpm2api.squareweb.app"

class CPMElse:
    def __init__(self, access_key):
        self.idToken = None
        self.access_key = access_key

    def get_key_access(self):
        url = f"{BASE_URL}/auth/get_key_acess.php"
        params = {"key": self.access_key}
        response = requests.get(url, params=params)

        if response.status_code == 200:
            data = response.json()
            if "user_id" in data and "api_key" in data and "expires_at" in data:
                return data  # Retorna os dados da chave de acesso
            else:
                return {"error": "Chave de acesso inválida."}
        else:
            return {"error": "Falha ao obter a chave de acesso."}

    def login(self, email, password):
        url = f"{BASE_URL}/auth/get_id_token.php"
        params = {
            "email": email,
            "password": password,
            "key": self.access_key  # Incluindo o parâmetro key
        }
        response = requests.get(url, params=params)

        if response.status_code == 200:
            data = response.json()
            self.idToken = data.get("idToken")
            if self.idToken:
                return 0  # Login bem-sucedido
            else:
                return 101  # Senha incorreta
        else:
            return 100  # Conta não encontrada ou outro erro

    def get_player_data(self):
        if not self.idToken:
            return {"ok": False, "error": "Nenhum idToken disponível. Login necessário."}
        
        url = f"{BASE_URL}/player/get_player_data.php"
        params = {
            "idToken": self.idToken,
            "key": self.access_key  # Incluindo o parâmetro key
        }
        response = requests.get(url, params=params)
        
        if response.status_code == 200:
            return {"ok": True, "data": response.json()}
        else:
            return {"ok": False, "error": "Falha ao recuperar os dados do jogador."}

    def set_player_name(self, new_name):
        if not self.idToken:
            return False
        
        url = f"{BASE_URL}/player/set_player_name.php"
        params = {
            "idToken": self.idToken,
            "name": new_name,
            "key": self.access_key  # Incluindo o parâmetro key
        }
        response = requests.post(url, params=params)
        
        return response.status_code == 200

    def set_player_id(self, new_id):
        if not self.idToken:
            return False
        
        url = f"{BASE_URL}/player/set_player_localid.php"
        params = {
            "idToken": self.idToken,
            "id": new_id,
            "key": self.access_key  # Incluindo o parâmetro key
        }
        response = requests.post(url, params=params)
        
        return response.status_code == 200

    def insert_money(self, amount):
        if not self.idToken:
            return False
        
        url = f"{BASE_URL}/player/set_player_money.php"
        params = {
            "idToken": self.idToken,
            "amount": amount,
            "key": self.access_key  # Incluindo o parâmetro key
        }
        response = requests.post(url, params=params)
        
        return response.status_code == 200

    def insert_slots(self, slots):
        if not self.idToken:
            return False
        
        url = f"{BASE_URL}/player/set_player_slots.php"
        params = {
            "idToken": self.idToken,
            "slots": slots,
            "key": self.access_key  # Incluindo o parâmetro key
        }
        response = requests.post(url, params=params)
        
        return response.status_code == 200

    def unlock_all_houses(self):
        if not self.idToken:
            return False
        
        url = f"{BASE_URL}/player/unlock_houses.php"
        params = {
            "idToken": self.idToken,
            "key": self.access_key  # Incluindo o parâmetro key
        }
        response = requests.post(url, params=params)
        
        return response.status_code == 200

    def set_player_king_rank(self):
        if not self.idToken:
            return False
        
        url = f"{BASE_URL}/player/set_player_king_rank.php"
        params = {
            "idToken": self.idToken,
            "key": self.access_key  # Incluindo o parâmetro key
        }
        response = requests.post(url, params=params)
        
        return response.status_code == 200

    def set_player_all_levels(self):
        if not self.idToken:
            return False
        
        url = f"{BASE_URL}/player/set_player_all_levels.php"
        params = {
            "idToken": self.idToken,
            "key": self.access_key  # Incluindo o parâmetro key
        }
        response = requests.post(url, params=params)
        
        return response.status_code == 200

    def unlock_all_wheels(self):
        if not self.idToken:
            return False
        
        url = f"{BASE_URL}/player/unlock_all_wheels.php"
        params = {
            "idToken": self.idToken,
            "key": self.access_key  # Incluindo o parâmetro key
        }
        response = requests.post(url, params=params)
        
        return response.status_code == 200

    def unlock_equip_female(self):
        if not self.idToken:
            return False
        
        url = f"{BASE_URL}/player/unlock_equip_female.php"
        params = {
            "idToken": self.idToken,
            "key": self.access_key  # Incluindo o parâmetro key
        }
        response = requests.post(url, params=params)
        
        return response.status_code == 200

    def unlock_equip_male(self):
        if not self.idToken:
            return False
        
        url = f"{BASE_URL}/player/unlock_equip_male.php"
        params = {
            "idToken": self.idToken,
            "key": self.access_key  # Incluindo o parâmetro key
        }
        response = requests.post(url, params=params)
        
        return response.status_code == 200

    def unlock_all_brakes(self):
        if not self.idToken:
            return False
        
        url = f"{BASE_URL}/player/unlock_all_brakes.php"
        params = {
            "idToken": self.idToken,
            "key": self.access_key  # Incluindo o parâmetro key
        }
        response = requests.post(url, params=params)
        
        return response.status_code == 200

    def unlock_all_calipers(self):
        if not self.idToken:
            return False
        
        url = f"{BASE_URL}/player/unlock_all_calipers.php"
        params = {
            "idToken": self.idToken,
            "key": self.access_key  # Incluindo o parâmetro key
        }
        response = requests.post(url, params=params)
        
        return response.status_code == 200

    def unlock_all_paint(self):
        if not self.idToken:
            return False
        
        url = f"{BASE_URL}/player/unlock_all_paint.php"
        params = {
            "idToken": self.idToken,
            "key": self.access_key  # Incluindo o parâmetro key
        }
        response = requests.post(url, params=params)
        
        return response.status_code == 200

    def unlock_all_car(self, car):
        if not self.idToken:
            return False
        
        url = f"{BASE_URL}/player/unlock_all_car.php"
        params = {
            "idToken": self.idToken,
            "key": self.access_key,
            "car": car
        }
        response = requests.post(url, params=params)
        
        return response.status_code == 200

    def set_crash_acc_v1(self):
        if not self.idToken:
            return False
        
        url = f"{BASE_URL}/player/set_crash_acc_v1.php"
        params = {
            "idToken": self.idToken,
            "key": self.access_key  # Incluindo o parâmetro key
        }
        response = requests.post(url, params=params)
        
        return response.status_code == 200

    def set_fix_acc_v1(self):
        if not self.idToken:
            return False
        
        url = f"{BASE_URL}/player/set_fix_acc_v1.php"
        params = {
            "idToken": self.idToken,
            "key": self.access_key  # Incluindo o parâmetro key
        }
        response = requests.post(url, params=params)
        
        return response.status_code == 200

    def set_crash_acc_v2(self):
        if not self.idToken:
            return False
        
        url = f"{BASE_URL}/player/set_crash_acc_v2.php"
        params = {
            "idToken": self.idToken,
            "key": self.access_key  # Incluindo o parâmetro key
        }
        response = requests.post(url, params=params)
        
        return response.status_code == 200

    def set_fix_acc_v2(self):
        if not self.idToken:
            return False
        
        url = f"{BASE_URL}/player/set_fix_acc_v1.php"
        params = {
            "idToken": self.idToken,
            "key": self.access_key  # Incluindo o parâmetro key
        }
        response = requests.post(url, params=params)
        
        return response.status_code == 200
