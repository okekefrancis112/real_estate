let idVal = 0;
const housingData = [
  {
    id: ++idVal,
    link: "./html/pageListing.html",
    linkTwo: "pageListing.html",
    image: "./assets/images/banner1.jpeg",
    imageTwo: "../assets/images/banner1.jpeg",
    price: 30000,
    location: "44B, Ejigbo, Lagos, Nigeria",
  },
  {
    id: ++idVal,
    link: "./html/pageListing.html",
    linkTwo: "pageListing.html",
    image: "./assets/images/banner2.jpeg",
    imageTwo: "../assets/images/banner2.jpeg",
    price: 40000,
    location: "44B, Ejigbo, Lagos, Nigeria",
  },
  {
    id: ++idVal,
    link: "./html/pageListing.html",
    linkTwo: "pageListing.html",
    image: "./assets/images/banner3.jpeg",
    imageTwo: "../assets/images/banner3.jpeg",
    price: 60000,
    location: "44B, Ejigbo, Lagos, Nigeria",
  },
  {
    id: ++idVal,
    link: "./html/pageListing.html",
    linkTwo: "pageListing.html",
    image: "./assets/images/banner4.jpeg",
    imageTwo: "../assets/images/banner4.jpeg",
    price: 45000,
    location: "44B, Ejigbo, Lagos, Nigeria",
  },
  {
    id: ++idVal,
    link: "./html/pageListing.html",
    linkTwo: "pageListing.html",
    image: "./assets/images/img1.jpeg",
    imageTwo: "../assets/images/img1.jpeg",
    price: 35000,
    location: "44B, Ejigbo, Lagos, Nigeria",
  },
  {
    id: ++idVal,
    link: "./html/pageListing.html",
    linkTwo: "pageListing.html",
    image: "./assets/images/img2.jpeg",
    imageTwo: "../assets/images/img2.jpeg",
    price: 55000,
    location: "44B, Ejigbo, Lagos, Nigeria",
  },
  {
    id: ++idVal,
    link: "./html/pageListing.html",
    linkTwo: "pageListing.html",
    image: "./assets/images/img3.jpg",
    imageTwo: "../assets/images/img3.jpg",
    price: 65000,
    location: "44B, Ejigbo, Lagos, Nigeria",
  },
  {
    id: ++idVal,
    link: "./html/pageListing.html",
    linkTwo: "pageListing.html",
    image: "./assets/images/img4.jpeg",
    imageTwo: "../assets/images/img4.jpeg",
    price: 63000,
    location: "44B, Ejigbo, Lagos, Nigeria",
  },
  {
    id: ++idVal,
    link: "./html/pageListing.html",
    linkTwo: "pageListing.html",
    image: "./assets/images/img5.jpeg",
    imageTwo: "../assets/images/img5.jpeg",
    price: 63000,
    location: "44B, Ejigbo, Lagos, Nigeria",
  },
  {
    id: ++idVal,
    link: "./html/pageListing.html",
    linkTwo: "pageListing.html",
    image: "./assets/images/img6.jpeg",
    imageTwo: "../assets/images/img6.jpeg",
    price: 63000,
    location: "44B, Ejigbo, Lagos, Nigeria",
  },
  {
    id: ++idVal,
    link: "./html/pageListing.html",
    linkTwo: "pageListing.html",
    image: "./assets/images/banner1.jpeg",
    imageTwo: "../assets/images/banner1.jpeg",
    price: 30000,
    location: "44B, Ejigbo, Lagos, Nigeria",
  },
  {
    id: ++idVal,
    link: "./html/pageListing.html",
    linkTwo: "pageListing.html",
    image: "./assets/images/banner2.jpeg",
    imageTwo: "../assets/images/banner2.jpeg",
    price: 40000,
    location: "44B, Ejigbo, Lagos, Nigeria",
  },
  {
    id: ++idVal,
    link: "./html/pageListing.html",
    linkTwo: "pageListing.html",
    image: "./assets/images/banner3.jpeg",
    imageTwo: "../assets/images/banner3.jpeg",
    price: 60000,
    location: "44B, Ejigbo, Lagos, Nigeria",
  },
  {
    id: ++idVal,
    link: "./html/pageListing.html",
    linkTwo: "pageListing.html",
    image: "./assets/images/banner4.jpeg",
    imageTwo: "../assets/images/banner4.jpeg",
    price: 45000,
    location: "44B, Ejigbo, Lagos, Nigeria",
  },
  {
    id: ++idVal,
    link: "./html/pageListing.html",
    linkTwo: "pageListing.html",
    image: "./assets/images/img1.jpeg",
    imageTwo: "../assets/images/img1.jpeg",
    price: 35000,
    location: "44B, Ejigbo, Lagos, Nigeria",
  },
  {
    id: ++idVal,
    link: "./html/pageListing.html",
    linkTwo: "pageListing.html",
    image: "./assets/images/img2.jpeg",
    imageTwo: "../assets/images/img2.jpeg",
    price: 55000,
    location: "44B, Ejigbo, Lagos, Nigeria",
  },
  {
    id: ++idVal,
    link: "./html/pageListing.html",
    linkTwo: "pageListing.html",
    image: "./assets/images/img3.jpg",
    imageTwo: "../assets/images/img3.jpg",
    price: 65000,
    location: "44B, Ejigbo, Lagos, Nigeria",
  },
  {
    id: ++idVal,
    link: "./html/pageListing.html",
    linkTwo: "pageListing.html",
    image: "./assets/images/img4.jpeg",
    imageTwo: "../assets/images/img4.jpeg",
    price: 63000,
    location: "44B, Ejigbo, Lagos, Nigeria",
  },
  {
    id: ++idVal,
    link: "./html/pageListing.html",
    linkTwo: "pageListing.html",
    image: "./assets/images/img5.jpeg",
    imageTwo: "../assets/images/img5.jpeg",
    price: 63000,
    location: "44B, Ejigbo, Lagos, Nigeria",
  },
  {
    id: ++idVal,
    link: "./html/pageListing.html",
    linkTwo: "pageListing.html",
    image: "./assets/images/img6.jpeg",
    imageTwo: "../assets/images/img6.jpeg",
    price: 63000,
    location: "44B, Ejigbo, Lagos, Nigeria",
  },
];

