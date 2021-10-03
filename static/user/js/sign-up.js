    var userError = document.getElementById('usernameError');
    var userInput = document.getElementById('InputUser');
    var emailError = document.getElementById('emailError');
    var emailInput = document.getElementById('InputEmail');
    var passwordError = document.getElementById('passwordError');
    var passwordInput = document.getElementById('InputPassword')
   var cPasswordError = document.getElementById('cPasswordError');
    var cPasswordInput = document.getElementById('ConfirmPassword')
    //  check if username exists
    var checkUsername = (user) => {
    console.log("working");
        fetch(`/validateusername/${user}`).then(response => response.json()).then(data => {
            if(data['response'] == 'INVALID'){
                userInput.classList.value = 'form-control is-valid';
                userError.innerHTML = '';
            } else {
                userError.classList.value = 'text-danger';
                userInput.classList.value = 'form-control is-invalid';
                userError.innerHTML = 'Username already exists, please choose another!';
            }
        });
    };

    // check if email exists
    var checkEmail = (userEmail) => {
        fetch(`/validateemail/${userEmail}`).then(response => response.json()).then(data => {
            if(data['response'] == 'INVALID' && emailFormat(userEmail)){
                emailInput.classList.value = 'form-control is-valid';
                emailError.innerHTML = '';
            } else if(!emailFormat(userEmail)) {
                emailError.classList.value = 'text-danger';
                emailInput.classList.value = 'form-control is-invalid';
                emailError.innerHTML = 'Invalid E-mail format, enter a valid E-mail!';
            } else {
                emailError.classList.value = 'text-danger';
                emailInput.classList.value = 'form-control is-invalid';
                emailError.innerHTML = 'This E-mail is already in use!';
            }
        });
    };


    // email format validator
    function emailFormat(email) {
        if (/^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/.test(email)) {
            return (true)
        } else {
            return (false)
        }
    }

    // password strength validator
    function passwordStrength(password) {
        var strength=  /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[^a-zA-Z0-9])(?!.*\s).{6,100000}$/;
        if(password.match(strength)){
           passwordInput.classList.value = 'form-control is-valid';
           passwordError.innerHTML = '';
        } else  {
            passwordError.classList.value = 'text-danger';
            passwordInput.classList.value = 'form-control is-invalid';
            passwordError.innerHTML = 'Weak password! Your password should contain at least one lowercase letter, one uppercase letter, one numeric digit, one special character and must be at least 6 character long!';
        }
    }

    function matchPassword(password){
        if(password == passwordInput.value){
           cPasswordInput.classList.value = 'form-control is-valid';
           cPasswordError.innerHTML = '';
        } else  {
            cPasswordError.classList.value = 'text-danger';
            cPasswordInput.classList.value = 'form-control is-invalid';
            cPasswordError.innerHTML = "Password didn't match!";
        }
    }

