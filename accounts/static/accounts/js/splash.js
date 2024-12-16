const redirect_url = document.querySelector('.redirect_url').getAttribute('data-redirect-url')
if (redirect_url) {
    setTimeout(function () {
        window.location.href = redirect_url;
    }, 3500);
}