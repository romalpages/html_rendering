from flask import Flask, render_template, send_file
import pdfkit
import os
import io  # <-- This is required for BytesIO

app = Flask(__name__)

path_to_wkhtmltopdf = r'E:/internship/wkhtmltopdf/bin/wkhtmltopdf.exe'
config = pdfkit.configuration(wkhtmltopdf=path_to_wkhtmltopdf)

options = {
    'enable-local-file-access': '',
    'page-size': 'A4',
    'encoding': 'UTF-8',
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate-pdf')
def generate_pdf():
    rendered = render_template('index.html')
    pdf = pdfkit.from_string(rendered, False, configuration=config, options=options)
    return send_file(
        io.BytesIO(pdf),
        download_name='output.pdf',
        as_attachment=True
    )

if __name__ == '__main__':
    app.run(debug=True)
