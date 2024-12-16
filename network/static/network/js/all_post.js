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