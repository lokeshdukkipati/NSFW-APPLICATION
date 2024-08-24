@app.route('/', methods=['POST', 'GET'])
def main():
    if request.method == 'GET':
        return render_template('index.html')

    received_text = request.form.get('text')
    if received_text:  # Check if text data is received
        #translated_text = translator.translate(received_text).text
        if ishate(received_text):
            return jsonify(False)
        return jsonify(True)
    else:
        return jsonify(False)  # Return False if no text data received

if __name__ == "__main__":
    app.run(debug=True)