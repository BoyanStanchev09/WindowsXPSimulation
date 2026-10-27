const taskbarClock = document.getElementById("taskbar-clock");
const localTimeFormatter = new Intl.DateTimeFormat(undefined, {
    hour: "numeric",
    minute: "2-digit",
});

function updateTaskbarClock() {
    const now = new Date();
    taskbarClock.textContent = localTimeFormatter.format(now);
    window.setTimeout(updateTaskbarClock, 60_000 - (now.getTime() % 60_000));
}

updateTaskbarClock();
