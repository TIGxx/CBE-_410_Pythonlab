def test_calculate_add():
    with app.test_client() as client:
        response = client.get('/calculate?operation=add&a=5&b=3')
        assert response.status_code == 200
        assert response.json['result'] == 8

def test_calculate_invalid_operation():
    with app.test_client() as client:
        response = client.get('/calculate?operation=invalid')
        assert response.status_code == 400
def test_health():
    with app.test_client() as client:
        response = client.get('/health')

        assert response.status_code == 201
        assert response.json == {'status': 'ok'}