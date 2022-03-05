'''
To test: python3 -m websockets ws://localhost:8081/
Then paste one of the following messages:
    * { "type": "login", "username": "walter" }
    * { "type": "disconnect" }
    * { "type": "chat", "text": "Hello world!", "username": "walter" }
    * { "type": "invalid", "text": "this is an invalid message" }
    
'''

from dotenv import load_dotenv
load_dotenv()

import asyncio
import websockets
import json
import os

logged_in_users = dict()

PORT = os.environ.get('WS_PORT') or 8081

async def broadcast(data):
    for sock in logged_in_users:
        await sock.send(json.dumps(data))

async def disconnect_user(websocket):
    if websocket not in logged_in_users:
        return

    del logged_in_users[websocket]
    await broadcast({'type': 'disconnect',
                     'users': list(logged_in_users.values())})

async def respond_to_message(websocket, message):
    try:
        data = json.loads(message)
    except:
        data = { 
            'error': 'error decoding {0}'.format(message),
            'details': 'See instructions for list of valid message formats.'}
        return await websocket.send(json.dumps(data))
    '''
    ******************************************************************
    * Server-Side Logic: Your Job 
    *******************************************************************
    The websocket.send(json.dumps(data)) (line 74, below) 
    echos a received message back to the sender. 
    Your job is to do a little processing and validation of the 
    messages in order to:
        * Track current users / websocket connections.
        * Relay the correct messages to all of the websockets that
          are connected to the server.
           
    Specifically:
    
    1. If the data.get('type') is 'login', add the logged in user to
       the logged_in_users dictionary. Then, send the following message
       back to the clients:
           {
               "type": "login",
               "users": list(logged_in_users.values())
           }
       HINT:  Use the following code to REMOVE a tracked user/socket 
       from the server's memory:
            logged_in_users[websocket] = data.get('username')
    
    2. If the data.type is "disconnect", remove the user from
       the logged_in_users dictionary. Then, send the following message
       back to the clients:
           {
               "type": "disconnect",
               "users": list(logged_in_users.values())
           }
       
       HINT:  Use the following code to REMOVE a tracked user/socket 
       from the server's memory:
            del logged_in_users[websocket]
    
    
    3. If the data.type is "chat", just pass on the entire
       data object to the clients (no processing needed).
    
    4. Otherwise, ignore the message (don't pass it on), and
       log it to the console:
    
            console.log('Unrecognized message type:', data);

    To send messages to all of the clients, iterate through the 
    logged_in_users (which stores each websocket-username) pair.
    ********************************************************************/
    '''
    
    match data:
        case {'type': 'login', 'username': username}:
            logged_in_users[websocket] = username
            await broadcast({'type': 'login',
                             'users': list(logged_in_users.values())})
        case {'type': 'disconnect'}:
            await disconnect_user(websocket)
        case {'type': 'chat'}:
            await broadcast(data)
        case _:
            await websocket.send(json.dumps({'error': f'error decoding {data}',
                                             'details': 'See instructions for list of valid message formats.'}))



async def broadcast_messages(websocket, path):
    try:
        async for message in websocket:
            await respond_to_message(websocket, message)
    except websockets.ConnectionClosed as e:
        print('A client just disconnected')
        print(e)
    finally:
        await disconnect_user(websocket)
    

async def main():
    async with websockets.serve(broadcast_messages, "", PORT):
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    print('Starting web socket server...')
    print('ws://localhost:{0}'.format(PORT))
    asyncio.run(main())