/**
 * KVJ Analytics - Main Scripts
 */

document.addEventListener('DOMContentLoaded', () => {
    // Mobile Menu Toggle
    const mobileMenuBtn = document.querySelector('.mobile-menu-btn');
    const navLinks = document.querySelector('.nav-links');

    if (mobileMenuBtn && navLinks) {
        mobileMenuBtn.addEventListener('click', () => {
            navLinks.classList.toggle('active');

            // Toggle icon (hamburger to close)
            const icon = mobileMenuBtn.querySelector('i');
            if (navLinks.classList.contains('active')) {
                icon.classList.remove('fa-bars');
                icon.classList.add('fa-times');
            } else {
                icon.classList.remove('fa-times');
                icon.classList.add('fa-bars');
            }
        });
    }

    // Set active nav link based on current path
    const initializeActiveLink = () => {
        const currentPath = window.location.pathname.split('/').pop() || 'index.html';
        const navItems = document.querySelectorAll('.nav-links a');

        navItems.forEach(link => {
            const href = link.getAttribute('href');
            if (href === currentPath) {
                link.classList.add('active');
            } else {
                link.classList.remove('active');
            }
        });
    };

    initializeActiveLink();

    // Contact Form Handling (AJAX)
    const contactForm = document.getElementById('contact-form');
    const formResult = document.getElementById('form-result');
    const submitBtn = document.getElementById('submit-btn');

    if (contactForm) {
        contactForm.addEventListener('submit', function (e) {
            e.preventDefault();

            const formData = new FormData(contactForm);
            const object = Object.fromEntries(formData);
            const json = JSON.stringify(object);

            formResult.style.display = 'block';
            formResult.style.backgroundColor = 'rgba(59, 130, 246, 0.1)';
            formResult.style.color = 'var(--accent-primary)';
            formResult.innerHTML = "Sending...";
            submitBtn.disabled = true;

            // Using the security string to prevent naked email issues
            const endpoint = "https://formsubmit.co/ajax/915c0ae7840117c04ad9d99403b4d857";

            fetch(endpoint, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Accept': 'application/json'
                },
                cache: 'no-cache',
                body: json
            })
                .then(async (response) => {
                    let res = await response.json();
                    if (response.ok) {
                        formResult.style.backgroundColor = 'rgba(16, 185, 129, 0.1)';
                        formResult.style.color = '#10B981';
                        formResult.innerHTML = "Thank you! Your message has been sent to our team.";
                        contactForm.reset();
                    } else {
                        console.log(response);
                        formResult.style.backgroundColor = 'rgba(239, 68, 68, 0.1)';
                        formResult.style.color = '#EF4444';
                        formResult.innerHTML = "Error: " + (res.message || "Something went wrong. Please try again.");
                    }
                })
                .catch(error => {
                    console.log(error);
                    formResult.innerHTML = "Something went wrong!";
                })
                .then(function () {
                    submitBtn.disabled = false;
                    setTimeout(() => {
                        formResult.style.display = "none";
                    }, 5000);
                });
        });
    }
});
