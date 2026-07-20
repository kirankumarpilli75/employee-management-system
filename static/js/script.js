// Employee Management System — custom JS
//
// Conventions expected by this file (used by templates generated later):
//   Toasts:
//     - Any element with class "toast" inside ".toast-container" is auto
//       initialized and shown on page load.
//
//   Image preview (Add/Edit Employee form):
//     - File input:  #id_profile_photo   (Django's default id for the
//                    "profile_photo" form field)
//     - Preview <img>: #photoPreview
//
//   Delete confirmation modal (Employee List / Employee Detail):
//     - Shared modal:      #deleteModal
//     - Modal's <form>:    #deleteForm            (action is set dynamically)
//     - Modal's name slot: #deleteEmployeeName    (text is set dynamically)
//     - Trigger buttons:   class "btn-delete-trigger"
//                          data-delete-url="{% url 'employees:employee_delete' pk %}"
//                          data-employee-name="Full Name"
//
//   Client-side validation:
//     - Any <form class="needs-validation"> gets Bootstrap's standard
//       "was-validated" treatment on submit; invalid forms are blocked
//       client-side. Server-side validation remains the source of truth.

document.addEventListener('DOMContentLoaded', function () {

    /* ---------------------------------------------------------------
     * 1. Auto-show Bootstrap Toast notifications
     * ------------------------------------------------------------- */
    const toastElements = document.querySelectorAll('.toast-container .toast');
    toastElements.forEach(function (toastEl) {
        const toast = bootstrap.Toast.getOrCreateInstance(toastEl);
        toast.show();
    });

    /* ---------------------------------------------------------------
     * 2. Image preview before uploading employee photo
     * ------------------------------------------------------------- */
    const photoInput = document.getElementById('id_profile_photo');
    const photoPreview = document.getElementById('photoPreview');

    if (photoInput && photoPreview) {
        photoInput.addEventListener('change', function (event) {
            const file = event.target.files && event.target.files[0];
            if (!file) {
                return;
            }

            // Basic client-side guard: only preview actual image files.
            if (!file.type.startsWith('image/')) {
                return;
            }

            const reader = new FileReader();
            reader.onload = function (e) {
                photoPreview.src = e.target.result;
                photoPreview.classList.remove('d-none');
            };
            reader.readAsDataURL(file);
        });
    }

    /* ---------------------------------------------------------------
     * 3. Delete confirmation modal support
     * ------------------------------------------------------------- */
    const deleteModalEl = document.getElementById('deleteModal');

    if (deleteModalEl) {
        const deleteForm = document.getElementById('deleteForm');
        const deleteNameSlot = document.getElementById('deleteEmployeeName');

        deleteModalEl.addEventListener('show.bs.modal', function (event) {
            const trigger = event.relatedTarget;
            if (!trigger) {
                return;
            }

            const deleteUrl = trigger.getAttribute('data-delete-url');
            const employeeName = trigger.getAttribute('data-employee-name');

            if (deleteForm && deleteUrl) {
                deleteForm.setAttribute('action', deleteUrl);
            }
            if (deleteNameSlot && employeeName) {
                deleteNameSlot.textContent = employeeName;
            }
        });
    }

    /* ---------------------------------------------------------------
     * 4. Simple client-side validation (Bootstrap pattern)
     * ------------------------------------------------------------- */
    const validatedForms = document.querySelectorAll('form.needs-validation');
    validatedForms.forEach(function (form) {
        form.addEventListener('submit', function (event) {
            if (!form.checkValidity()) {
                event.preventDefault();
                event.stopPropagation();
            }
            form.classList.add('was-validated');
        }, false);
    });

});