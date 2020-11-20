<script>
  import ShipsTable from './objects/ShipsTable.js'
	import Dock from './components/Dock.svelte'
	import DraftTable from './components/DraftTable.svelte'
  import { dock,shipSelected } from './stores/planning.js';
  import { baseAddr } from './stores/global.js';
  import axios from 'axios'

  let st = new ShipsTable(10);
  let grid = st.grid

  function deselectShip(e){
    if(!$shipSelected) return;
    document.querySelector('#sticked').remove()
    const newDock = [...$dock,$shipSelected];
    dock.update(_ => newDock);
    shipSelected.update(_ => false)
    if(st.locs.h){
      st.removeShip('h')
    }
    grid = st.grid
  }

  function handleStart(){
    axios({
      method: 'post',
      url: $baseAddr + '/game/new',
      data: {
        grid: st.getSaveData()
      }
    })
    .then(res => {
      console.log(res)
    })
    .catch(res => {
      console.log(res)
    });
  }


</script>

<main>
	<div class="ship-storage">
    <Dock on:deselect={deselectShip}/>
  </div>
  <div class="game-table">
	<DraftTable st={st} grid={grid} on:update={_ => grid = st.grid}/>
  </div>
  <button class="game-button" on:click={handleStart}>HOTOVO</button>
</main>

<style>
.game-table, .ship-storage {
  margin: 20px;
  float: left;
}
.game-button {
  padding: 12px;
  font-size: 1.2em;
  background-color: rgba(0,0,0,0.3);
  color: white;
}

.game-button:hover {
  background-color: rgba(0,0,0,0.6)
}

</style>
