import os
import pyrogram
from pyrogram import Client

api_id = 7322837
api_hash = "2047a64426f81acbb180c0a749b5d565"

try:
   os.remove("masamba.session")
except:
     pass
with Client("peamasamba", api_id=api_id, api_hash=api_hash) as app:
    session = f"**🥀 𝐏𝐲𝐫𝐨𝐠𝐫𝐚𝐦 » 𝐒𝐭𝐫𝐢𝐧𝐠 𝐒𝐞𝐬𝐬𝐢𝐨𝐧 💞**\n\n`{app.export_session_string()}`\n\n**💥 𝐏𝐨𝐰𝐞𝐫𝐞𝐝 𝐁𝐲: [𝐏𝐞𝐚 𝐌𝐚𝐬𝐚𝐦𝐛𝐚](https://t.me/CollectionMovie_Subtitles) ✨**"
    app.send_message("me", session, disable_web_page_preview=True)
    try:
        app.join_chat("PeaMasamba")
        app.join_chat("PeaMasamba")
        app.join_chat("PeaMasamba")
        app.join_chat("Pea_Masamba")
    except:
        pass
    print(f"✅ String Session Has 🌟 Been Sent\nTo Your 🔥 Saved Message ✨ ...")
    os.remove("masamba.session")


