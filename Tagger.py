import random, os, logging, asyncio
from telethon import Button
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.types import ChannelParticipantsAdmins

logging.basicConfig(
    level=logging.INFO,
    format='%(name)s - [%(levelname)s] - %(message)s'
)
LOGGER = logging.getLogger(__name__)

api_id = int(os.environ.get("APP_ID"))
api_hash = os.environ.get("API_HASH")
bot_token = os.environ.get("TOKEN")
client = TelegramClient('client', api_id, api_hash).start(bot_token=bot_token)



anlik_calisan = []

tekli_calisan = []





# BAŞLANĞIC BUTONU

@client.on(events.NewMessage(pattern="^/start$"))
async def start(event):
  await event.reply("**⚡ Dizzy Tagger Bot**İlə Qrupunuzdakı Üyələri Etiket Edə Bilərəm.\nℹ Mənim Qruplarda Asan Və Sürətli İşləyə Bilməyim Üçün Mənə Qrupunuzda Sadə Adminlik Vermənizi Rica Edirem.\n✔ Əmrlərlə Tanış Olmaq Üçün __ƏMRLƏR__ Butonuna Toxun",
                    buttons=(
                   
		      [Button.url('➕ Botu Qrupa Al ➕', 'https://t.me/Dizzytaggerbot?startgroup=a')],
                      [Button.url('🤖 DİGƏR BOTLARIM', 'https://t.me/DizzyBots')],
		      [Button.url('🇦🇿 OWNER 👨🏻‍💻', 'https://t.me/ThisisFrep')],
		      [Button.inline("⚙ ƏMRLƏR", data="help")],
		    ),
                    link_preview=False
                   )

@client.on(events.callbackquery.CallbackQuery(data="start"))
async def handler(event):
    await event.edit(f"**⚡ Dizzy Tagger Bot**İlə Qrupunuzdakı Üyələri Etiket Edə Bilərəm.\nℹ Mənim Qruplarda Asan Və Sürətli İşləyə Bilməyim Üçün Mənə Qrupunuzda Sadə Adminlik Vermənizi Rica Edirem\n✔ Əmrlərlə Tanış Olmaq Üçün __ƏMRLƏR__ Butonuna Toxun", buttons=(
                      
                      [Button.url('➕ Botu Qrupa Al ➕', 'https://t.me/Dizzytaggerbot?startgroup=a')],
                      [Button.url('🤖 DİGƏR BOTLARIM', f'https://t.me/DizzyBots')],
                      [Button.url('🇦🇿 OWNER 👨‍💻', f'https://t.me/ThisisFrep')],
                      [Button.inline("⚙ ƏMRLƏR", data="help")],
                    ),
                    link_preview=False)

			     
@client.on(events.callbackquery.CallbackQuery(data="help"))
async def handler(event):
    await event.edit(f"⚡ Dizzy Tagger Botunun Əmrləri **\n\n**/tag <səbəb> - 7-li Tağ Edər**\n\n**/etag <səbəb> - Emoji İlə Tağ Edər**\n\n**/btag <səbəb> - Bayraqlarla Tağ Edər**\n\n**/mtag <səbəb> 7 - Li Mafia Rolları İlı Tağ Edər**\n\n**/rtag <səbəb> 7 - Li Rayon Və Şəhər Adları İlə Tağ Edər**\n\n**/tektag <səbəb> - Tək Teək Tağ Edər**\n\n**/admins <səbəb> - Adminləri Tağ Edər**\n\n**/cancel - Tağ Prosesin Saxlayar\n\n**/start - Botu Başladar**", buttons=(
                      [Button.url('➕ Botu Qrupa Al ➕', 'https://t.me/Dizzytaggerbot?startgroup=a')],
	              [Button.inline("ℹ İNFO", data="info")],
                      [Button.inline("🗑 Bağla", data="start")],
                    ),
                    link_preview=False)


