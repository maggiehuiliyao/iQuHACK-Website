document.querySelector("form").addEventListener("submit", function(event) {
    event.preventDefault();
    // Get values of input fields
    const from = document.querySelector("#from").value;
    const to = document.querySelector("#to").value;
    const budget = document.querySelector("#budget").value;})
