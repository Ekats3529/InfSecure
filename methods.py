import sys


def put_message(message_path, container_path, stego_path):
    if message_path is None:
        msg = sys.stdin.buffer.read()
    else:
        with open(message_path, "rb") as file_msg:
            msg = file_msg.read()

    with open(container_path, 'r') as file_con:
        text = [line.rstrip() for line in file_con.readlines()]

    result = []
    bin_msg = str(bin(int(msg.hex(), 16)))[2::]
    #print(bin_msg, text)
    for i in range(len(bin_msg)):
        cur = text[i] if i < len(text) else ""
        cur += " " if bin_msg[i] == "1" else ""
        result.append(cur)

    result = "\n".join(result)

    if stego_path is None:
        sys.stdout.write(result)
    else:
        with open(stego_path, "w") as file_stego:
            file_stego.write(result + "\n")


def get_message(message_path, stego_path):
    if message_path is None:
        msg = sys.stdin.buffer.read()
    else:
        with open(stego_path, "r") as file_stego:
            text = [line[:-1:] for line in file_stego.readlines()]

    bin_text = ""

    print(text)
    for i in range(len(text)):
        bin_text += "1" if text[i].endswith(" ") else "0"

    result = ""

    for k in range((len(text) + 1) // 8):
        cur_byte = bin_text[8 * k: (8 * (k + 1)):]
        result += f"{str(hex(int(cur_byte, 2)))[1::]}"

    print(result)
    print(bytes(result, "UTF-8"))
    if stego_path is None:
        sys.stdout.write(result)
    else:
        with open(message_path, "wb") as file_msg:
            file_msg.write(result)
