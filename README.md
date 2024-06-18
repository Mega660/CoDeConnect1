# CodeConnect

## From API Dev
POST
    Register - server:8000/users/register/
        requires email, password, username
        returns 201 created status on success, with email and username

    Login - server:8000/users/login/
        requires email, password
        returns 200 ok status on success, with email and username
