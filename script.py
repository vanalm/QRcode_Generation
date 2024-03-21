import segno
qr = segno.make('https://youtube.com/shorts/N2IKLQy7ZIY?feature=share')
qr.save(
    "scaled_qrcode.png",
    scale=5,
    boarder=10, 
    light="lightblue",
    dark="darblue",
    quiet_zone="maroon",
    data_dark="green",

)

