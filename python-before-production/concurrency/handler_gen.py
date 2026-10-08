def handle(conn):
    page = yield read_file("index.html")
    yield conn.send(page)
