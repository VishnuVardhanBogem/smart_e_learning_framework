function getRecommendations() {
    const userId = document.getElementById('userId').value;
    if (!userId) {
        alert('Please enter a User ID');
        return;
    }

    fetch('http://127.0.0.1:5000/api/recommend', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ user_id: userId })
    })
    .then(response => response.json())
    .then(data => {
        const resultDiv = document.getElementById('recommendationResult');
        if (data.error) {
            resultDiv.innerHTML = `<p>${data.error}</p>`;
        } else {
            resultDiv.innerHTML = `<p>Recommended modules: ${data.join(', ')}</p>`;
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
}
