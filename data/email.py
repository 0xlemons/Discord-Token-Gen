from kopeechka import MailActivations, KopeechkaApiError

api = MailActivations("c26acb9797d1b02c0c58950ac58707b3")

def get_mail(provider: str):
    try:
        ans_2 = api.mailbox_get_email("rambler.ru")
        print(ans_2)
    except KopeechkaApiError as e:
        print(e)
