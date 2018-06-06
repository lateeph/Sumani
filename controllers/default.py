def register():
    return dict()

def store():
    submitted_firstname = request.vars.firstname
    submitted_lastname = request.vars.lastname
    submitted_email = request.vars.email
    submitted_password = request.vars.password

    results = db.users.insert(
        db_firstname=submitted_firstname,
        db_lastname = submitted_lastname,
        db_email = submitted_email,
        db_password = submitted_password
    )

    if results:
        return "User Saved Succesfully"
    else:
        return "An Error Occured"
    