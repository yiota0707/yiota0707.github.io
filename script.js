// =========================================================
// MOBILE MENU
// =========================================================

const mobileMenuButton =
    document.getElementById("mobileMenuButton");

const sidebar =
    document.getElementById("sidebar");

mobileMenuButton.addEventListener(
    "click",
    () => {
        const isOpen =
            sidebar.classList.toggle("open");

        mobileMenuButton.setAttribute(
            "aria-expanded",
            String(isOpen)
        );
    }
);

document
    .querySelectorAll(".sidebar-navigation a")
    .forEach((link) => {
        link.addEventListener(
            "click",
            () => {
                sidebar.classList.remove("open");

                mobileMenuButton.setAttribute(
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
                if (entry.isIntersecting) {
                    entry.target.classList.add(
                        "visible"
                    );

                    revealObserver.unobserve(
                        entry.target
                    );
                }
            });
        },
        {
            threshold: 0.12
        }
    );

document
    .querySelectorAll(".reveal")
    .forEach((element) => {
        revealObserver.observe(element);
    });


// =========================================================
// ACTIVE SIDEBAR SECTION
// =========================================================

const pageSections =
    document.querySelectorAll(
        "main section[id]"
    );

const navigationLinks =
    document.querySelectorAll(
        ".nav-link"
    );

const sectionObserver =
    new IntersectionObserver(
        (entries) => {
            entries.forEach((entry) => {
                if (!entry.isIntersecting) {
                    return;
                }

                navigationLinks.forEach(
                    (link) => {
                        link.classList.remove(
                            "active"
                        );

                        const target =
                            link.getAttribute(
                                "href"
                            );

                        if (
                            target ===
                            `#${entry.target.id}`
                        ) {
                            link.classList.add(
                                "active"
                            );
                        }
                    }
                );
            });
        },
        {
            rootMargin:
                "-35% 0px -55% 0px"
        }
    );

pageSections.forEach((section) => {
    sectionObserver.observe(section);
});


// =========================================================
// POPUPS
// =========================================================

const popupButtons =
    document.querySelectorAll(
        "[data-popup]"
    );

const popupCloseButtons =
    document.querySelectorAll(
        "[data-close-popup]"
    );

const popups =
    document.querySelectorAll(
        ".popup"
    );

function openPopup(popupId) {
    const popup =
        document.getElementById(
            popupId
        );

    if (!popup) {
        return;
    }

    popup.classList.add("active");

    popup.setAttribute(
        "aria-hidden",
        "false"
    );

    document.body.classList.add(
        "popup-active"
    );
}

function closePopup(popup) {
    if (!popup) {
        return;
    }

    popup.classList.remove("active");

    popup.setAttribute(
        "aria-hidden",
        "true"
    );

    document.body.classList.remove(
        "popup-active"
    );
}

popupButtons.forEach((button) => {
    button.addEventListener(
        "click",
        () => {
            openPopup(
                button.dataset.popup
            );
        }
    );
});

popupCloseButtons.forEach((button) => {
    button.addEventListener(
        "click",
        () => {
            closePopup(
                button.closest(".popup")
            );
        }
    );
});

document.addEventListener(
    "keydown",
    (event) => {
        if (event.key !== "Escape") {
            return;
        }

        popups.forEach((popup) => {
            if (
                popup.classList.contains(
                    "active"
                )
            ) {
                closePopup(popup);
            }
        });
    }
);


// =========================================================
// CURRENT YEAR
// =========================================================

document.getElementById(
    "currentYear"
).textContent =
    new Date().getFullYear();