document.getElementById('personForm').addEventListener('submit', function(e) {
    e.preventDefault();
    const name = document.getElementById('name').value;
    const age = document.getElementById('age').value;

    fetch('/add_person', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ name: name, age: age })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            loadPeople();
        }
    });
});

function loadPeople() {
    fetch('/get_people')
    .then(response => response.json())
    .then(data => {
        const peopleList = document.getElementById('peopleList');
        peopleList.innerHTML = '';
        data.forEach(person => {
            const div = document.createElement('div');
            div.className = 'person';
            div.innerHTML = `<span>${person.name} (${person.age})</span>`;
            peopleList.appendChild(div);
        });
    });
}

document.addEventListener('DOMContentLoaded', loadPeople);
