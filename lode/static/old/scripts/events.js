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


function getLobby(event){
  return new Promise((resolve,reject) => {
    axios({
      method: 'get',
      url: '/lobby',
    })
    .then(function (res) {
      resolve(res);
    })
    .catch(function (res) {
      reject(res);
    })
  })
}


function connect(id){
  console.log('Vytvořit socket na toto id: ' + id);
}
