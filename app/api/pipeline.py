from api import idee, postrank

class Pipeline(object):
    
    apis = [
        idee.PixMatch,
        postrank.PostrankApi,
    ]
    
    def run(self, msg):
        context = {}
        for f in self.apis:
            context.update(f.process(msg))
        return context