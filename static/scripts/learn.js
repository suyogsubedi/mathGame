// Addition Form
let additionForm = document.querySelector(".addition");
let additionResult = document.querySelector(".additionResult");
let subtractionForm = document.querySelector(".subtraction");
let subtractionResult = document.querySelector(".subtractionResult");
let multiplicationForm = document.querySelector(".multiplication");
let multiplicationResult = document.querySelector(".multiplicationResult");
let divisionForm = document.querySelector(".division");
let divisionResult = document.querySelector(".divisionResult");

additionForm.addEventListener("submit", (e) => {
  e.preventDefault();
  const firstValue = additionForm.querySelector(".additionFN").value;
  const secondValue = additionForm.querySelector(".additionSN").value;
  if (firstValue)
    additionResult.innerHTML = parseInt(firstValue) + parseInt(secondValue);
});

subtractionForm.addEventListener("submit", (e) => {
  e.preventDefault();
  const firstValue = subtractionForm.querySelector(".subtractionFN").value;
  const secondValue = subtractionForm.querySelector(".subtractionSN").value;
  if (firstValue)
    subtractionResult.innerHTML = parseInt(firstValue) - parseInt(secondValue);
});

multiplicationForm.addEventListener("submit", (e) => {
  e.preventDefault();
  const firstValue =
    multiplicationForm.querySelector(".multiplicationFN").value;
  const secondValue =
    multiplicationForm.querySelector(".multiplicationSN").value;
  if (firstValue)
    multiplicationResult.innerHTML =
      parseInt(firstValue) * parseInt(secondValue);
});

divisionForm.addEventListener("submit", (e) => {
  e.preventDefault();
  const firstValue = divisionForm.querySelector(".divisionFN").value;
  const secondValue = divisionForm.querySelector(".divisionSN").value;
  if (firstValue)
    divisionResult.innerHTML = parseInt(firstValue) / parseInt(secondValue);
});
