
function openSkillWindow() {
    // Open a new window for user to add more skills
    let params = `width=800, height=400, menubar=no, toolbar=no, left=100, top=100`

    skillWindow = window.open('/users/add-skill', 'Add Skills', params);
  }

function closeWindow() {
    // Closes new window, and reloads profile page
    window.close();
    window.opener.location.reload();
  }