from download_data import *
from pipelines.ingest import ingest
from pipelines.transform import transform
from pipelines.serve import serve

def run():
    # download
    # (optional : comment after first run)
    
    ingest()
    transform()
    serve()
    
if __name__ ==  "__main__" :
    run()