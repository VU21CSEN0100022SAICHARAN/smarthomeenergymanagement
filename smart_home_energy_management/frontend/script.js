document.getElementById('predictButton').addEventListener('click', function() {
    const userId = document.getElementById('userId').value;
    const applianceId = document.getElementById('applianceId').value;
    const dayOfWeek = document.getElementById('dayOfWeek').value;
    const hour = document.getElementById('hour').value;

    fetch('predict.php', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: `user_id=${userId}&appliance_id=${applianceId}&day_of_week=${dayOfWeek}&hour=${hour}`
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('predictionResult').innerText = `Predicted Energy Usage: ${data.predicted_usage} kWh`;
    });
});
