const dashboard = document.querySelector(".dashboard");
const edit = document.getElementById("edit-info");
const form = document.querySelector("form");
const allInputs = document.querySelectorAll("form input");
const update = document.getElementById("update");
edit.onclick = () => {
  allInputs.forEach((input) => {
    input.removeAttribute("disabled");
    input.classList.add("edit");

    form.classList.add("blur-effect");
    setTimeout(() => {  
      form.classList.remove("blur-effect");
    }, 2000);
  });
};

update.onsubmit = (e) => {
  e.preventDefault();
  allInputs.forEach((input) => {
    input.classList.remove("edit");
    input.setAttribute("disabled", true);
    updateToast.classList.add("animate__toast");
    setTimeout(() => {
      updateToast.classList.remove("animate__toast");
    }, 5000);
  });
};

const allNavs = document.querySelectorAll(".navs");
const statsContent = document.querySelector(".stats__content");
const profileContent = document.querySelector(".profile__content");

allNavs.forEach((nav) => {
  nav.onclick = () => {
    for (let i = 0; i < allNavs.length; i++) {
      allNavs[i].classList.remove("active");
    }
    nav.classList.add("active");
    if (nav.classList.contains("stats")) {
      profileContent.classList.remove("show");
      statsContent.classList.add("show");
      dashboard.classList.remove("slide__in");
    }
    if (nav.classList.contains("profile")) {
      statsContent.classList.remove("show");
      profileContent.classList.add("show");
      dashboard.classList.remove("slide__in");
    }
  };
});

const menuButton = document.querySelector(".menu__list");
const times = document.querySelector("#times");

menuButton.onclick = (e) => {
  dashboard.classList.toggle("slide__in");
};
times.onclick = (e) => {
  dashboard.classList.remove("slide__in");
};

const clientDetailsContainer = document.querySelector(".client__details");
const scrollUpBtn = document.querySelector("#up");
const scrollDownBtn = document.querySelector("#down");

scrollUpBtn.onclick = () => {
  clientDetailsContainer.scrollBy({
    top: 200,
    left: 0,
    behavior: "smooth",
  });
};

scrollDownBtn.onclick = () => {
  clientDetailsContainer.scrollBy({
    top: -200,
    left: 0,
    behavior: "smooth",
  });
};

const code = document.getElementById("referral__code");
const copyBtn = document.querySelector("#copy");
const updateBtn = document.querySelector("#update");
const copyToast = document.querySelector("#copy-toast");
const updateToast = document.querySelector("#update-profile-toast");

copyBtn.onclick = () => {
  navigator.permissions.query({ name: "clipboard-write" }).then((result) => {
    if (result.state == "granted" || result.state == "prompt") {
      navigator.clipboard.writeText(code.value).then(
        () => {
          copyToast.classList.add("animate__toast");
          setTimeout(() => {
            copyToast.classList.remove("animate__toast");
          }, 5000);
        },
        () => {
          alert("failed");
        }
      );
    }
  });
};
