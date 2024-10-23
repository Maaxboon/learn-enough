let elementById = document.getElementById("elementId"); // Access element by ID
let elementsByClassName = document.getElementsByClassName("className"); // Access a collection of elements by class name
let elementsByTagName = document.getElementsByTagName("tagName"); // Access a collection of elements by tag name

// Adding or removing elements
// Create a new element
let newElement = document.createElement("div");
newElement.textContent = "Hello, world!";
document.body.appendChild(newElement); // Add the new element to the document body
document.body.removeChild(newElement); // Remove the element from the document body

// Create a new element
let newElement = document.createElement("div");
newElement.textContent = "Hello, world!";
document.body.appendChild(newElement); // Add the new element to the document body
document.body.removeChild(newElement); // Remove the element from the document body

// Event handling: Event listeners allow you to respond to users actions.
addEventListener("event", function () {});
elementById.addEventListener("click", function () {
  console.log("Element was clicked!");
});

document.addEventListener("DOMContentLoaded", function () {
  const form = document.getElementById("record-form");
  const recordsList = document.getElementById("records-list");
  const totalIncomeEl = document.getElementById("total-income");
  const totalExpenseEl = document.getElementById("total-expense");
  const balanceEl = document.getElementById("balance");
  let draggedIndex = null; // Index of the dragged item
});
