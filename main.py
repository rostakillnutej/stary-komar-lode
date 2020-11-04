from lode import app, socketio

if __name__ == '__main__':
    #socketio.run(app)
    app.run(debug=True, host= '0.0.0.0', port="8000")
