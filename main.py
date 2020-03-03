from vk_api.longpoll import VkLongPoll
import vk_api
import confidential

TOKEN = confidential.get_token()


def main():
    vk_session = vk_api.VkApi(token=TOKEN)
    vk_session.auth()


if __name__ == '__main__':
    main()
