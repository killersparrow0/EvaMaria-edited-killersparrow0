class script(object):
    START_TXT = """𝑯𝒐𝒍𝒂 👋 {},
𝑴𝒚 𝒏𝒂𝒎𝒆 𝒊𝒔 <a href=https://t.me/{}>{}</a>, 𝑰 𝒄𝒂𝒏 𝒑𝒓𝒐𝒗𝒊𝒅𝒆 𝒎𝒐𝒗𝒊𝒆𝒔, 𝑱𝒖𝒔𝒕 𝒋𝒐𝒊𝒏 @movie_ott 𝒂𝒏𝒅 𝒄𝒉𝒊𝒍𝒍 😎🍿."""
    HELP_TXT = """𝑯𝒐𝒍𝒂 {}
𝑯𝒆𝒓𝒆 𝒊𝒔 𝒕𝒉𝒆  𝒉𝒆𝒍𝒑  𝒇𝒐𝒓 𝒎𝒚 𝒄𝒐𝒎𝒎𝒂𝒏𝒅."""
    ABOUT_TXT = """✯ 𝑴𝒚 𝑵𝒂𝒎𝒆: {}
✯ 𝑪𝒓𝒆𝒂𝒕𝒐𝒓: <a href=https://t.me/TeamEvamaria> 𝑻𝒆𝒂𝒎 𝑬𝒗𝒂 𝑴𝒂𝒓𝒊𝒂 </a>
✯ 𝑬𝒅𝒊𝒕𝒐𝒓 : <a href=https://t.me/elonmuskme> @𝒆𝒍𝒐𝒏𝒎𝒖𝒔𝒌𝒎𝒆 </a>
✯ 𝑳𝒊𝒃𝒓𝒂𝒓𝒚: 𝑷𝒚𝒓𝒐𝒈𝒓𝒂𝒎
✯ 𝑳𝒂𝒏𝒈𝒖𝒂𝒈𝒆: 𝑷𝒚𝒕𝒉𝒐𝒏 3
✯ 𝑫𝒂𝒕𝒂 𝑩𝒂𝒔𝒆: 𝑴𝒐𝒏𝒈𝒐 𝑫𝑩
✯ 𝑩𝒐𝒕 𝑺𝒆𝒓𝒗𝒆𝒓: 𝑯𝒆𝒓𝒐𝒌𝒖
✯ 𝑩𝒖𝒊𝒍𝒅 𝑺𝒕𝒂𝒕𝒖𝒔: 𝒗1.0.1 [ 𝑪𝒖𝒔𝒕𝒐𝒎 𝒃𝒖𝒊𝒍𝒅 𝒐𝒇 <a href=https://t.me/elonmuskme> @𝒆𝒍𝒐𝒏𝒎𝒖𝒔𝒌𝒎𝒆 </a> ]"""
    SOURCE_TXT = """<b>NOTE:</b>
- 𝑬𝒗𝒂 𝑴𝒂𝒓𝒊𝒂 𝒊𝒔 𝒂 𝒐𝒑𝒆𝒏 𝒔𝒐𝒖𝒓𝒄𝒆 𝒑𝒓𝒐𝒋𝒆𝒄𝒕. 
- 𝑺𝒐𝒖𝒓𝒄𝒆 - https://github.com/EvamariaTG/EvaMaria  

<b>DEVS:</b>
- <a href=https://t.me/TeamEvamaria>Team Eva Maria</a>"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and EvaMaria will respond whenever a keyword is found the message

<b>NOTE:</b>
1. eva maria should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- Eva Maria Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. Eva Maria supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/EvaMariaBot)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of Eva Maria

<b>Commands and Usage:</b>
• /id - <code>get id of a specifed user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """★ 📁𝑻𝒐𝒕𝒂𝒍 𝒇𝒊𝒍𝒆: <code>{}</code>
★ 👥𝑻𝒐𝒕𝒂𝒍 𝒖𝒔𝒆𝒓𝒔: <code>{}</code>
★ 💬𝑻𝒐𝒕𝒂𝒍 𝒄𝒉𝒂𝒕𝒔: <code>{}</code>
★ 📀𝑼𝒔𝒆𝒅 𝒔𝒕𝒐𝒓𝒂𝒈𝒆: <code>{}</code> 𝑴𝒊𝑩
★ 🆓𝑭𝒓𝒆𝒆 𝒔𝒕𝒐𝒓𝒂𝒈𝒆: <code>{}</code> 𝑴𝒊𝑩"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
