import bot from './assets/bot.svg';
import user from './assets/user.svg';


/* target HTML elements using document.querySelector */
const form = document.querySelector('form');
const chatContainer = document.querySelector('#chat_container');
const sideMenu = document.querySelector('#side_menu');
const newChat = document.querySelector('#new_chat');

let loadInterval;

// /* generate side menu history of chats */
// function sideMenu() {
//   return (
//     `<div class="side_menu"></div>`
//   )
// }

/* implement bot loading before outputting response */
function loader(element) {
  element.textContent = '';

  loadInterval = setInterval(() => {
    element.textContent += '.';

    if (element.textContent === '....') {
      element.textContent = '';
    }
  }, 300)
}

/* implement typing functionality one letter at a time */
function typeText(element, text) {
  let index = 0;

  let interval = setInterval(() => {
    if(index < text.length) {
      element.innerHTML += text.charAt(index);
      index++;
    } else {
      clearInterval(interval);
    }
  }, 20)
}

/* generate a unique id for each message, via timestamping, to map over them. */
function generateUniqueId() {
  const timestamp = Date.now();
  const randomNumber = Math.random();
  const hexadecimalString = randomNumber.toString(16);

  return `id-${timestamp}-${hexadecimalString}`;
}

/* implement chat stripe for bot and user */
function chatStripe (isAi, value, uniqueId) {
  return (
    `
    <div class="wrapper ${isAi && 'ai'}">
      <div class="chat">
        <div className="profile">
          <img 
            src="${isAi ? bot : user}"
            alt="${isAi ? 'bot' : 'user'}"
          />
        </div>
        <div class="message" id=${uniqueId}>${value}</div>
      </div>
    </div>
    `
  )
}

/* create handleSubmit to trigger getting the Ai generated response */
const handleSubmit = async (e) => {
  e.preventDefault(); // prevent default browser reload

  const data = new FormData(form); // get the data typed into form

  // generate new user chat stripe
  chatContainer.innerHTML += chatStripe(false, data.get('prompt'))

  // clear text input
  form.reset();

  // generate new bot chat stripe
  const uniqueId = generateUniqueId();
  chatContainer.innerHTML += chatStripe(true, " ", uniqueId)

  // keep scrolling as new chats appear and stay in view
  chatContainer.scrollTop = chatContainer.scrollHeight;

  // fetch the new message
  const messageDiv = document.getElementById(uniqueId);
  
  // load the new message
  loader(messageDiv);
}

/* regulate changes in submit events */
form.addEventListener('submit', handleSubmit);
form.addEventListener('keyup', (e) => {
  if (e.keyCode === 13) {
    handleSubmit(e);
  }
})


/* connect to openAI */

