 // Получаем все кнопки по ID
  const newHabitsBtn = document.getElementById('new-habits');
  const oldHabitsBtn = document.getElementById('old-habits');
  const habitListBtn = document.getElementById('habit-list');

  function setActiveButton(activeButton) {
    // Снимаем активный класс с каждой кнопки
    newHabitsBtn.classList.remove('btn-outline-primary');
    oldHabitsBtn.classList.remove('btn-outline-primary');
    habitListBtn.classList.remove('btn-outline-primary');

    // Все кнопки становятся btn-outline-secondary
    newHabitsBtn.classList.add('btn-outline-secondary');
    oldHabitsBtn.classList.add('btn-outline-secondary');
    habitListBtn.classList.add('btn-outline-secondary');

    // Назначаем активный класс на нужную кнопку
    activeButton.classList.remove('btn-outline-secondary');
    activeButton.classList.add('btn-outline-primary');
  }

  // Устанавливаем обработчики на кнопки
  newHabitsBtn.addEventListener('click', function(event) {
    event.preventDefault();
    setActiveButton(newHabitsBtn);
  });

  oldHabitsBtn.addEventListener('click', function(event) {
    event.preventDefault();
    setActiveButton(oldHabitsBtn);
  });

  habitListBtn.addEventListener('click', function(event) {
    event.preventDefault();
    setActiveButton(habitListBtn);
  });