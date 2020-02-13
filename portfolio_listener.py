import sys
import time
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("portfolio-website-340c1-firebase-adminsdk-8lff3-7442a173ef.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

docs = db.collection(u'users').stream()
current_docs = len(list(docs))


def main_loop():
    while True:
        if current_docs != len(list(docs)):
            for doc in docs:
                print(u'{} => {}'.format(doc.id, doc.to_dict()))
        time.sleep(1.1)


if __name__ == '__main__':
    try:
        main_loop()
    except KeyboardInterrupt:
        print >> sys.stderr, '\nExiting by user request.\n'
        sys.exit(0)
