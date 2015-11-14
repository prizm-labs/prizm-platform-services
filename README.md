player-portal
=============

Each console will open a DDP connection to the generalServices server through the PrizmOS/NodeWebkit app.


Services:

- login users
- associate users to tabletop devices
- send associated users to game session

The tabletop app will request platform API for the user IDs associated with its device ID
The tabletop app will register all users as players in the game session.

A companion app will defer to Prizm mobile app or mobile website for logging user in
mobile app or website will launch companion app through custom URL scheme with query parameter
containing user session token.

The companion app will exchange session token for full user information, i.e. userID


App key
s18vv906j28753i
App secret
pnoyg0doihxkt4y
