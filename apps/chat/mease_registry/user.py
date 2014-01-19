import mease

from ..websocket import make_message


# ---- Openers

@mease.opener
def set_initial_username(client, clients_clist):
    """
    Sets an initial guest user name to the client
    """
    guest_id = client.application.storage.get('guests_increment', 0) + 1
    client.application.storage['guests_increment'] = guest_id

    username = 'Guest{guest_id:d}'.format(guest_id=guest_id)
    client.storage['username'] = username

    message = make_message('me.setname', username)

    client.send(message)


# ---- Closers

@mease.closer
def user_logged_out(client, clients_list):
    """
    Inform users that someone logged out
    """
    board_id = client.storage.get('subscription')

    if board_id:
        message = make_message('user.leaveboard', client.storage['id'])

        for c in clients_list:
            if c.storage.get('subscription') == board_id and c is not client:
                c.send(message)


# ---- Receivers

@mease.receiver(json=True)
def set_username(client, message, clients_list):
    """
    Sets an user name
    """
    if message.get('type') == 'user.setname':
        username = message.get('data', {}).get('username')
        client.storage['username'] = username

        board_id = client.storage.get('subscription')

        if board_id:
            message = make_message('user.setname', {
                'id': client.storage.get('id'),
                'username': username
            })

            for c in clients_list:
                if c.storage.get('subscription') == board_id:
                    c.send(message)
