def l3jr(request):
    import firebase_admin
    from firebase_admin import credentials
    from firebase_admin import firestore

    # Use the application default credentials
    cred = credentials.ApplicationDefault()
    firebase_admin.initialize_app(cred, {
        'projectId': "l3jr-c35a0",
    })

    db = firestore.client()
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
    """
    id = request.args.get('id')
    doc_ref = db.collection('places').document(id)

    try:
        doc = doc_ref.get()
        return 'Document data: {}'.format(doc.to_dict())
    except google.cloud.exceptions.NotFound:
        return 'No such document!'
    #
    # request_json = request.get_json()
    # places = db.collection('places').stream()
    # return_json = {}
    # for place in places:
    #     snapshot = place.get()
    #     return_json[snapshot.id] = snapshot.to_dict()
    # return return_json
