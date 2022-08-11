// ================ Hero Images Animation ===============
const heroImageContainer = document.querySelector(".hero_images");

const options = {
  root: heroImageContainer,
  threshold: 0.3,
};

let scrollLeft, scrollRight;

// ================= First Observer ==================

const callback = (entries) => {
  if (entries[0].isIntersecting) {
    clearInterval(scrollLeft);
    scrollRight = setInterval(() => {
      heroImageContainer.scrollBy({
        top: 0,
        left: 400,
        behavior: "smooth",
      });
    }, 5000);
  }
};

const observer = new IntersectionObserver(callback, options);
observer.observe(heroImageContainer.children[0]);

// ================= Second Observer ==================

const callbackTwo = (entries) => {
  if (entries[0].isIntersecting) {
    clearInterval(scrollRight);
    scrollLeft = setInterval(() => {
      heroImageContainer.scrollBy({
        top: 0,
        left: -400,
        behavior: "smooth",
      });
    }, 5000);
  }
};
const observerTwo = new IntersectionObserver(callbackTwo, options);
observerTwo.observe(
  heroImageContainer.children[heroImageContainer.children.length - 1]
);

// ============= Hero text Container animation ==============
const heroText = document.querySelector(".hero_text");
heroText.style.transform = `translate(${lerp(0, 0, 0.1)}%)`;
heroText.style.opacity = lerp(1, 0, 0.005);

const evidence = document.querySelector("#evidence");
evidence.onclick = (e) => {
  const thisOne = e.target;
  imagesArray = thisOne.parentElement.nextElementSibling.children[0].src;
  localStorage.setItem("data", imagesArray);
};
