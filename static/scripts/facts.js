fact = document.querySelector(".fact");
fetch("http://numbersapi.com/random/year?json")
  .then((response) => {
    // console.log("resolved", response);
    // Gets the json data
    return response.json();
  })
  .then((data) => {
    console.log(data);
    // document.write(data.text);
    fact.innerHTML = data.text;
  })

  .catch((err) => {
    console.log("rejected", err);
  });

// Use this api later
// http://numbersapi.com/7/
