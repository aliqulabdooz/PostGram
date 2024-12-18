document.addEventListener('DOMContentLoaded', () => {
    const id = location.search.split('=')[1]
    const target = document.getElementById(id)
    setTimeout(() => {
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    }, 100)

})
function toggleCaption(captionId) {
    const captionElement = document.getElementById(captionId);
    const read_more = document.getElementById('read-more')
    captionElement.classList.toggle('text-truncate')
    if (captionElement.classList.contains('text-truncate')) {
        read_more.textContent = 'read more'
    } else {
        read_more.textContent = 'close caption'
    }
}

function previewImage(event) {
    const reader = new FileReader();
    reader.onload = function () {
        document.getElementById('preview').src = reader.result;
    };
    reader.readAsDataURL(event.target.files[0]);
}

const imageContainer = document.querySelector('label[for="image"]');
const overlay = document.getElementById('upload-overlay');

if (imageContainer && overlay) {
    imageContainer.addEventListener('mouseenter', () => {
        overlay.style.display = 'block';
    });
    imageContainer.addEventListener('mouseleave', () => {
        overlay.style.display = 'none';
    });
}
