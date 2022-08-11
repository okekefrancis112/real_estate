const lerp = (start, end, ratio) => {
  return (1 - ratio) * start + ratio * end;
};

// ============= Burger ===============
const burger = document.querySelector(".burger");
const navLinks = document.querySelector(".nav_links");
const navLinksLinks = document.querySelectorAll(".nav_links a");
burger.onclick = () => {
  burger.children[0].classList.toggle("open");
  navLinks.classList.toggle("slide_in_from_left");
};
navLinksLinks.forEach((link) => {
  link.onclick = () => {
    burger.children[0].classList.remove("open");
    navLinks.classList.remove("slide_in_from_left");
  };
});

// ================ loading Animation ================

const loadingAnimation = document.querySelector(".loading_animation"),
  loadingAnimationHeading = document.querySelector(".loading_animation img"),
  body = document.querySelector("body");

loadingAnimationHeading.style.transform = `translate(${lerp(0, 0, 0.1)}%)`;
window.onload = () => {
  loadingAnimation.style.opacity = lerp(0, 0, 0.005);
  body.style.overflow = "auto";
};

// ====================== New properties for you animation ================
const properties = document.querySelectorAll(".animate_up");

const generalcallback = (entries) => {
  entries.forEach((entry) => {
    if (entry.isIntersecting) {
      entry.target.style.transform = `translate(${lerp(0, 0, 0.1)}%)`;
      entry.target.style.opacity = lerp(1, 0, 0.005);
    }
  });
};

const generalOption = {
  threshold: 0.2,
};

const generalObserver = new IntersectionObserver(
  generalcallback,
  generalOption
);

properties.forEach((property) => {
  generalObserver.observe(property);
});
