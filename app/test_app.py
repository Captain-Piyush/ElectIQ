import os
import pytest
from unittest.mock import patch, MagicMock

def test_health_check(client):
    """1. test_health_check — GET /health returns 200 and {status: 'ok'}"""
    response = client.get('/health')
    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}

def test_chat_empty_message(client):
    """2. test_chat_empty_message — POST /api/chat with empty string returns 400"""
    response = client.post('/api/chat', json={"message": ""})
    assert response.status_code == 400

def test_chat_too_long(client):
    """3. test_chat_too_long — POST /api/chat with 600 char message returns 400"""
    long_message = "a" * 600
    response = client.post('/api/chat', json={"message": long_message})
    assert response.status_code == 400

@patch('main.client')
def test_chat_valid_message(mock_client, client):
    """4. test_chat_valid_message — POST /api/chat with 'How do I register to vote?' 
       returns 200 with a non-empty response string (mock the Gemini API call)"""
    mock_response = MagicMock()
    mock_response.text = "You can register to vote online or by mail."
    mock_client.models.generate_content.return_value = mock_response

    response = client.post('/api/chat', json={"message": "How do I register to vote?"})
    
    assert response.status_code == 200
    data = response.get_json()
    assert data is not None
    assert "response" in data
    assert len(data["response"]) > 0
    mock_client.models.generate_content.assert_called_once()

@patch('main.client')
def test_chat_history_passed(mock_client, client):
    """5. test_chat_history_passed — verify conversation history is included 
       in Gemini API call"""
    mock_response = MagicMock()
    mock_response.text = "Yes, you can check online."
    mock_client.models.generate_content.return_value = mock_response

    history = [
        {"role": "user", "parts": "Am I registered?"},
        {"role": "model", "parts": "You need to check with your state."}
    ]
    
    response = client.post('/api/chat', json={
        "message": "How do I do that?",
        "history": history
    })
    
    # Asserting successful routing and mock invocation
    assert response.status_code == 200
    mock_client.models.generate_content.assert_called_once()
    
    # Verify history is passed to the Gemini call
    call_args, call_kwargs = mock_client.models.generate_content.call_args
    assert 'contents' in call_kwargs
    contents_str = str(call_kwargs['contents'])
    
    # History data should be present in the call's contents argument
    assert "Am I registered?" in contents_str

def test_cors_headers(client):
    """6. test_cors_headers — verify CORS headers present in response"""
    response = client.options('/api/chat')
    if response.status_code == 405:
        # Fallback to a GET/POST request if OPTIONS is not specifically handled
        response = client.post('/api/chat', json={"message": "test"})
        
    assert response.headers.get('Access-Control-Allow-Origin') is not None

def test_no_api_key_hardcoded():
    """7. test_no_api_key_hardcoded — scan main.py source and assert the string 
       'AIza' does not appear"""
    main_py_path = os.path.join(os.path.dirname(__file__), 'main.py')
    with open(main_py_path, 'r', encoding='utf-8') as f:
        source_code = f.read()
    
    assert "AIza" not in source_code, "Hardcoded API key found in main.py!"

def test_rate_limit_headers(client):
    """8. test_rate_limit_headers — verify rate limit headers present"""
    response = client.get('/')
    
    headers_str = str(response.headers).lower()
    # Looking for typical rate limiting headers
    assert "ratelimit" in headers_str or "retry-after" in headers_str, "Rate limit headers not found"
