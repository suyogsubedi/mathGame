let websiteList = document.querySelector(".website-list");
let tempMessage = document.querySelector(".temp-message");
const baseURL = "http://localhost:3000/";
// Template
const generateTemplate = (websiteName, websiteURL, isFree, imageSource) => {
  const html = `
    <li class="website card">
    <img class="website-logo" src=${imageSource} alt="Website Logo"> <br>
    <span class="website-name">${websiteName}</span> <br>
    <a href=${websiteURL} class="website-url " target="_blank">Click Here</a>
    <br>
    <span class="free-to-use">  ${isFree}</span>
    
  </li>
    `;
  websiteList.innerHTML += html;
};

// Loading Screen Template

fetch("http://localhost:3000/")
  .then((response) => {
    return response.json();
  })
  .then((data) => {
    if (data) {
      tempMessage.innerHTML = "";
      for (let i = 0; i < data.length; i++) {
        generateTemplate(
          data[i].websiteName,
          data[i].url,
          data[i].free,
          baseURL + data[i].image
        );
      }
    }
  });
