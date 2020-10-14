$ = document.querySelector.bind(document);
//$$ = document.querySelectorAll.bind(document);


function createLobby(event){
  event.preventDefault();
  const payload = {
    name: $('#name').value
  }

  axios({
    method: 'post',
    url: '/lobby/new',
    data: payload
  })
  .then(function (res) {
    console.log(res);
  });

}
