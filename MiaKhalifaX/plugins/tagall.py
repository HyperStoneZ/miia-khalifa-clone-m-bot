from MiaKhalifaX import app 
import asyncio
import random
from pyrogram import Client, filters
from pyrogram.errors import UserNotParticipant
from pyrogram.types import ChatPermissions

spam_chats = []

EMOJI = [ "🦋🦋🦋🦋🦋",
          "🧚🌸🧋🍬🫖",
          "😠🌷🌹🌺💐",
          "🌸🌿💮🌱🌵",
          "❤️💚💙💜🖤",
          "💓💕💞💗💖",
          "🌸💐🌺🌹🦋",
          "🍔🦪🍛🍲🥗",
          "🍎🍓🍒🍑🌶️",
          "🧋🥤🧋🥛🍷",
          "🍬🍭🧁🎂🍡",
          "🍨🧉🍺☕🍻",
          "🥪🥧🍦🍥🍚",
          "🫖☕🍹🍷🥛",
          "☕🧃🍩🍦🍙",
          "🍁🌾💮🍂🌿",
          "🌨️🌥️⛈️🌩️🌧️",
          "🌷🏵️🌸🌺💐",
          "💮🌼🌻🍀🍁",
          "🧟🦸🦹🧙👸",
          "🧅🍠🥕🌽🥦",
          "🐷🐹🐭🐨🐻‍❄️",
          "🦋🐇🐀🐈🐈‍⬛",
          "🌼🌳🌲🌴🌵",
          "🥩🍋🍐🍈🍇",
          "🍴🍽️🔪🍶🥃",
          "🕌🏰🏩⛩️🏩",
          "🎉🎊🎈🎂🎀",
          "🪴🌵🌴🌳🌲",
          "🎄🎋🎍🎑🎎",
          "🦅🦜🕊️🦤🦢",
          "🦤🦩🦚🦃🦆",
          "🐬🦭🦈🐋🐳",
          "🐔🐟🐠🐡🦐",
          "🦩🦀🦑🐙🦪",
          "🐦🦂🕷️🕸️🐚",
          "🥪🍰🥧🍨🍨",
          " 🥬🍉🧁🧇",
        ]

