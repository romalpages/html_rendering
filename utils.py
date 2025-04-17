from flask import Flask, render_template, send_file
import pdfkit
import os
import io 


def index():
    return render_template('index.html')

def generate_pdf():
    rendered = render_template('index.html')
    pdf = pdfkit.from_string(rendered, False, configuration=config, options=options)
    return send_file(
        io.BytesIO(pdf),
        download_name='output.pdf',
        as_attachment=True
        return jsonify("Download")
    )
    