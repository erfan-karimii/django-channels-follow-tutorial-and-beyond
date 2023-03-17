document.querySelector('#room-name-input').onkeyup = function(e) {
    if (e.keyCode === 13) {  // enter, return
        document.querySelector('#room-name-submit').click();
    }
};

document.querySelector('#room-name-submit').onclick = function(e) {
    var roomName = document.querySelector('#room-name-input').value;
    if (roomName){
        window.location.pathname = '/chat/' + roomName + '/';
    }
};

document.querySelector('#random-generator').onclick = function(e) {
    document.querySelector('#room-name-input').value = uuidv4();
};
function uuidv4() {
    return ([1e7]+1e3+4e3+8e3+1e11).replace(/[018]/g, c =>
      (c ^ crypto.getRandomValues(new Uint8Array(1))[0] & 15 >> c / 4).toString(16)
    );
  }