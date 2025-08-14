document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('registerForm');
    form.addEventListener('submit', function(e) {
        // Basic client-side validation
        const name = form.elements['name'].value.trim();
        const email = form.elements['email'].value.trim();
        if (!name || !email) {
            alert('Please fill in all fields.');
            e.preventDefault();
        }
    });
});