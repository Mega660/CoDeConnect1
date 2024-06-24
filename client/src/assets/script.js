document.addEventListener('DOMContentLoaded', () => {
    const BASE_URL = "http://localhost:8000";
    
    const handleFormSubmit = (event) => {
        event.preventDefault();
        const formData = {
            email: document.querySelector('input[type = "email"]').value,
            username: document.querySelector('input[type="text"]').value,
            password: document.querySelector('input[type = "password"]').value,
        };

        fetch (`${BASE_URL}/users/register/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(formData),
        })
        .then(response => response.json())
        .then(data => {
            console.log(data);
        })
        .catch(error => {
            console.log(error);
        });
    }
    const signupButton = document.getElementById("signupButton");
    signupButton.addEventListener('click', handleFormSubmit);
});

