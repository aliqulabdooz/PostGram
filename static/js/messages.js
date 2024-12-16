document.addEventListener('DOMContentLoaded', () => {
    if (document.querySelector('.close-error')) {
        document.querySelector('.close-error').addEventListener('click', closeErrorMessage)

        function closeErrorMessage() {
            const errorMessage = document.querySelector('.error-message');
            if (errorMessage) {
                errorMessage.style.animation = 'fade 1s ease-out'
                window.setTimeout(() => {
                    errorMessage.style.display = 'none'
                }, 600)
            }
        }
    }


})