TAGSRT = [ " **ரொம்ப நாளை பண்ணுங்க பொண்ணுக்கு முகிலில போட்டி 😄😄😄** ",
           " **கண்டிப்பா எல்லாம் பார்த்ததுக்கு மகிழ்ச்சி கிடைக்குது 🤣🤣🤣** ",
           " **அப்புறம் பத்தி ஆகுது, எப்படி கத்திய எடுத்து அப்படியே பிழிக்கவே முடியாது 🙃🙃🙃** ",
           " **சிறு பேச்சுக்கு பேச்சு சிறு, ஆனா எல்லாம் சொல்லி சொல்லி சிறுப்பேச்சு 😜😜😜** ",
           " **இது போதும் இல்ல போதும் பொய்யா என்று கேட்டு கொள்ள நான் கவலை படுத்துறீங்க 🤭🤭🤭** ",
           " **நான் என்ன சொன்னாலும் நீ எப்படி பார்த்தது அதை மாதிரி மாதிரி பொய்யாக கேட்குற நிலையில்லை 😂😂😂** ",
           " **அடுத்த வாரம் பண்ணுவேன் பசங்க நாரையை விரித்து விட்டு வர வைக்கும் 🤣🤣🤣** ",
           " **இந்த பேச்சு எப்படி பத்தி குடுத்து இருக்கு போல இல்லையா 😆😆😆** ",
           " **மதுரை மருத்துவமனை குடும்பத்திற்கு உங்களை பரிதாபிக்கப்பட்டதாக இருக்கு 🤭🤭🤭** ",
           " **பின்னுவீங்க பின்னு அடிங்கிவிடுங்க அடி விடுங்க சொல்லுங்க சொல் அடி செய்யுங்க 😜😜😜** ",
           " **வாழ்க்கையை காட்டிலும் மகிழுங்கள், என்னது எதிர்பார்ப்பு விரும்பினால் அது பிரபஞ்சமாகப் பேசுவது போன்றது.** ",
           " **முழு உலகம் என்னை பற்றி கூட நிச்சயமா அறியாம நிலையில் இருக்கின்றன், ஆனால் நினைத்து நேரம் வராது எனக்கு என்ன பயன்!** ",
           " **நான் புத்தி கேட்டா போனா நேரம், நான் கை விட்டு ஓடிவிட்டேன்!** ",
           " **நான் எப்போதும் விழித்துக்கொள்வது என்றால், அது ஒரு நல்ல சிரிப்பை கொண்டிருக்கும்.** ",
           " **சரித்திரத்தின் எனக்கு மிகுந்த அதிசயம், நான் நடிப்புக்கு அந்த அதிசயத்தை கொடுத்தவன்!** ",
           " **நினைவு தொடர்ந்து என் உயிரை அடைக்கும், புது காலத்தின் மொழி என் மனதில் மூடும்** ",
           " **கண்களில் உள்ள நீர் வழியில் இருக்கும், நான் நெஞ்சில் கலங்கி இருக்கும்.** ",
           " **என் மனதின் நினைவுகள் உன்னை தேடும், உன் மனதின் நினைவுகள் எனை விட்டுப் போகும்.** ",
           " **𝐃𝐨 𝐘𝐨𝐮 𝐊𝐧𝐨𝐰 𝐖𝐡𝐨 𝐈𝐬 𝐌𝐲 𝐎𝐰𝐧𝐞𝐫.?** ",
           " **நீ எப்போதும் என் வாழ்க்கையின் புனித கவிதை, நேசிக்க மாட்டாய் என் நினைவு கவிதை",
           " **நினைவுகள் எனக்கு அழகுக் கவிதைகள், அவை என் மனதில் அடித்திடும்** ",
           " **விருப்பம் விரும்பாமல் உணர்ந்து செயல் படாமல் விரும்பினால் அது மட்டும் நிச்சயமாக தோன்றும்.** ",
           " **எப்போதும் புதிய சோதனைகளை எடுத்து நம்மை மேம்படுத்துவோம், நிச்சயமாக எல்லா தோன்றலுக்கும் அடிப்படை கிடைக்கும்** ",
           " **யாம் பெற்ற மெல்லிய கோழி, அது எப்படி குஞ்சுகுஞ்சு என்று கூறுவாய்?  Answer: பெண் குஞ்சுகுஞ்சு கோழி (குஞ்சுகுஞ்சு - குழந்தை)** ",
           " **எவ்விடத்தில் இருக்கும் பழம் உற்றவர் யார்?** ",
           " **அந்த குட்டியும் நானும் கொஞ்சம் செங்குத்து போட்டே போகும், யார் நாம்?** ",
           " **மூன்று பாதங்களுள்ள நாதஸ்வரம் என்ன?** ",
           " **மரத்தில் பழம் ஏது** ",
           " **எல்லாரும் வாழ்க்கையில் மகிழுங்கள்! 🎉** ",
           " **𝐇𝐞𝐥𝐥𝐨🙊** ",
           " **எல்லாரும் வாழ்க்கையில் மகிழுங்கள்! 🎉??😺** ",
           " **நலமாக காலை காட்டியது உங்கள் நண்பர்கள்! 🌞** ",
           " **இனிய மன்னிப்பு நண்பர்களே! 😊** ",
           " **உங்கள் நண்பர்களுககு வாழ்த்துக்கள்! 🎈** ",
           " **குழந்தைகளுக்கு என்று மகிழுங்கள்! 🧒🧒🧒** ",
           " **இனிய குடும்ப நண்பர்கள் நேர்காணல்! 👪👪👪** ",
           " **𝐈 𝐋𝐨𝐯𝐞 𝐘𝐨𝐮🙈🙈🙈** ",
           " **𝐃𝐨 𝐘𝐨𝐮 𝐋𝐨𝐯𝐞 𝐌𝐞..?👀** ",
           " **புது அறிவுகள் மகிழ்ச்சியுடன் வருகின்றன! 🧠💡🙉** ",
           " **உங்கள் நண்பர்களுக்கு இனிய பண்டிகை நலம்! 🎊** ",
           "சந்தோஷமாக இருக்கும் விளைவிகள் காண்க! 🎉 இப்போது என் அன்பு உங்கள் மகளிர் மற்றும் மகனருக்கு சேருகின்றேன்! @daughtersandsons** ",
           "இன்ஸ்தக்ராம ஹோ..??🙃",
            "இன்ஸ்தக்ராம ஹோ..??🙃",   
           "வாட்ஸாப் நும்பர் டோகே ?😕",
            "தும்மி கோன ச முசிக் ?🙃",
             "சரா கம் கதம் ஹோ கியா ஆப்கா..?🙃",
              "காஹா சே ஹோ ஆப்க😊",
            "சுனோ நா🧐",
          "மேரா எக் காம் கதம் டோகே..?",
            "பை தட் கர்னா அஜ் கே பாத்😠",
       "மொம் தத் கைச ஹைன்..?❤",
       "கியா ஹூ..?👱",
       "போஹோத் யா ரி ஹை 🤧❣️",
        "போஹோ க்யே முஜ்ஹே😏😏",
        "ஜுத் நி போல்நா ச ஹியே🤐",
        "காஹா லோ பா மத் கிரோ பாத😒",
        "கியா ஹூ😮😮",
        "ஹீ👀",
        "ஆப்கே ஜைசா டோ ஸத் மே பேர் கும் கே பாத் கும் 🙈",
        "ஆஜ மேக் சத் ஹூ ☹️",
        "முஸ்ஜிஸ் பத் பீ பாத் கும் நா 🥺🥺",
        "கியா கர் ராஹே ஹோ👀",
        "கியா ஹால் சால் ஹை 🙂",
           "கியா சே ஹோ ஆப்க..?🤔",
        "சத்திங் கார் கும் நா..🥺",
           "மே மாசூம் ஹூ நா🥺🥺",
           "கால் மாஜா அய தா நா🤭😅",
           "க்ரூப் மே பாத் கும் நாஹி கர்தே ஹோ😕",
           "ஆப் ரிலேட்ஸ்ஹிப் மே ஹை..?👀",
           "கிட்னா சாப் ராத் ஹை👿",
           "ஆப்கோ கன கனே ஆட்க்க ஹை ஹோ😸",
           "கம்னி சொல்க் மே..??🙈",
           "கியா ஹூச் ரா க்கொ ✌️🤞",
           "ஆப்கோ கன கனே ஆட்க்க ஹை ஹோ😸",
           "**கம்னி சொல்க் மே..??🙈**",
           "**கியா ஹூச் ரா க்கொ ✌️🤞**",
           "இனிமையான கோபம், இனிய குரல், இசையும் முகமும் போன்றே தொடங்குகிறாய்",
           "**உயிர் என்று பேசும் அழகுதான், உன் கண்கள் என்று பார்க்கும் பார்வையில் - உயிரே உயிரே**",
           "**அன்புடன் சேர்ந்து வாழும் சிறுவர்களுக்கு வணக்கம்! 🤗 அவர்களுக்குக் கையேடு செய்யவேண்டும்! @kids**",
           "**சந்தோஷமாக இருக்கும் விளைவிகள் காண்க! 🎉 இப்போது என் அன்பு உங்கள் மகளிர் மற்றும் மகனருக்கு சேருகின்றேன்! @daughtersandsons 😉** ",
           "**இந்த குழு ஒரு குடும்பம் போல இருக்கின்றது! 👨‍👩‍👧‍👦 அனைவருக்கும் வணக்கம்! @kudumbam**",
           "**𝐇𝐞𝐥𝐨𝐨🧐**",
           " **நேரம் வந்தது எப்படி நிறைவு! 🕰️ நாம் அனைவருக்கும் பட்டியலில் இருக்கின்றோம்! @all🥺**",
           " **𝐘𝐚𝐡𝐚 𝐀𝐚 𝐉𝐚𝐨:- [ @miiakhalifamusic_support ] 𝐌𝐚𝐬𝐭𝐢 𝐊𝐚𝐫𝐞𝐧𝐠𝐞 🤭🤭** ",
           " **𝐓𝐫𝐮𝐭𝐡 𝐀𝐧𝐝 𝐃𝐚𝐫𝐞 ? 😊** ",
           " **𝐀𝐣 𝐌𝐮𝐦𝐦𝐲  𝐃𝐚𝐭𝐚 𝐘𝐫🥺🥺** ",
           " **𝐉𝐨𝐢𝐧 𝐊𝐚𝐫o:- [ @miiakhalifamusic_support ]🤗** ",
           " **𝐄𝐤 𝐃𝐢𝐥 𝐇𝐚𝐢 𝐄𝐤 𝐃𝐢𝐥 𝐇𝐢 𝐓𝐨 𝐇𝐚𝐢😗😗** ",
           " **மகிழ்ச்சி மறக்க வேண்டாம்! 😃 இன்னும் பல செய்திகள் உள்ளன, காணுங்கள். @everyone** ",
           " **𝐌𝐲 𝐂𝐮𝐭𝐞 𝐎𝐰𝐧𝐞𝐫 [ @Kumargk_0007 ]🥰** ",
           " **அனைவருக்கும் வணக்கம்! 🙏🌟 உங்கள் அரங்கே எப்போதும் சேருகிறேன்! ** ",
           " **𝐆𝐨𝐨𝐝 𝐍8 ** ",
           ]

