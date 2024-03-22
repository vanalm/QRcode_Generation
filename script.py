import segno





link = 'https://youtu.be/b89Px7C18aw?si=g3I03LAq-QjW3Od9'
filename = 'qrcode_shindaiwawhacker.png'


qrcode = segno.make(link)
# qrcode_rotated = qrcode.to_pil().rotate(45)

# ## Formatted QR Code
# qrcode_rotated = qrcode.to_pil(
#     scale=5,
#     light="lightblue",
#     dark="green",
# ).rotate(45, expand=True)
# qrcode_rotated.save("formatted_rotated_qrcode.png")


## Basic QR Code
qrcode.save(
    filename,
    scale=2.5,
    # boarder=10, 
    # light="lightblue",
    # dark="darblue",
    # quiet_zone="maroon",
    # data_dark="green",
    # data_light="lightgreen",


)
def get_basic_qr(link, scale=10, filename="qrcode.png"):
    qrcode = segno.make(link)
    qrcode.save(
        filename,
        scale=10,
    )
    return qrcode

# from urllib.request import urlopen

# slts_qrcode = segno.make_qr("https://www.youtube.com/watch?v=hTWKbfoikeg")
# nirvana_url = urlopen("https://media.giphy.com/media/LpwBqCorPvZC0/giphy.gif")
# slts_qrcode.to_artistic(
#     background=nirvana_url,
#     target="animated_qrcode.gif",
#     scale=5,
# )

if __name__ == "__main__":

    
    qrcode = get_basic_qr(link, filename)
    print(f'QR Code Generated Successfully!, saved as {filename}')
    
    pass
    # print