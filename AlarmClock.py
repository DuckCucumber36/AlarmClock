function setAlarm(minutes) {
    console.log(`Alarm set for ${minutes} minutes.`);
    setTimeout(() => console.log("Time's up!"), minutes * 60000);
}

const minutes = parseInt(prompt("Enter minutes for the alarm:"), 10);
setAlarm(minutes);
 