document.addEventListener('DOMContentLoaded', () => {
    const BASE_URL = "http://localhost:8000";
    
    const handleFormSubmit = (event) => {
        event.preventDefault(); 

        const formData = {
            email: document.querySelector('input[type="email"]').value,
            password: document.querySelector('input[type="password"]').value,

        };

        fetch (`${BASE_URL}/users/login/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(formData),
        })
        .then (response => response.json())
        .then (data => {
            console.log (data);
        })

        .catch(error=> {
            console.error('Error:', error);
        });
    };
    const loginButton = document.getElementById('signinButton');
    loginButton.addEventListener('click', handleFormSubmit);
})