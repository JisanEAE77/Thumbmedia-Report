    var userError = document.getElementById('usernameError');
    var userInput = document.getElementById('InputUser');
    var passwordError = document.getElementById('passwordError');
    var passwordInput = document.getElementById('InputPassword')

    //  check if username exists
    var checkUsername = (user) => {
    console.log("working");
        fetch(`/validateusername/${user}`).then(response => response.json()).then(data => {
            if(data['response'] == 'VALID'){
                userInput.classList.value = 'form-control is-valid';
                userError.innerHTML = '';
            } else {
                userError.classList.value = 'text-danger';
                userInput.classList.value = 'form-control is-invalid';
                userError.innerHTML = 'Username doesn\'t exist, please enter a valid username!';
            }
        });
    };

    // validate login
    var validateLogin = () => {
        fetch(`/validatelogin/${userInput.value}/${passwordInput.value}`).then(response => response.json()).then(data => {
            if(data["response"] == "VALID"){
                passwordInput.classList.value = 'form-control is-valid';
                passwordError.innerHTML = '';
            } else {
                passwordError.classList.value = 'text-danger';
                passwordInput.classList.value = 'form-control is-invalid';
                passwordError.innerHTML = 'Password don\'t match for this username!';
            }
        });
    };