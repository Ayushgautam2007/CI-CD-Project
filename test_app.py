import pytest
from bson.objectid import ObjectId

from app import app, mongo


@pytest.fixture
def client():

    app.config["TESTING"] = True

    with app.app_context():

        mongo.db.students.delete_many({})

        mongo.db.students.insert_one({
            "_id": ObjectId("66fddff25f4b5f6a0a12345"),
            "name": "Test Student",
            "email": "test@student.com",
            "course": "Flask"
        })

    with app.test_client() as client:
        yield client

    with app.app_context():
        mongo.db.students.delete_many({})


def test_home_page(client):

    response = client.get("/")

    assert response.status_code == 200
    assert b"Test Student" in response.data


def test_add_student(client):

    response = client.post(
        "/add",
        data={
            "name": "New User",
            "email": "new@user.com",
            "course": "Python"
        },
        follow_redirects=True
    )

    assert response.status_code == 200
    assert b"New User" in response.data


def test_update_student(client):

    response = client.post(
        "/update/66fddff25f4b5f6a0a12345",
        data={
            "name": "Updated Name",
            "email": "updated@student.com",
            "course": "Updated Course"
        },
        follow_redirects=True
    )

    assert response.status_code == 200
    assert b"Updated Name" in response.data


def test_delete_student(client):

    with app.app_context():

        student_id = mongo.db.students.insert_one({
            "name": "Temp User",
            "email": "temp@user.com",
            "course": "Temp Course"
        }).inserted_id

    response = client.get(
        f"/delete/{student_id}",
        follow_redirects=True
    )

    assert response.status_code == 200

    with app.app_context():
        assert mongo.db.students.find_one({"_id": student_id}) is None