@client.on(events.callbackquery.CallbackQuery(data="info"))
async def handler(event):
    await event.edit(f"**Çox Özəllikli Tağ Botu Axtarmağa Çalışan Qrub Sahibləri  ⚡Dizzy Tagger Bot Sizə Görə:\n\n📌 7-Li Tağ\n📌 Emojilərlə Tağ Edər\n📌 Bayraqlarla Tağ Edər\n📌 Mafia Rolları İlə Tağ Edər\n📌 Rayon Və Şəhər Adları İlə Tağ Edər\n📌 Təkli Tağ\n📌 Yalnız Admimləri Tağ\n\n\nBelə Çox Özəllikli @Flashtaggerbot 'u Qrupunuza Yönətici Olaraq Alıb Rahatlıqla , Tağ edə bilirsiz\n📢 ADMİNLİK MÜTLƏQDİ**", buttons=(      
	              [Button.url('➕ Botu Qruba Al ➕', 'https://t.me/Flashtaggerbot?startgroup=a')],
		      [Button.inline("⚙ Əsas Meynu", data="start")],
		    ),
                    link_preview=False)
   
	
	



	
	
	
	

@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)


	
emoji = "🐵 🦁 🐯 🐱 🐶 🐺 🐻 🐨 🐼 🐹 🐭 🐰 🦊 🦝 🐮 🐷 🐽 🐗 🦓 🦄 🐴 🐸 🐲 🦎 🐉 🦖 🦕 🐢 🐊 🐍 🐁 🐀 🐇 🐈 🐩 🐕 🦮 🐕‍🦺 🐅 🐆 🐎 🐖 🐄 🐂 🐃 🐏 🐑 🐐 🦌 🦙 🦥 🦘 🐘 🦏 🦛 🦒 🐒 🦍 🦧 🐪 🐫 🐿️ 🦨 🦡 🦔 🦦 🦇 🐓 🐔 🐣 🐤 🐥 🐦 🦉 🦅 🦜 🕊️ 🦢 🦩 🦚 🦃 🦆 🐧🦈 🐬 🐋 🐳 🐟 🐠 🐡 🦐 🦞 🦀 🦑 🐙 🦪 🦂 🕷️ 🦋 🐞 🐝 🦟 🦗 🐜 🐌 🐚 🕸️ 🐛 🐾 😀 😃 😄 😁 😆 😅 😂 🤣 😭 😗 😙 😚 😘 🥰 😍 🤩 🥳 🤗 🙃 🙂 ☺️ 😊 😏 😌 😉 🤭 😶 😐 😑 😔 😋 😛 😝 😜 🤪 🤔 🤨 🧐 🙄 😒 😤 😠 🤬 ☹️ 🙁 😕 😟 🥺 😳 😬 🤐 🤫 😰 😨 😧 😦 😮 😯 😲 😱 🤯 😢 😥 😓 😞 😖 😣 😩 😫 🤤 🥱 😴 😪 🌛 🌜 🌚 🌝 🌞 🤢 🤮 🤧 🤒 🍓 🍒 🍎 🍉 🍑 🍊 🥭 🍍 🍌 🌶 🍇 🥝 🍐 🍏 🍈 🍋 🍄 🥕 🍠 🧅 🌽 🥦 🥒 🥬 🥑 🥯 🥖 🥐 🍞 🥜 🌰 🥔 🧄 🍆 🧇 🥞 🥚 🧀 🥓 🥩 🍗 🍖 🥙 🌯 🌮 🍕 🍟 🥨 🥪 🌭 🍔 🧆 🥘 🍝 🥫 🥣 🥗 🍲 🍛 🍜 🍢 🥟 🍱 🍚 🥡 🍤 🍣 🦞 🦪 🍘 🍡 🥠 🥮 🍧 🍧 🍨".split(" ")


