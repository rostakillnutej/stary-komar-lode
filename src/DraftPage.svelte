<script>
	import Dock from './components/Dock.svelte'
	import DraftTable from './components/DraftTable.svelte'
  import { socket,table,tableSize,dock,shipSelected } from './stores/planning.js';
  import { baseAddr } from './stores/global.js';
  import axios from 'axios'
  import { onMount } from 'svelte';
  import io from 'socket.io-client';
  import * as lode from './lodeLib.js';

	//Připojuje se na server
  socket.update(_ => io($baseAddr + '/plan'))

	//Event který se zavolá když je připojeno
  $socket.on('connect', data => {
    console.log('Socket OK')
  });
	//Event na získání lodí
  $socket.emit('getShips');
	//Event který čeká na vrácení lodí
  $socket.on('returnShips', data => {
    let strs = JSON.parse(data);
    let ships = strs.map(str => {
      return lode.parseShipSaveData(str)
    })
    dock.update(_ => ships)
  });
	//Event na celé tabulky
  $socket.emit('getDraftTable');
	//Event který čeká na vrácení celé tabulky
  $socket.on('returnDraftTable', data => {
    table.update(_ => lode.parseDraftTableSaveData(data))
    tableSize.update(_ => $table.length)
  });

	$socket.on('finishStatus', data => {
		if(data){
			$socket.disconnect(true)
		}
  });

  function handleFinish(){
    $socket.emit('finish')
  }


</script>

<main>
	<div class="ship-storage">
    <Dock/>
  </div>
  <div class="game-table">
	<DraftTable />
  </div>
  <button class="game-button" on:click={handleFinish}>HOTOVO</button>
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
