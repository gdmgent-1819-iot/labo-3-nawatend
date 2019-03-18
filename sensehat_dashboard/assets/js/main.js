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





function readEnvironment() {
    let environmentData = firebase.database().ref("/currentEnvironment/");

    environmentData.on("value", function (snapshot) {
        // snapshot.forEach(function (data) {
        //     console.log(data.val());
        // });
        console.log(snapshot.val())
    });
}

// A post entry
var postData = {
    temp: '45'
};

// Write the new post's data simultaneously in the posts list and the user's post list
var updates = {}

updates["/currentEnvironment/"] = postData;

firebase
    .database()
    .ref()
    .update(updates);


readEnvironment()