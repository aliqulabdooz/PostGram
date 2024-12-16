document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.switch-link').forEach((e) => {
        e.addEventListener('click', toggleForms)
    })


    function toggleForms(event) {
        const loginForm = document.querySelector('.login-container');
        const signupForm = document.querySelector('.signup-container');
        const baseUrl = `${window.location.protocol}//${window.location.host}`
        const path = event.target.getAttribute('data-get-url')
        history.pushState(null, '', `${baseUrl}${path}`)
        loginForm.classList.toggle('active');
        if (loginForm.classList.contains('active')) {
            loginForm.querySelector('.user-login').focus()
        } else {
            requestAnimationFrame(() => {
                signupForm.querySelector('.user-register').focus()

            })
        }
        signupForm.classList.toggle('active');

    }

    window.addEventListener('popstate', () => {
        const loginForm = document.querySelector('.login-container');
        const signupForm = document.querySelector('.signup-container');
        loginForm.classList.toggle('active');
        signupForm.classList.toggle('active');
    })
})