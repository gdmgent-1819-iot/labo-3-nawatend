// Initialize Firebase
let config = {
    apiKey: "AIzaSyAfx2W4GkPmsqV0Ag6hK6VQQjAAmvI3RqA",
    authDomain: "environment-pi.firebaseapp.com",
    databaseURL: "https://environment-pi.firebaseio.com",
    projectId: "environment-pi",
    storageBucket: "environment-pi.appspot.com",
    messagingSenderId: "484802952614"
};

firebase.initializeApp(config);




// elements to get value from firebase
let temp = document.getElementById('temp')
let humi = document.getElementById('humi')
let pres = document.getElementById('pres')

//colorPicker element
let colorPicker = document.getElementById('colorpicker')
let sendColor = document.getElementById('sendcolor')
let colorDiv = document.getElementById('ambilight_light')
const readEnvironment = () => {
    let environmentData = firebase.database().ref("/environment/");

    environmentData.on("value", function (snapshot) {
        // snapshot.forEach(function (data) {
        //     console.log(data.val());
        // });
        temp.innerText = snapshot.val()['temperature'].value + ' ' + snapshot.val()['temperature'].unit
        humi.innerText = snapshot.val()['humidity'].value + ' ' + snapshot.val()['humidity'].unit
        pres.innerText = snapshot.val()['pressure'].value + ' ' + snapshot.val()['pressure'].unit

        console.log(snapshot.val()['pressure'].value + ' ' + snapshot.val()['pressure'].unit)

    });
}

const sendColorToFirebase = () => {

    let environmentData = firebase.database().ref("/ambilight/");

    let color_obj = {
        color: colorPicker.value,
    }
    var updates = {}

    updates["/ambilight/"] = color_obj;

    firebase
        .database()
        .ref()
        .update(updates);

    colorDiv.style.backgroundColor = colorPicker.value
}
// A post entry


// Write the new post's data simultaneously in the posts list and the user's post list
// var updates = {}

// updates["/currentEnvironment/"] = postData;

// firebase
//     .database()
//     .ref()
//     .update(updates);


readEnvironment()

sendColor.addEventListener('click', () => {
    sendColorToFirebase()

})