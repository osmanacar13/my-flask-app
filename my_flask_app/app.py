# app.py
from flask import Flask, render_template, request, jsonify

app = Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET', 'POST'])
def anket_formu():
    if request.method == 'POST':
        veriler = request.form
        # Anket verilerini bir dosyaya kaydedebiliriz
        with open('anket_verileri.csv', 'a') as f:
            f.write(f"{veriler['isim']},{veriler['yas']},{veriler['cinsiyet']},{veriler['memleket']}\n")
        return "Anket başarıyla gönderildi. Teşekkürler!"
    return render_template('anket_formu.html')

if __name__ == '__main__':
    app.run(debug=True)
