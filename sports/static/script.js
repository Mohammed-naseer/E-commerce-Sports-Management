/**
 * dSports E-Commerce Interactive Application Scripts
 */

// Modal handlers
function openModal(imageSrc, captionText) {
    var modal = document.getElementById("myModal");
    var modalImg = document.getElementById("img01");
    var caption = document.getElementById("caption");
    if (!modal || !modalImg) return;

    modal.style.display = "block";
    modalImg.src = imageSrc;
    if (caption) {
        caption.innerText = captionText || "";
    }
}

function closeModal() {
    var modal = document.getElementById("myModal");
    if (modal) {
        modal.style.display = "none";
    }
}

// Close modal when clicking outside dialog
window.addEventListener("click", function(event) {
    var modal = document.getElementById("myModal");
    if (event.target === modal) {
        closeModal();
    }
});

// Close modal on Escape key
window.addEventListener("keydown", function(event) {
    if (event.key === "Escape") {
        closeModal();
    }
});

// Toast Notifications Auto-Dismiss
document.addEventListener("DOMContentLoaded", function() {
    var toasts = document.querySelectorAll(".toast-message");
    toasts.forEach(function(toast) {
        setTimeout(function() {
            toast.style.transition = "opacity 0.5s ease, transform 0.5s ease";
            toast.style.opacity = "0";
            toast.style.transform = "translateX(50px)";
            setTimeout(function() {
                toast.remove();
            }, 500);
        }, 4000);
    });

    // Payment Option selection style toggle
    var paymentOptions = document.querySelectorAll(".payment-option");
    paymentOptions.forEach(function(option) {
        option.addEventListener("click", function() {
            paymentOptions.forEach(function(opt) { opt.classList.remove("selected"); });
            this.classList.add("selected");
            var radio = this.querySelector("input[type='radio']");
            if (radio) radio.checked = true;
        });
    });

    // AJAX Add to Cart for all add-to-cart forms
    var addForms = document.querySelectorAll(".add-to-cart-form");
    addForms.forEach(function(form) {
        form.addEventListener("submit", function(e) {
            e.preventDefault();
            var formEl = this;
            var url = formEl.getAttribute("action");
            var formData = new FormData(formEl);
            var submitBtn = formEl.querySelector("button[type='submit']");
            var originalBtnHtml = submitBtn ? submitBtn.innerHTML : "";

            if (submitBtn) {
                submitBtn.disabled = true;
                submitBtn.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i> Adding...';
            }

            fetch(url, {
                method: "POST",
                body: formData,
                headers: {
                    "X-Requested-With": "XMLHttpRequest"
                }
            })
            .then(function(response) {
                return response.json();
            })
            .then(function(data) {
                if (data.status === "success") {
                    // Update badge
                    var badge = document.getElementById("cart-badge-count");
                    if (badge) {
                        badge.innerText = data.cart_count;
                        badge.style.transform = "scale(1.3)";
                        setTimeout(function() { badge.style.transform = "scale(1)"; }, 300);
                    }

                    // Show Toast
                    showToast(data.message, "success");

                    if (submitBtn) {
                        submitBtn.innerHTML = '<i class="fa-solid fa-check"></i> Added!';
                        setTimeout(function() {
                            submitBtn.disabled = false;
                            submitBtn.innerHTML = originalBtnHtml;
                        }, 1200);
                    }
                } else {
                    formEl.submit();
                }
            })
            .catch(function(err) {
                // fallback to regular form submit
                formEl.submit();
            });
        });
    });
});

// Dynamic Toast Creator
function showToast(message, type) {
    var container = document.getElementById("toast-container");
    if (!container) {
        container = document.createElement("div");
        container.id = "toast-container";
        container.className = "messages-container";
        document.body.appendChild(container);
    }

    var toast = document.createElement("div");
    toast.className = "toast-message toast-" + (type || "info");
    toast.innerHTML = '<i class="fa-solid ' + (type === 'success' ? 'fa-circle-check' : 'fa-circle-info') + '"></i>' +
                      '<span>' + message + '</span>' +
                      '<button class="toast-close" onclick="this.parentElement.remove()">&times;</button>';

    container.appendChild(toast);

    setTimeout(function() {
        toast.style.transition = "opacity 0.5s ease, transform 0.5s ease";
        toast.style.opacity = "0";
        toast.style.transform = "translateX(50px)";
        setTimeout(function() { toast.remove(); }, 500);
    }, 3500);
}