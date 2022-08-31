@dominator_cmd(
    pattern="hey$",
    info={
        "header": "Just a art command try out yourself to see",
        "usage": "{tr}hey",
    },
)
async def viello(event):
    "fun art command"
    reply_to_id = await reply_id(event)
    event = await eor(event, "**(❛ Hi ❜!**")
    HELL_PIC = "https://te.legra.ph/file/b86eff074051b0b2d4513.jpg"
    K_PIC = "https://te.legra.ph/file/a679e3d061ac6b349cd60.jpg"
    L_PIC = "https://te.legra.ph/file/96c2b61d6361f112ceac5.jpg"
    M_PIC = "https://te.legra.ph/file/4d0c641e085f7ed15dfec.jpg"
    if HELL_PIC:
        HELLO = f"╔┓┏╦━╦┓╔┓╔━━╗\n"
        HELLO += f"║┗┛║┗╣┃║┃║X X ║\n"
        HELLO += f"║┏┓║┏╣┗╣┗╣╰╯║\n"
        HELLO += f"╚┛┗╩━╩━╩━╩━━╝\n"
        on = await event.client.send_file(
            event.chat_id, file=HELL_PIC, caption=HELLO, reply_to=reply_to_id
        )
        await asyncio.sleep(3)
        ok = await event.client.edit_message(event.chat_id, on, file=K_PIC)
        await asyncio.sleep(3)
        ok1 = await event.client.edit_message(event.chat_id, on, file=L_PIC)
        await asyncio.sleep(3)
        ok2 = await event.client.edit_message(event.chat_id, ok1, file=M_PIC)
        await asyncio.sleep(5)
        ok3 = await event.client.edit_message(event.chat_id, ok2, file=L_PIC)
        await asyncio.sleep(5)
        ok4 = await event.client.edit_message(event.chat_id, ok3, file=K_PIC)
        await asyncio.sleep(5)
        ok5 = await event.client.edit_message(event.chat_id, ok4, file=HELL_PIC)
        await event.delete(0)