@client.on(events.NewMessage(pattern="^/etag ?(.*)"))
async def mentionall(event):
  global anlik_calisan
  if event.is_private:
    return await event.respond("**Bu Əmr Yanlız Qruplar Və Kanallar Da İsdifadə Edilə Bilər ❗**")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**Bu Əmri sadacə Adminlər İsdifadə Edə Bilər 〽️**")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("**❌ Keçmiş Mesajlar Üçin Tağ Edə Bilmirəm **")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("Tağ Eləmək Üçün Bir Səbəb yox❗️")
  else:
    return await event.respond("**📢 Tağ ı Başlatmaq Üçün Bir Səbəb Yazın...!**")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{random.choice(emoji)}](tg://user?id={usr.id}) - "
      if event.chat_id not in anlik_calisan:
        await event.respond("**✅ Tağ Prosesi Uğurla Durduruldu**")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, f"{usrtxt}\n\n{msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
  
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{random.choice(emoji)}](tg://user?id={usr.id}) - "
      if event.chat_id not in anlik_calisan:
        await event.respond("✅ Proses Uğurla Durduruldu\n\n**📢 Burda Sizin Reklamınız Ola Bilər\n☎️ Əlaqə:- @ThisisFrep**")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""


@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)	

	

	
bay = "🏁 🚩 🏴 🏳 🏳️‍🌈 🏴‍☠️ 🇦🇨 🇦🇱 🇦🇮 🇦🇬 🇦🇫 🇦🇪🇦🇩 🇦🇼 🇦🇺 🇦🇹 🇦🇸 🇦🇷 🇦🇶 🇦🇴 🇧🇫 🇧🇪 🇧🇩 🇧🇧🇦🇿 🇦🇽 🇧🇳 🇧🇲 🇧🇱 🇧🇯 🇧🇮 🇧🇭 🇧🇬 🇧🇼 🇧🇻 🇧🇹 🇧🇸 🇧🇷 🇧🇶 🇧🇴 🇨🇬 🇨🇫 🇨🇩 🇨🇨 🇨🇦 🇧🇿 🇧🇾 🇨🇳 🇨🇲 🇨🇱 🇨🇰 🇨🇮 🇨🇭 🇨🇾 🇨🇽 🇨🇼 🇨🇻 🇨🇺 🇨🇷 🇨🇵 🇩🇴 🇩🇲 🇩🇰 🇩🇯 🇩🇬 🇩🇪 🇨🇿 🇪🇷 🇪🇭 🇪🇬 🇪🇪 🇪🇨 🇪🇦 🇩🇿 🇫🇲 🇫🇰 🇫🇯 🇫🇮 🇪🇺 🇪🇹 🇪🇸 🇬🇫 🇬🇪 🇬🇩 🇬🇧 🇬🇦 🇫🇷 🇫🇴 🇬🇵 🇬🇳 🇬🇲 🇬🇱 🇬🇮 🇬🇭 🇬🇬 🇬🇾 🇬🇼 🇬🇺 🇬🇹 🇬🇸 🇬🇷 🇬🇶 🇮🇨 🇭🇺 🇭🇹 🇭🇷 🇭🇳 🇭🇲 🇭🇰 🇮🇶 🇮🇴 🇮🇳  🇮🇱 🇮🇪 🇮🇩 🇯🇵 🇯🇴 🇯🇲 🇯🇪 🇮🇹 🇮🇸 🇮🇷 🇰🇵 🇰🇳 🇰🇲 🇰🇮 🇰🇭 🇰🇬 🇰🇪 🇱🇨 🇱🇧 🇱🇦 🇰🇿 🇰🇾 🇰🇼 🇰🇷 🇱🇻 🇱🇺 🇱🇹 🇱🇸 🇱🇷 🇱🇰 🇱🇮 🇲🇬 🇲🇫 🇲🇪 🇲🇩 🇲🇨 🇲🇦 🇱🇾 🇲🇵 🇲🇴 🇲🇳 🇲🇲 🇲🇱 🇲🇰 🇲🇭 🇲🇼 🇲🇻 🇲🇺 🇲🇹 🇲🇸 🇲🇷 🇲🇶 🇳🇫 🇳🇺 🇵🇭 🇵🇹 🇷🇺 🇷🇸 🇵🇸 🇵🇬 🇳🇷 🇳🇪 🇳🇨 🇳🇵🇵🇫 🇵🇷 🇷🇴 🇷🇪 🇵🇳 🇵🇪 🇳🇴 🇳🇦 🇶🇦 🇵🇲 🇵🇦 🇳🇱 🇲🇿 🇵🇾 🇵🇱 🇴🇲 🇳🇮 🇲🇾 🇲🇽 🇳🇬 🇳🇿 🇵🇰 🇵🇼 🇸🇬 🇸🇳 🇸🇾 🇹🇭 🇹🇷 🇹🇴 🇹🇬 🇸🇽 🇸🇲 🇸🇪 🇸🇩 🇸🇱 🇸🇻 🇹🇫 🇹🇳 🇹🇲 🇹🇩 🇸🇹 🇸🇰 🇸🇨 🇸🇧 🇸🇯 🇸🇸 🇹🇨 🇹🇱 🇹🇰 🇹🇦 🇸🇷 🇸🇮 🇸🇦 🇷🇼 🇸🇭 🇸🇿 🇹🇯 🇺🇲 🇽🇰 🏴󠁧󠁢󠁳󠁣󠁴󠁿 🏴󠁧󠁢󠁥󠁮󠁧󠁿 🇼🇸 🇻🇨 🇺🇬 🇺🇦 🇻🇦 🇼🇫 🇿🇼 🇿🇲 🇻🇺 🇺🇿 🇹🇿 🇹🇼 🇺🇾 🇻🇳 🇿🇦 🇾🇹 🇻🇮 🇺🇸 🇹🇻 🏴󠁧󠁢󠁷󠁬󠁳󠁿 🇾🇪 🇻🇬 🇺🇳".split(" ")
	
