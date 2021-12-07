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
  boilerplate = `${firstValue} + ${secondValue} = `;
  let result = parseInt(firstValue) + parseInt(secondValue);
  additionResult.innerHTML = boilerplate + result;
});

subtractionForm.addEventListener("submit", (e) => {
  e.preventDefault();
  const firstValue = subtractionForm.querySelector(".subtractionFN").value;
  const secondValue = subtractionForm.querySelector(".subtractionSN").value;
  boilerplate = `${firstValue} - ${secondValue} = `;
  let result = parseInt(firstValue) - parseInt(secondValue);
  subtractionResult.innerHTML = boilerplate + result;
});

multiplicationForm.addEventListener("submit", (e) => {
  e.preventDefault();
  const firstValue =
    multiplicationForm.querySelector(".multiplicationFN").value;
  const secondValue =
    multiplicationForm.querySelector(".multiplicationSN").value;
  boilerplate = `${firstValue} * ${secondValue} = `;
  let result = parseInt(firstValue) * parseInt(secondValue);
  multiplicationResult.innerHTML = boilerplate + result;
});

divisionForm.addEventListener("submit", (e) => {
  e.preventDefault();
  const firstValue = divisionForm.querySelector(".divisionFN").value;
  const secondValue = divisionForm.querySelector(".divisionSN").value;
  boilerplate = `${firstValue} / ${secondValue} = `;
  let result = parseInt(firstValue) / parseInt(secondValue);
  divisionResult.innerHTML = boilerplate + result;
});
