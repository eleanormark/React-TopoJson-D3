from www.server import create


if __name__ == "__main__":
    app = create()
    app.run(host='0.0.0.0', port=5000, threaded=True, debug=True)