const buttonContainer = document.querySelector(".buttons");
const allBtns = document.querySelectorAll(".page_btns");
const parentContainer = document.querySelector(".properties_grid");
const imageClick = document.querySelectorAll(".props_img");
const pageList = document.querySelector(".housingData_image img");

const itemsPerPage = 8;
const currentPageNumber = 1;

//Function to create the image elements and to populate them

display = (wrapper, itemsArray, currentPageNumber, pageContentNumber) => {
  let end = currentPageNumber * pageContentNumber;
  let start = end - pageContentNumber;
  wrapper.innerHTML = "";

  for (let i = start; i < end; i++) {
    let item = itemsArray[i];

    //The main div
    const mainDiv = document.createElement("div");
    mainDiv.setAttribute("class", "property_image");

    //The link
    const myLink = document.createElement("a");
    myLink.setAttribute(
      "href",
      document.URL.includes("index.html") ? item.link : item.linkTwo
    );

    //The image
    const myImage = document.createElement("img");
    myImage.setAttribute("class", "props_img");
    myImage.src = document.URL.includes("index.html")
      ? item.image
      : item.imageTwo;

    //The child div
    const childDiv = document.createElement("div");
    childDiv.setAttribute("class", "property_info");

    //The spans
    const priceSpan = document.createElement("span");
    priceSpan.innerText = "$" + item.price;

    const locationSpan = document.createElement("span");
    locationSpan.innerText = "$" + item.location;

    //Merging all the elements
    myLink.appendChild(myImage);
    childDiv.append(priceSpan, locationSpan);
    mainDiv.append(myLink, childDiv);

    //Adding the mainDiv to its parent element in the DOM
    wrapper.appendChild(mainDiv);
  }
};

//Function to create the buttons

createButtons = (
  btnWrapper,
  currentPageNumber,
  itemsArray,
  pageContentNumber
) => {
  //Some variables
  let btnLink;
  let theLength = itemsArray.length / pageContentNumber;

  //For loop to create buttons based on theLength calculated
  for (let j = 0; j < Math.ceil(theLength); j++) {
    btnLink = document.createElement("a");
    btnLink.setAttribute("href", "#property_head");
    btnLink.setAttribute("class", "page_btns");
    btnLink.textContent = j + 1;
    btnWrapper.appendChild(btnLink);
  }

  //Adding an event listener to the buttons to update the page number
  let allBtns = btnWrapper.querySelectorAll(".page_btns");
  allBtns.forEach((btn) => {
    btn.addEventListener("click", () => {
      currentPageNumber = parseInt(btn.innerText);
      display(parentContainer, housingData, currentPageNumber, itemsPerPage);
    });
  });
};

//Calling the display and create button function populate page function
const populatePage = () => {
  createButtons(buttonContainer, currentPageNumber, housingData, itemsPerPage);
  display(parentContainer, housingData, currentPageNumber, itemsPerPage);
};

populatePage();

//Setting items to display to the localstorage

if (window.innerWidth < 450) {
  if (document.URL.includes("index.html")) {
    pageList.style = true;
  } else {
    pageList.style.height = window.innerWidth - window.innerWidth * 0.1 + "px";
  }
}
