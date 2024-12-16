document.addEventListener('DOMContentLoaded', () => {
    if (document.querySelector('.title')) {
        document.getElementById('title').focus()
    }
    document.querySelector('#preview').addEventListener('click', () => {
        document.querySelector('#image').click()
    })

})
document.getElementById("image").addEventListener("change", function (event) {
    const file = event.target.files[0]; // دریافت فایل انتخاب‌شده
    const preview = document.getElementById("preview"); // المان پیش‌نمایش
    let original_crc = preview.src

    if (file) {
        const reader = new FileReader();

        reader.onload = function (e) {
            preview.src = e.target.result; // تنظیم URL تصویر به پیش‌نمایش
        };

        reader.readAsDataURL(file); // خواندن فایل و تبدیل به URL
    } else {
        // بازگشت به تصویر پیش‌فرض اگر فایلی انتخاب نشود
        if (location.pathname === '/profile_edit/') {
            preview.src = original_crc
        }
        preview.src = "https://via.placeholder.com/150";
    }

});
