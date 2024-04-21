document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('dataForm');
    const resultDiv = document.getElementById('result');

    form.addEventListener('submit', function(event) {
        event.preventDefault();

        const formData = new FormData(form);
        const formDataObj = Object.fromEntries(formData.entries());
        console.log(formDataObj);
        fetch('/prediction', {
            method: 'POST',
            body: JSON.stringify(formDataObj),
            headers: {
                'Content-Type': 'application/json'
            }
        })
        .then(response => response.text())
        .then(text => {
            resultDiv.textContent = text;
        })
        .catch(error => console.error('Error:', error));
    });
});
