/* Get the input and messages elements from the HTML */
const inputElement = document.getElementById("input");
const messagesElement = document.getElementById("messages");

/* Listen for keydown events on the input element */
inputElement.addEventListener("keydown", async (event) => {
  /* Check if the Enter key was pressed */
  if (event.key === "Enter") {
    /* Get the user's input from the input element */
    const user_input = inputElement.value;
    /* Clear the input element */
    inputElement.value = "";
    /* Add the user's input to the messages element */
    messagesElement.innerHTML += `<p><strong>You:</strong> ${user_input}</p>`;

    /* Send a request to the API endpoint with the user's input */
    const response = await fetch("enter your api gateway link", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ user_input }),
    });

    /* Parse the response data as JSON */
    const data = await response.json();
    const responseBody = JSON.parse(data.body);

    /* Add the bot's response to the messages element */
    messagesElement.innerHTML += `<p class="chat-message"><strong>Bot:</strong> ${responseBody.response}</p>`;
  }
});
