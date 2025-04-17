from flask import Flask, send_file
import pdfkit
import io

app = Flask(__name__)

# URL to convert
url = 'https://www.w3schools.com/w3css/tryw3css_templates_architect.htm'

# Path to wkhtmltopdf
config = pdfkit.configuration(wkhtmltopdf=r'E:/internship/wkhtmltopdf/bin/wkhtmltopdf.exe')

@app.route('/generate-pdf')
def generate_pdf():
    # Generate PDF in-memory (not saved to file)
    pdf = pdfkit.from_url(url, False, configuration=config)

    # Return PDF as a downloadable file
    return send_file(
        io.BytesIO(pdf),
        download_name='output_url.pdf',
        as_attachment=True,
        mimetype='application/pdf'
    )

if __name__ == '__main__':
    app.run(debug=True)
