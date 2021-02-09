<script>
  import { winner } from './stores/global.js';
  import { socket,myTable,enemyTable,myTableHoles } from './stores/game.js';
  import * as lode from './lodeLib.js';

  function iterate(grid,cb){
    for (let line of grid){
      for (let cell of line){
        cb(cell)
      }
    }
  }

  let shot = 0;
  let hit = 0;
  iterate($enemyTable, x => {
    if (x > 0) shot += 1;
    if (x == 2) hit += 1;
  })
  let rate = hit / (shot / 100)

  let enemyShot = 0
  let enemyHit = 0
  iterate($myTableHoles, x => {
    if (x > 0) enemyShot += 1;
    if (x == 2) enemyHit += 1;
  })

  let enemyRate = enemyHit / (enemyShot / 100)


  function handleBack(){
    location.reload(); 
  }

</script>

<main>
  <div class="wrap">
    {#if $winner == 'player'}
      <h1>Vyhráli jste</h1>
    {:else}
      <h1>Prohráli jste</h1>
    {/if}

    <h3>Vy</h3>

      <h4>Vystřelů: {shot}</h4>

      <h4>Zásahů: {hit} / 17</h4>

      <h4>Úspěšnost zásahů: {Math.round(rate * 100)/100}%</h4>

      <div class="split"></div>

    <h3>Nepřítel</h3>

      <h4>Vystřelů: {enemyShot}</h4>

      <h4>Zásahů: {enemyHit} / 17</h4>

      <h4>Úspěšnost zásahů: {Math.round(enemyRate * 100)/100}%</h4>

    <button on:click={handleBack}>Zpět</button>
  </div>
</main>

<style>
.wrap {
  width: 350px;
  height: 550px;
  margin: 15px auto;
  background: rgba(0,0,0,0.3);
  color: white;
  border: solid 2px var(--blue1);
  text-align: center;
}

button {
  background: rgba(0,0,0,0.3);
  color: white;
  padding: 10px;
  margin: 15px auto;
  font-size: 1.3em;
}

button:hover {
  background: var(--blue1);
}

.split {
  width: 100%;
  height: 2px;
  background: var(--blue1);
}

h1 {
  text-align: center;
  padding: 5px;
}
</style>
