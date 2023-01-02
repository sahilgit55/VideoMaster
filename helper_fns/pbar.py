from asyncio import sleep as asynciosleep
from pyrogram.errors import FloodWait
from helper_fns.helper import hrb, getbotuptime, Timer, timex, get_readable_time
from helper_fns.process import get_sub_process, get_master_process



def get_progress_bar_string(current,total):
    completed = int(current) / 8
    total = int(total) / 8
    p = 0 if total == 0 else round(completed * 100 / total)
    p = min(max(p, 0), 100)
    cFull = p // 6
    p_str = '■' * cFull
    p_str += '□' * (16 - cFull)
    p_str = f"[{p_str}]"
    return p_str

timer = Timer(7)

async def progress_bar(current,total,reply,start, client, subprocess_id, process_id, *datam):
      if process_id not in get_master_process():
        client.stop_transmission()
      if subprocess_id not in get_sub_process():
        client.stop_transmission()
      if timer.can_send():
        now = timex()
        diff = now - start
        if diff < 1:
            return
        else:
            perc = f"{current * 100 / total:.1f}%"
            elapsed_time = round(diff)
            speed = current / elapsed_time
            sp=str(hrb(speed))+"ps"
            tot=hrb(total)
            cur=hrb(current)
            progress = get_progress_bar_string(current,total)
            try:
                name = datam[0]
                opt = datam[1]
                remnx = datam[2]
                ptype = datam[3]
                ps = datam[4]
                stime = datam[5]
                mtime = datam[6]
                sptime = get_readable_time(timex() - stime)
                mptime = get_readable_time(timex() - mtime)
                botupt = getbotuptime()
                ctext = f"⛔Skip Video: `/cancel sp {str(subprocess_id)}`"
                ptext = f"🔴Cancel Task: `/cancel mp {str(process_id)}`"
                pro_bar = f"{str(ptype)} ({opt})\n🎟️File: {name}\n🧶Remaining: {str(remnx)}\n\n\n {str(progress)}\n\n ┌ 𝙿𝚛𝚘𝚐𝚛𝚎𝚜𝚜:【 {perc} 】\n ├ 𝚂𝚙𝚎𝚎𝚍:【 {sp} 】\n ├ {ps}:【 {cur} 】\n └ 𝚂𝚒𝚣𝚎:【 {tot} 】\n\n\n🔸Sp Time: {str(sptime)}\n🔹Mp Time: {str(mptime)}\n♥️Bot Uptime: {str(botupt)}\n{str(ctext)}\n{str(ptext)}"
                await reply.edit(pro_bar)
            
            except FloodWait as e:
                    await asynciosleep(int(e.value)+10)
            except Exception as e:
                    print(e)