@app.on_message(filters.command(["mention", "all", "tagmember"], prefixes=["/", "@", "#"]))
async def mentionall(client, message):
    chat_id = message.chat.id
    if message.chat.type == "private":
        return await message.reply("This command can be used in groups and channels!")

    is_admin = False
    try:
        participant = await client.get_chat_member(chat_id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in ("administrator", "creator"):
            is_admin = True
    if not is_admin:
        return await message.reply("Only admin can use this command!")

    if message.reply_to_message and message.text:
        return await message.reply("/tagall hello 👈 Try this next time for tagging..")
    elif message.text:
        mode = "text_on_cmd"
        msg = message.text
    elif message.reply_to_message:
        mode = "text_on_reply"
        msg = message.reply_to_message
        if not msg:
            return await message.reply("/tagall hii 👈 Try this or reply any message...")
    else:
        return await message.reply("/tagall hii 👈 Try this or reply any message...")

    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_chat_members(chat_id):
        if not chat_id in spam_chats:
            break
        if usr.user.is_bot:
            continue
        usrnum += 1
        usrtxt += f"[{usr.user.first_name}](tg://user?id={usr.user.id}) "

        if usrnum == 5:
            if mode == "text_on_cmd":
                txt = f"{usrtxt} {random.choice(TAGSRT)}"
                await client.send_message(chat_id, txt)
            elif mode == "text_on_reply":
                await msg.reply(f"[{random.choice(EMOJI)}](tg://user?id={usr.user.id})")
            await asyncio.sleep(5)
            usrnum = 0
            usrtxt = ""
    try:
        spam_chats.remove(chat_id)
    except:
        pass

@app.on_message(filters.command(["cancel", "stop"]))
async def cancel_spam(client, message):
    if not message.chat.id in spam_chats:
        return await message.reply("No active mention process is started by me.")
    is_admin = False
    try:
        participant = await client.get_chat_member(message.chat.id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in ("administrator", "creator"):
            is_admin = True
    if not is_admin:
        return await message.reply("This command is only for admins. You can't use this command.")
    else:
        try:
            spam_chats.remove(message.chat.id)
        except:
            pass
        return await message.reply("♦ Mention process stopped ♦")