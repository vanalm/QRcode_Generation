import segno
qrcode = segno.make('https://youtube.com/shorts/N2IKLQy7ZIY?feature=share')
# qrcode_rotated = qrcode.to_pil().rotate(45)

## Formatted QR Code
qrcode_rotated = qrcode.to_pil(
    scale=5,
    light="lightblue",
    dark="green",
).rotate(45, expand=True)
qrcode_rotated.save("formatted_rotated_qrcode.png")


## Basic QR Code
qrcode.save(
    "scaled_qrcode.png",
    scale=10,
    # boarder=10, 
    # light="lightblue",
    # dark="darblue",
    # quiet_zone="maroon",
    # data_dark="green",
    # data_light="lightgreen",


)



from urllib.request import urlopen

slts_qrcode = segno.make_qr("https://www.youtube.com/watch?v=hTWKbfoikeg")
nirvana_url = urlopen("https://media.giphy.com/media/LpwBqCorPvZC0/giphy.gif")
slts_qrcode.to_artistic(
    background=nirvana_url,
    target="animated_qrcode.gif",
    scale=5,
)

