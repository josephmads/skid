function openSkillWindow() {
    // Open a new window with a specified URL
    let params = `width=800, height=400, menubar=no, toolbar=no, left=100, top=100`

    window.open('/users/add-skill', 
                'Add Skills', 
                params
                );
  }