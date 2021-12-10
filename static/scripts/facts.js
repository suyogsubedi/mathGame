fact = document.querySelector(".fact");
fetch("http://numbersapi.com/random/year?json")
  .then((response) => {
    console.log("resolved", response);
    // Gets the json data
    return response.json();
  })
  .then((data) => {
    fact.innerHTML = data.text;
  })
  .catch((err) => {
    console.log("rejected", err);
  });
