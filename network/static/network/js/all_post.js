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
    captionElement.classList.toggle('text-truncate')
}