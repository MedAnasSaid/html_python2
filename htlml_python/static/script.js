// Function for running the test
function runTest() {
    // Récupérer le code généré
    let generatedCode = document.getElementById('generatedCode').innerText;

    // Envoyer le code au serveur pour exécution
    fetch('/run_test', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ code: generatedCode })
    })
    .then(response => {
        if (response.ok) {
            alert('Test executed successfully!');
        } else {
            alert('Failed to execute test!');
        }
    })
    .catch(error => {
        console.error('Error executing test:', error);
        alert('An error occurred while executing the test!');
    });
}

// Event listener for the Run Test button
document.getElementById('runTestButton').addEventListener('click', runTest);
