document.addEventListener('DOMContentLoaded', () => {
    if (document.querySelector('.title')) {
        document.getElementById('title').focus()
    }
    document.querySelector('#preview').addEventListener('click', () => {
        document.querySelector('#image').click()
    })

})
document.getElementById("image").addEventListener("change", function (event) {
    const file = event.target.files[0];
    const preview = document.getElementById("preview");
    let original_crc = preview.src

    if (file) {
        const reader = new FileReader();

        reader.onload = function (e) {
            preview.src = e.target.result;
        };

        reader.readAsDataURL(file);
    } else {

        if (location.pathname === '/profile_edit/') {
            preview.src = original_crc
        }
        preview.src = "https://via.placeholder.com/150";
    }

});
