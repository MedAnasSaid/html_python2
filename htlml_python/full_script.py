from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/run_test', methods=['POST'])
def run_test():
    # Récupérer le code envoyé depuis la requête POST
    code = request.json.get('code')

    # Ici, vous pouvez exécuter le code reçu, par exemple :
    # exec(code)
    # Pour l'exemple, nous renvoyons simplement un message de succès
    return jsonify({'message': 'Test exécuté avec succès !'}), 200

@app.route('/')
def index():
    # Page d'accueil qui renvoie le contenu HTML
    return """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Generated Selenium Code</title>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
  <style>
    body {
      font-family: Arial, sans-serif;
    }
    .container {
      max-width: 800px;
      margin: 50px auto;
      padding: 20px;
      border: 1px solid #ccc;
      border-radius: 5px;
    }
    .select-area-container {
      display: flex;
      align-items: center;
      margin-bottom: 20px;
    }
    select,
    textarea,
    input[type="url"],
    input[type="text"] {
      width: calc(33.33% - 16px);
      padding: 10px;
      margin: 5px 0;
      border: 1px solid #ccc;
      border-radius: 5px;
    }
    textarea {
      width: calc(50% - 16px);
    }
    .add-button {
      width: 30px;
      height: 30px;
      margin-left: 10px;
      border: none;
      background-color: #4CAF50;
      color: white;
      border-radius: 50%;
      cursor: pointer;
    }
    .generate-button {
      padding: 10px 20px;
      background-color: #007bff;
      color: white;
      border: none;
      border-radius: 5px;
      cursor: pointer;
    }
  </style>
</head>
<body>
  <div class="container">
    <h1>Dynamic Script Generator</h1>
    <div id="areasContainer">
      <!-- Container for the URL input field -->
      <div class="select-area-container" id="urlContainer">
        <input type="url" name="url" id="url" placeholder="Enter URL" required>
      </div>
    </div>
    <button id="addButton">Add Select and Text Area</button>
    <!-- Paragraph for displaying the value of x -->
    <p id="xValue"></p>
    <!-- Button for generating the code -->
    <button type="submit" class="generate-button" onclick="generateCode()"><i class="fas fa-code"></i> Generate Code</button>
    <h2>Python Code Generated:</h2>
    <pre id="generatedCode"></pre>
    <!-- Button for running the test -->
    <button type="button" id="runTestButton" class="generate-button"><i class="fas fa-play"></i> Run Test</button>
  </div>
  <script>
    let x = 0; // Initialize the value of x

    // Function for adding a new select and text area container
    function addSelectAndTextArea() {
      x++; // Increment the value of x
      const container = document.getElementById('areasContainer');
      for (let i = 0; i < 1; i++) { // Loop to add two sets of select and text areas
        const selectAreaContainer = document.createElement('div');
        selectAreaContainer.classList.add('select-area-container');
        selectAreaContainer.id = `${x}`;

        const select1 = document.createElement('select');
        select1.name = `S1_${x}`;
        select1.id = `S1_${x}`;
        select1.required = true;

        const option1_1 = document.createElement('option');
        option1_1.value = 'button';
        option1_1.textContent = 'button';

        const option1_2 = document.createElement('option');
        option1_2.value = 'input';
        option1_2.textContent = 'input';

        select1.appendChild(option1_1);
        select1.appendChild(option1_2);

        const select2 = document.createElement('select');
        select2.name = `S2_${x}`;
        select2.id = `S2_${x}`;
        select2.required = true;

        const option2_1 = document.createElement('option');
        option2_1.value = 'css_selector';
        option2_1.textContent = 'css selector';

        const option2_2 = document.createElement('option');
        option2_2.value = 'xpath';
        option2_2.textContent = 'xpath';
        
        select2.appendChild(option2_1);
        select2.appendChild(option2_2);
        

        const textArea1 = document.createElement('textarea');
        textArea1.name = `TA1_${x}`;
        textArea1.id = `TA1_${x}`;
        textArea1.placeholder = 'Enter css selector';
        textArea1.required = true;

        const textArea2 = document.createElement('textarea');
        textArea2.name = `TA2_${x}`;
        textArea2.id = `TA2_${x}`;
        textArea2.placeholder = 'Enter Value quand vous choissez input ';
        textArea2.required = true;

        selectAreaContainer.appendChild(select1);
        selectAreaContainer.appendChild(select2);
        selectAreaContainer.appendChild(textArea1);
        selectAreaContainer.appendChild(textArea2);

        container.appendChild(selectAreaContainer);
      }
    }

    // Event listener for the Add button
    document.getElementById('addButton').addEventListener('click', addSelectAndTextArea);

    // Function to generate code
    function generateCode() {
        var url = document.getElementById('url').value;
      let generatedCode =`from selenium import webdriver
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
driver = webdriver.Chrome()
driver.get('${url}')
print(driver.title)




\n`;
      for (let i = 1; i <= x; i++) {
        
        const select1Value = document.getElementById(`S1_${i}`).value;
        const select2Value = document.getElementById(`S2_${i}`).value;
        const textareaValue1 = document.getElementById(`TA1_${i}`).value;
        const textareaValue2 = document.getElementById(`TA2_${i}`).value;
        if (select1Value === "button") {
          generatedCode += `element${i} =driver.find_element_by_${select2Value}("${textareaValue1}").click();\n`;
        } else if (select1Value === "input") {
          generatedCode += `element${i} = driver.find_element_by_${select2Value}("${textareaValue1}")\nelement${i}.send_keys('${textareaValue2}');\n`;
        }

   
      }
      generatedCode +=`time.sleep(7) \ndriver.quit()`;
      
      document.getElementById('generatedCode').textContent = generatedCode;
    }
    // Ajouter un événement click sur le bouton "Run Test"
document.getElementById('runTestButton').addEventListener('click', function() {
    // Récupérer le code généré
    var generatedCode = document.getElementById('generatedCode').innerText;

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
});


  </script>
</body>
</html>
"""

if __name__ == '__main__':
    app.run(debug=True)
