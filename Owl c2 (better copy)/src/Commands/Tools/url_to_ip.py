import socket, time

def url_to_ip(args, send, client):
    from src.cnc import gradientText

    try:
        url = ""
        if len(args) == 2:
            url = args[1]
            host = str(url).replace("https://", "").replace("http://", "").replace("www.", "")
            ip = socket.gethostbyname(host)
            time.sleep(0.2)
            DATA_TEXT = f'\nURL {url} | IP {ip}\n'
            send(client, gradientText(DATA_TEXT, (147, 103, 176), (189, 174, 199)))
        else:
            send(client, gradientText('\n!GETIP [URL]\n', (147, 103, 176), (189, 174, 199)))
    except socket.gaierror:
        send(client, gradientText('\nInvalid website\n', (255,0,0), (255,100,100)))