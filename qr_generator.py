import qrcode
from PIL import Image


def create_qr_code(url:str, save_where: str, color="black", backcolor="white", logo_name="na", filename="default"):
    # Daten für den QR-Code
    data = url

    # QR-Code generieren
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=1,
        )
    qr.add_data(data)
    qr.make(fit=True)

    # QR-Code als Bild erstellen
    qr_image = qr.make_image(fill_color=color, back_color=backcolor).convert('RGB')

    # Logo laden
    if logo_name != "na":
        logo_path = logo_name  # Pfad zu Ihrem Logo
        logo = Image.open(logo_name)
    
        # Größe des QR-Codes und des Logos ermitteln
        qr_size = qr_image.size[0]
        logo_size = logo.size[0]
    
        # Logo skalieren
        base_size = qr_size // 5
        logo = logo.resize((base_size, base_size), Image.LANCZOS)
    
        # Position des Logos berechnen
        pos = ((qr_size - base_size) // 2, (qr_size - base_size) // 2)
    
        # QR-Code und Logo kombinieren
        qr_image.paste(logo, pos, logo) 

    # QR-Code speichern
    qr_image.save(f"{save_where}/{filename}.png")

    # QR-Code anzeigen
    #qr_image.show()