import pytest

def test_get_all_goals_from_empty_db(client):
    response = client.get("/")
    response_body = response.get_json()
    
    assert response.status_code == 200
    assert response_body == []

def test_insert_and_get_one_goal(client):
    insert_response = client.get("/insert")
    insert_response_body = insert_response.get_json()

    assert "id" in insert_response_body
    assert "title" in insert_response_body
    assert "due_date" in insert_response_body

    get_response = client.get("/")
    get_response_body = get_response.get_json()

    assert len(get_response_body) == 1
    assert get_response_body[0] == insert_response_body