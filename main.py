from vk_api.longpoll import VkLongPoll, VkEventType
import vk_api
import confidential
from random import randint, choice

TOKEN = confidential.TOKEN


def write_msg(user_id, message, vk_session):
    vk_session.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': randint(0, 10**5)})


greeting_msg = ['хай', 'привет', 'здарова', 'здравствуйте', 'дарова', 'hi', 'hello']
farewell_msg = ['пока', 'досвидания', 'пока пока']


def main():
    vk_session = vk_api.VkApi(token=TOKEN)
    longpoll = VkLongPoll(vk_session)

    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:

            if event.to_me:
                request = event.text.lower()
                print(request)

                # Каменная логика ответа
                if request in greeting_msg:
                    write_msg(event.user_id, choice(greeting_msg), vk_session)
                elif request in farewell_msg:
                    write_msg(event.user_id, choice(farewell_msg), vk_session)
                else:
                    write_msg(event.user_id, "Не понял, что вы сказали", vk_session)


if __name__ == '__main__':
    main()
