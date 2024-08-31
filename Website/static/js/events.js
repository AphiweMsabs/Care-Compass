import { initializeApp } from "https://www.gstatic.com/firebasejs/10.13.0/firebase-app.js";
import { getAnalytics } from "https://www.gstatic.com/firebasejs/10.13.0/firebase-analytics.js";
import { getDatabase, ref, push, set } from "https://www.gstatic.com/firebasejs/10.13.0/firebase-database.js";

// Firebase configuration
const firebaseConfig = {
    apiKey: "AIzaSyC_4AVd9QKo74m77VUfVustsJQDo5joV3M",
    authDomain: "care-compass-25253.firebaseapp.com",
    databaseURL: "https://care-compass-25253-default-rtdb.firebaseio.com",
    projectId: "care-compass-25253",
    storageBucket: "care-compass-25253.appspot.com",
    messagingSenderId: "306549999936",
    appId: "1:306549999936:web:c9a25e370606972d2052a5",
    measurementId: "G-2EXXRY9BER"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);
const database = getDatabase(app);

// Reference to 'messages' node in Firebase Realtime Database
const messageRef = ref(database, 'messages');

// Listen for form submission
document.getElementById('create-events').addEventListener('submit', submitForm);

function submitForm(e) {
    e.preventDefault();
    
    // Get values from the form
    const eventType = getInputValue('eventType');
    const location = getInputValue('location');
    const eventDate = getInputValue('eventDate');
    const province = getInputValue('province');
    const host = getInputValue('host');
    const message = getInputValue('message');

    // Debugging output
    console.log(eventType);
    
    // Save message to Firebase
    saveMessage(eventType, location, eventDate, province, host, message);
}

// Function to get values from the form
function getInputValue(id) {
    return document.getElementById(id).value;
}

// Function to save message to Firebase
function saveMessage(eventType, location, eventDate, province, host, message) {
    const newMessageRef = push(messageRef);
    set(newMessageRef, {
        eventType: eventType,
        location: location,
        eventDate: eventDate,
        province: province,
        host: host,
        message: message,
    });
}
