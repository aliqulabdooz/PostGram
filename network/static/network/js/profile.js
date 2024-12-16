document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.card').forEach((e) => {
        e.addEventListener('click', (element) => {
            const id = e.getAttribute('data-id')
            const url = e.getAttribute('data-redirect-url')
            const a = document.createElement('a')
            a.href = `${url}?post=${id}`
            a.click()
        })
    })

})