
function openTagWindow(tag) {
    // Opens a new window for user to add more tags
    let params = `width=800, height=400, menubar=no, toolbar=no, left=100, top=100`
    
    window.open('/users/add-' + tag, 'Add tags', params);
  }

function closeWindow() {
    // Closes new window, and reloads profile page
    window.close();
    window.opener.location.reload();
  }