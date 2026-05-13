import rpyc
# pip install rpyc

class StringService(rpyc.Service):
    def exposed_concatenate(self, str1, str2):
        return str1 + str2

if __name__ == "__main__":
    from rpyc.utils.server import ThreadedServer
    server = ThreadedServer(StringService, port=18861)
    print("RPYC Server is running on port 18861...")
    server.start()
  
