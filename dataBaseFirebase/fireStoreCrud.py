# Assuming get_firestore_client is imported from your firebaseCredentials module
from firebaseCredentials.activateFirebase import get_firestore_client

# Get Firestore client
db = get_firestore_client()


# Create function (C)
def create_document(data, collection_name, doc_id=None):
    """
    Creates a new document in the Firestore collection.

    Parameters:
    - data: A dictionary containing the data to be stored.
    - collection_name: The name of the Firestore collection.
    - doc_id: Optional; a document ID. If not provided, Firestore generates one.

    Returns:
    - The document reference (ID and data).
    """
    try:
        if doc_id:
            db.collection(collection_name).document(doc_id).set(data)
        else:
            doc_ref = db.collection(collection_name).add(data)
        print("Document successfully created!")
    except Exception as e:
        print(f"An error occurred while creating the document: {e}")


# Read function (R)
def read_document(collection_name, doc_id=None):
    print("entro")
    """
    Reads a document from the Firestore collection.

    Parameters:
    - collection_name: The name of the Firestore collection.
    - doc_id: The ID of the document to be retrieved.

    Returns:
    - The document's data or None if the document doesn't exist.
    """
    try:
        doc_ref = db.collection(collection_name).document(doc_id)
        doc = doc_ref.get()
        print(doc.to_dict())
        if doc.exists:
            print(f"Document data: {doc.to_dict()}")
            return doc.to_dict()
        else:
            print(f"No such document with ID: {doc_id}")
            return None
    except Exception as e:
        print(f"An error occurred while reading the document: {e}")
        return None


# Update function (U)
def update_document(collection_name, doc_id, data):
    """
    Updates an existing document in the Firestore collection.

    Parameters:
    - collection_name: The name of the Firestore collection.
    - doc_id: The ID of the document to update.
    - data: A dictionary with the fields to update.
    """
    try:
        db.collection(collection_name).document(doc_id).update(data)
        print(f"Document with ID {doc_id} successfully updated!")
    except Exception as e:
        print(f"An error occurred while updating the document: {e}")


# Delete function (D)
def delete_document(collection_name, doc_id):
    """
    Deletes a document from the Firestore collection.

    Parameters:
    - collection_name: The name of the Firestore collection.
    - doc_id: The ID of the document to delete.
    """
    try:
        db.collection(collection_name).document(doc_id).delete()
        print(f"Document with ID {doc_id} successfully deleted!")
    except Exception as e:
        print(f"An error occurred while deleting the document: {e}")


# List all documents in the collection (Extra function)
def list_all_documents(collection_name):
    """
    Lists all documents in the Firestore collection.

    Parameters:
    - collection_name: The name of the Firestore collection.

    Returns:
    - A list of all document IDs and their data.
    """
    try:
        docs = db.collection(collection_name).stream()
        for doc in docs:
            print(f"Document ID: {doc.id}")
            print(f"Document data: {doc.to_dict()}")
    except Exception as e:
        print(f"An error occurred while listing documents: {e}")
