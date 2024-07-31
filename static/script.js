document.addEventListener('DOMContentLoaded', function () {
    var calendarEl = document.getElementById('calendar');
    var eventsData = JSON.parse(document.getElementById('events-data').innerText);

    var calendar = new FullCalendar.Calendar(calendarEl, {
        initialView: 'dayGridMonth',
        events: eventsData.map(item => ({
            title: item.name,
            start: item.date,
            description: item.description
        }))
    });

    calendar.render();
});

function showAddItemForm() {
    document.getElementById('add-item-form').style.display = 'block';
}

function closeAddItemForm() {
    document.getElementById('add-item-form').style.display = 'none';
}

function showToday() {
    document.getElementById('main-title').innerText = 'Today';
    document.getElementById('today-items').style.display = 'block';
    document.getElementById('upcoming-items').style.display = 'none';
}

function showUpcoming() {
    document.getElementById('main-title').innerText = 'Upcoming';
    document.getElementById('today-items').style.display = 'none';
    document.getElementById('upcoming-items').style.display = 'block';
}

function showUpdateForm(id, name, description, date) {
    document.getElementById('update_id').value = id;
    document.getElementById('update_name').value = name;
    document.getElementById('update_description').value = description;
    document.getElementById('update_date').value = date;
    document.getElementById('updateForm').style.display = 'block';
}

function closeUpdateForm() {
    document.getElementById('updateForm').style.display = 'none';
}
