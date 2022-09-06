import gui, download

proxy_handler = {
    "http": "127.0.0.1",
    'https': '127.0.0.1'
}
#helpers.install_proxy(proxy_handler)

def main():
    gui.open()
    #download.manager("https://www.youtube.com/watch?v=D9G1VOjN_84&list=PLep4cGi16m4Oi_7Pq5Ai590sjKIsEgdgd", "mp3")

if __name__ == '__main__':
    main()