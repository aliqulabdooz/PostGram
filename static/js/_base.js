document.addEventListener('DOMContentLoaded', () => {
    let active
    document.querySelectorAll('.nav-link').forEach((e) => {
        if (e.classList.contains('active')) {
            active = e
        }
        e.addEventListener('mouseenter', () => {
            if (active) {
                active.classList.remove('active')
            }
        })
        e.addEventListener('mouseleave', () => {
            if (active) {
                active.classList.add('active')

            }
        })
    })
})