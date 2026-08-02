// =========================================================
// MOBILE NAVIGATION
// =========================================================

const menuButton =
    document.getElementById("menuButton");

const mainNavigation =
    document.getElementById("mainNavigation");

menuButton.addEventListener(
    "click",
    () => {
        const isOpen =
            mainNavigation.classList.toggle("open");

        menuButton.setAttribute(
            "aria-expanded",
            String(isOpen)
        );
    }
);

document
    .querySelectorAll(".main-navigation a")
    .forEach((link) => {
        link.addEventListener(
            "click",
            () => {
                mainNavigation.classList.remove(
                    "open"
                );

                menuButton.setAttribute(
                    "aria-expanded",
                    "false"
                );
            }
        );
    });


// =========================================================
// SCROLL REVEAL
// =========================================================

const revealObserver =
    new IntersectionObserver(
        (entries) => {
            entries.forEach((entry) => {
                if (!entry.isIntersecting) {
                    return;
                }

                entry.target.classList.add(
                    "visible"
                );

                revealObserver.unobserve(
                    entry.target
                );
            });
        },
        {
            threshold: 0.1
        }
    );

document
    .querySelectorAll(".reveal")
    .forEach((element) => {
        revealObserver.observe(element);
    });


// =========================================================
// RESEARCH DIALOGS
// =========================================================

document
    .querySelectorAll("[data-dialog]")
    .forEach((button) => {
        button.addEventListener(
            "click",
            () => {
                const dialog =
                    document.getElementById(
                        button.dataset.dialog
                    );

                if (!dialog) {
                    return;
                }

                dialog.showModal();
            }
        );
    });

document
    .querySelectorAll(".dialog-close")
    .forEach((button) => {
        button.addEventListener(
            "click",
            () => {
                button
                    .closest("dialog")
                    .close();
            }
        );
    });

document
    .querySelectorAll("dialog")
    .forEach((dialog) => {
        dialog.addEventListener(
            "click",
            (event) => {
                const rectangle =
                    dialog.getBoundingClientRect();

                const clickedOutside =
                    event.clientX < rectangle.left ||
                    event.clientX > rectangle.right ||
                    event.clientY < rectangle.top ||
                    event.clientY > rectangle.bottom;

                if (clickedOutside) {
                    dialog.close();
                }
            }
        );
    });


// =========================================================
// CURRENT YEAR
// =========================================================

document.getElementById(
    "currentYear"
).textContent =
    new Date().getFullYear();