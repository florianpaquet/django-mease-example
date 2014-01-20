from djmease import mease
from uuid import uuid4

from ..websocket import make_message


# ---- Openers

@mease.opener
def board_init_subscriptions(client, clients_list):
    """
    Initializes an empty subscription for the client
    """
    client.storage['id'] = str(uuid4())
    client.storage['subscription'] = None


# ---- Receivers

@mease.receiver(json=True)
def board_subscribe(client, message, clients_list):
    """
    Subscribe the client to the board
    """
    if message.get('type') == 'boards.subscribe':
        previous_board_id = client.storage.get('subscription')
        board_id = message.get('data', {}).get('board_id')

        client.storage['subscription'] = board_id

        # Send users on board informations
        users = []

        leave_message = make_message('user.leaveboard', client.storage['id'])

        join_message = make_message('user.joinboard', {
            'id': client.storage['id'],
            'username': client.storage['username']
        })

        for c in clients_list:

            # Inform clients that someone left
            if c.storage.get('subscription') == previous_board_id and c is not client:
                c.send(leave_message)

            # Inform clients that someone joined
            if c.storage['subscription'] == board_id:

                # Inform the client that a user joined
                c.send(join_message)

                # Append user to users on board
                if c is not client:
                    users.append({
                        'id': c.storage['id'],
                        'username': c.storage['username']
                    })

        # Inform client about users on board
        onboard_message = make_message('user.onboard', users)

        client.send(onboard_message)


# ---- Senders

@mease.sender(routing='boards.created')
def board_created(routing, clients_list, board):
    """
    Sends messages on board creation
    """
    message = make_message('boards.created', {
        'id': board.pk,
        'name': board.name,
    })

    for client in clients_list:
        client.send(message)
