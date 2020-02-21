import time
import logging
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

logging.basicConfig(filename='portfolio_listener.log', filemode='w',
                    format='%(asctime)s | %(levelname)s: %(message)s',
                    level=logging.INFO, datefmt='%m/%d/%Y %I:%M:%S %p'
                    )
cred = credentials.Certificate(
    "portfolio-website-340c1-firebase-adminsdk-8lff3-7442a173ef.json"
    )
firebase_admin.initialize_app(cred)

db = firestore.client()
document_quantity = 0


# docs = db.collection(u'users').stream()
# Create a callback on_snapshot function to capture changes
def on_snapshot(col_snapshot, changes, read_time):
    if document_quantity != len(list(col_snapshot)):
        print("I got a callback")
        order_doc_dict = {}
        order_doc_list = []
        for doc in col_snapshot:
            order_doc_dict[doc.create_time.seconds] = doc
        for value in sorted(order_doc_dict.keys()):
            order_doc_list.append(order_doc_dict[value])
        doc = order_doc_list[-1]
        email = doc._data.get('email')
        name = doc._data.get('fullname')
        message = doc._data.get('message')
        logging.info('\nemail: %s\nname: %s\nmessage: %s\n\n',
                     email, name, message)
        print(u'Document data: {}'.format(doc.to_dict()))


if __name__ == '__main__':
    col_query = db.collection(u'users')
    query_watch = col_query.on_snapshot(on_snapshot)
    while True:
        time.sleep(2)
        print("zzzz....")
