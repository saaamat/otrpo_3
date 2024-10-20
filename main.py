import requests
import json

def get_vk_user_info(user_id, access_token):
    url = 'https://api.vk.com/method/users.get'
    params = {
        'user_ids': user_id,
        'access_token': access_token,
        'v': '5.131'
    }
    response = requests.get(url, params=params)
    return response.json()

def get_user_followers(user_id, access_token):
    url = 'https://api.vk.com/method/users.getFollowers'
    params = {
        'user_id': user_id,
        'access_token': access_token,
        'v': '5.131'
    }
    response = requests.get(url, params=params)
    return response.json()

def get_user_subscriptions(user_id, access_token):
    url = 'https://api.vk.com/method/users.getSubscriptions'
    params = {
        'user_id': user_id,
        'access_token': access_token,
        'v': '5.131'
    }
    response = requests.get(url, params=params)
    return response.json()

def main():
    user_id = input('Введите ID пользователя(123456 или username): ')
    access_token = input('Ваш токен: ')

    user_info = get_vk_user_info(user_id, access_token)
    id_value = user_info['response'][0]['id']
    followers_info = get_user_followers(id_value, access_token)
    subscriptions_info = get_user_subscriptions(id_value, access_token)

    if 'response' in followers_info and len(followers_info['response']) > 0:
        followers_count = len(followers_info['response'])
    else:
        print("У пользователя нет подписчиков.")
        return

    if 'response' in subscriptions_info and len(subscriptions_info['response']['groups']['items']) > 0:
        subscriptions_count = len(subscriptions_info['response']['groups']['items'])
    else:
        print("У пользователя нет подписок.")
        return

    result = {
        'Информация': user_info['response'],
        'Кол-во подписчиков': followers_count,
        'Кол-во подписок': subscriptions_count,
        'Фолловеры': followers_info['response'],
        'Подписки': subscriptions_info['response']['groups']['items']
    }

    with open('vk_user_info.json', 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=4)

    print("Информация сохранена в файл vk_user_info.json")

if __name__ == "__main__":
    main()
