function deleteNote(noteId) {
  fetch(`/delete-note`, {
    method: 'POST',
    body: JSON.stringify({ noteId: noteId})
  }).then(response => {
      if (response.ok) {
        window.location.reload();
      }
    });
}