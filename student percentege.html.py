<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Student Grade Calculator</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            background-color: #f0f0f0;
        }
        .container {
            max-width: 600px;
            margin: 0 auto;
            padding: 20px;
            background-color: white;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }
        .form-group {
            margin: 15px 0;
        }
        label {
            display: block;
            margin-bottom: 5px;
        }
        input {
            width: 100%;
            padding: 8px;
            border: 1px solid #ddd;
            border-radius: 4px;
        }
        button {
            background-color: #4CAF50;
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            margin-top: 10px;
        }
        button:hover {
            background-color: #45a049;
        }
        .result {
            margin-top: 20px;
            padding: 15px;
            border: 1px solid #ddd;
            border-radius: 4px;
            background-color: #f9f9f9;
        }
    </style>
</head>
<body>
    <div class="container">
        <h2>Student Grade Calculator</h2>
        <div class="form-group">
            <label for="math">Math Score:</label>
            <input type="number" id="math" min="0" max="100">
        </div>
        <div class="form-group">
            <label for="science">Science Score:</label>
            <input type="number" id="science" min="0" max="100">
        </div>
        <div class="form-group">
            <label for="english">English Score:</label>
            <input type="number" id="english" min="0" max="100">
        </div>
        <button onclick="calculateGrade()">Calculate Grade</button>
        <div id="result" class="result"></div>
    </div>

    <script>
        function calculateGrade() {
            const math = Number(document.getElementById('math').value);
            const science = Number(document.getElementById('science').value);
            const english = Number(document.getElementById('english').value);

            if (isNaN(math) || isNaN(science) || isNaN(english)) {
                alert('Please enter valid numbers');
                return;
            }

            const average = (math + science + english) / 3;
            let grade = '';

            if (average >= 90) grade = 'A';
            else if (average >= 80) grade = 'B';
            else if (average >= 70) grade = 'C';
            else if (average >= 60) grade = 'D';
            else grade = 'F';

            document.getElementById('result').innerHTML = `
                Average Score: ${average.toFixed(2)}<br>
                Grade: ${grade}
            `;
        }
    </script>
</body>
</html>