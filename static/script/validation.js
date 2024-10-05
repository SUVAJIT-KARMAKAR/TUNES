function validateForm() {
    // Simple validation example, you should implement more robust validation logic
    const email = document.getElementsByName('email')[0].value;
    const phoneNumber = document.getElementsByName('phone_number')[0].value;

    // Email validation regex
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

    // Phone number validation regex (simple example)
    const phoneRegex = /^\d{10}$/;

    if (!emailRegex.test(email)) {
        alert('INVALID EMAIL ADDRESS');
        return false;
    }

    if (!phoneRegex.test(phoneNumber)) {
        alert('INVAILD PHONE NUMBER');
        return false;
    }

    return true;
}