@client.on(events.NewMessage(pattern="^/btag ?(.*)"))
async def mentionall(event):
  global anlik_calisan
  if event.is_private:
    return await event.respond("**Bu Əmr Yanlız Qruplar Və Kanallar Da İsdifadə Edilə Bilər ❗**")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**Bu Əmri sadacə Adminlər İsdifadə Edə Bilər 〽️**")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("**❌ Keçmiş Mesajlar Üçin Tağ Edə Bilmirəm **")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("Tağ Eləmək Üçün Bir Səbəb yox❗️")
  else:
    return await event.respond("**📢 Tağ ı Başlatmaq Üçün Bir Səbəb Yazın...!**")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{random.choice(bay)}](tg://user?id={usr.id}) - "
      if event.chat_id not in anlik_calisan:
        await event.respond("**✅ Tağ Prosesi Uğurla Durduruldu**")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, f"{usrtxt}\n\n{msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
  
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{random.choice(bay)}](tg://user?id={usr.id}) - "
      if event.chat_id not in anlik_calisan:
        await event.respond("✅ Proses Uğurla Durduruldu\n\n**📢 Burda Sizin Reklamınız Ola Bilər\n☎️ Əlaqə:- @ThisisFrep**")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""


@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)	
	
	
	
	
mafia = "👨‍🌾Vətəndaş 👨‍✈️Komissar Kattani 👨‍💼Çavuş 👨‍⚕️Doktor 🧟‍♀️Cadugar 🕵️Suiqəstçi 🧔Bomj 🦎Buqələmun 💂🏻Securıty 👳🏻‍♂️Satıcı 🙇🏻‍♂️Oğru 👷🏻‍♂️Mədənçi ⭐️General 🧝🏻‍♀️Şəhzadə 🎧DJ 🏦Bankir 🕴Don 🕺Mafia 👨‍⚖️Vəkil 🙍🏻‍♂️Məhbus 👨🏻‍🦱Dedektiv 🦦Köstəbək 👨🏻‍🎤Specialist 🔪Manyak 🤡Joker 👻Ruh 🧚🏻‍♀️Mələk 🦹🏻‍♂️BOSS 🥷Ninja 🥷SUPER Ninja 👨🏻‍🦲Dəli 🔮Reviver 💂Killer 🧛🏻‍♂️Vampir󠁧󠁢󠁷󠁬󠁳󠁿󠁧󠁢󠁷󠁬󠁳󠁿".split(" ")	

@client.on(events.NewMessage(pattern="^/mtag ?(.*)"))
async def mentionall(event):
  global anlik_calisan
  if event.is_private:
    return await event.respond("**Bu Əmr Yanlız Qruplar Və Kanallar Da İsdifadə Edilə Bilər ❗**")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**Bu Əmri sadacə Adminlər İsdifadə Edə Bilər 〽️**")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("**❌ Keçmiş Mesajlar Üçin Tağ Edə Bilmirəm **")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("Tağ Eləmək Üçün Bir Səbəb yox❗️")
  else:
    return await event.respond("**📢 Tağ ı Başlatmaq Üçün Bir Səbəb Yazın...!**")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"➢ [{random.choice(mafia)}](tg://user?id={usr.id}) \n"
      if event.chat_id not in anlik_calisan:
        await event.respond("**✅ Tağ Prosesi Uğurla Durduruldu**")
        return
      if usrnum == 7:
        await client.send_message(event.chat_id, f"{usrtxt}\n\n{msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
  
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"➢ [{random.choice(mafia)}](tg://user?id={usr.id}) \n"
      if event.chat_id not in anlik_calisan:
        await event.respond("✅ Proses Uğurla Durduruldu\n\n**📢 Burda Sizin Reklamınız Ola Bilər\n☎️ Əlaqə:- @ThisisFrep**")
        return
      if usrnum == 7:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
    

@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)
	
	
rayon = "Ağcabədi Ağdam Ağdaş Ağdərə Ağıstafa Ağsu Astara Babək Bakı Balakən Beyləqan Bərdə Biləsuvar Cəbrayıl Cəlilabad Culfa Daşkəsən Dəliməmmədli Xocalı Füzuli Gədəbəy Gəncə Goranboy Göyçay Göygöl Göytəpə Hacıqabul Horadiz Xaçmaz Xankəndi Xocalı Xocavənd Xırdalan Xızı Xudat İmişli İsmayıllı Kəlbəcər Kürdəmir Qax Qazax Qəbələ Qobustan Qovlar Quba Qubadlı Qusar Laçın Lerik Lənkəran Liman Masallı Naftalan Naxçıvan Neftçala Oğuz Ordubad Saatlı Sabirabad Salyan Samux Siyəzən Sumqayıt Şuşa Şabran Şahbuz Şamaxı Şəki Şəmkir Şərur Şirvan Tərtər Tovuz Ucar Yardımlı Yevlax Zaqatala Zəngilan Zərdab󠁧󠁢󠁷󠁬󠁳󠁿󠁧󠁢󠁷󠁬󠁳󠁿".split(" ")
@client.on(events.NewMessage(pattern="^/rtag ?(.*)"))
async def mentionall(event):
  global anlik_calisan
  if event.is_private:
    return await event.respond("**Bu Əmr Yanlız Qruplar Və Kanallar Da İsdifadə Edilə Bilər ❗**")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**Bu Əmri sadacə Adminlər İsdifadə Edə Bilər 〽️**")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("**❌ Keçmiş Mesajlar Üçin Tağ Edə Bilmirəm **")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("Tağ Eləmək Üçün Bir Səbəb yox❗️")
  else:
    return await event.respond("**📢 Tağ ı Başlatmaq Üçün Bir Səbəb Yazın...!**")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"➢ [{random.choice(rayon)}](tg://user?id={usr.id}) \n"
      if event.chat_id not in anlik_calisan:
        await event.respond("**✅ Tağ Prosesi Uğurla Durduruldu**")
        return
      if usrnum == 7:
        await client.send_message(event.chat_id, f"{usrtxt}\n\n{msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
  
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"➢ [{random.choice(rayon)}](tg://user?id={usr.id}) \n"
      if event.chat_id not in anlik_calisan:
        await event.respond("✅ Proses Uğurla Durduruldu\n\n**📢 Burda Sizin Reklamınız Ola Bilər\n☎️ Əlaqə:- @ThisisFrep**")
        return
      if usrnum == 7:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
    	
	
	
	
	
	
	
	
	
@client.on(events.NewMessage(pattern="^/tag ?(.*)"))
async def mentionall(event):
  global anlik_calisan
  if event.is_private:
    return await event.respond("Bu Əmr Yanlız Qruplar Və Kanallar Da İsdifadə Edilə Bilər ❗️**")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**Bu Əmri Yanlız Adminlər İsdifadə Edə Bilər 〽️**")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("ℹ Əvvəlki Mesajlara Cavab Verməyin")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("Prosesi Başlatmaq Üçün Səbəb yoxdur ❗️")
  else:
    return await event.respond("❌ Tağ Edmək Üçün Səbəb Yox ")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"➢ [{usr.first_name}](tg://user?id={usr.id}) \n"
      if event.chat_id not in anlik_calisan:
        await event.respond("✅ Proses Uğurla Durduruldu**\n\n📢 Burda Sizin Reklamınız Ola Bilər\n\n☎️ Əlaqə:- @ThisisFrep**")
        return
      if usrnum == 7:
        await client.send_message(event.chat_id, f"{usrtxt}\n\n{msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
  
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"➢ [{usr.first_name}](tg://user?id={usr.id}) \n"
      if event.chat_id not in anlik_calisan:
        await event.respond("**✅ Proses Uğurla Sonlandırıldı**")
        return
      if usrnum == 7:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""

@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)
	

@client.on(events.NewMessage(pattern="^/tektag ?(.*)"))
async def mentionall(event):
  global tekli_calisan
  if event.is_private:
    return await event.respond("**Bu Əmr Yanlız Qruplar Və Kanallar Da İsdifadə Edilə Bilər ❗️**")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**Bu Əmri Sadacə Arminlər İadifadə Edə Bilər 〽**")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("**❌ Əvvəlki Mesajı Tağ Edə Bilmərəm*")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("Başlamaq Üçün Səbəb Yazın❗️")
  else:
    return await event.respond("**ℹ Prosesə Başlamağım Üçün səbəb Yazın..**")
  
  if mode == "text_on_cmd":
    tekli_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"**➢ [{usr.first_name}](tg://user?id={usr.id}) \n**"
      if event.chat_id not in tekli_calisan: 
        await event.respond("**✅ Proses Uğurla Durduruldu\n\n**\n\n📢 Burda Sizin Reklamınız Ola Bilər\n☎️ Əlaqə:- @ThisisFrep****")
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, f"{usrtxt} {msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
  
  if mode == "text_on_reply":
    tekli_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"➢ [{usr.first_name}](tg://user?id={usr.id}) \n"
      if event.chat_id not in tekli_calisan:
        await event.respond("✅ Proses Uğirla Durduruldu\n\n**📢 Burda Sizin Reklamınlz Ola Bilər\n☎️ Əlaqə:- @ThisisFrep**")
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""

@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
  global tekli_calisan
  tekli_calisan.remove(event.chat_id)
	
	

@client.on(events.NewMessage(pattern="^/admins ?(.*)"))
async def mentionall(tagadmin):

	if tagadmin.pattern_match.group(1):
		seasons = tagadmin.pattern_match.group(1)
	else:
		seasons = ""

	chat = await tagadmin.get_input_chat()
	a_=0
	await tagadmin.delete()
	async for i in client.iter_participants(chat, filter=cp):
		if a_ == 500:
			break
		a_+=1
		await tagadmin.client.send_message(tagadmin.chat_id, "**[{}](tg://user?id={}) {}**".format(i.first_name, i.id, seasons))
		sleep(0.5)

				
		

		
@client.on(events.NewMessage(pattern="^/gtag ?(.*)"))
async def mentionalladmin(event):
  global gece_tag
  if event.is_private:
    return await event.respond(f"{noqrup}")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond(f"{noadmin}")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("__Köhnə mesajları görə bilmirəm! (bu mesaj məni qrupa əlavə etməmişdən qabaq yazılıb)__")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("__Tağ mesajı yazmadın!__")
  else:
    return await event.respond("__Tağ etməy üçün bir mesaj yanıtlayın və ya bir mətn yazın!__")
    
  if mode == "text_on_cmd":
    await client.send_message(event.chat_id, "❄️ Admin tağ başladı\n⏱️ İnterval - 2 saniyə",
                    buttons=(
                      [
                       Button.url('📣 Support', f'https://t.me/{support}')
                      ]
                    )
                  ) 
    gece_tag.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{usr.first_name}](tg://user?id={usr.id}) "
      if event.chat_id not in gece_tag:
        await event.respond("⛔ Admin Tağ Prosesi Dayandırıldı",
                    buttons=(
                      [
                       Button.url('📣 Support', f'https://t.me/{support}')
                      ]
                    )
                  )
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, f"{usrtxt} {msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
 		
		
		

		
		
		

print(">> Bot Uğurla İşləyir. Narahat olma 🚀 @ThisisFrep dən məlumat ala bilırsən<<")
client.run_until_disconnected()
