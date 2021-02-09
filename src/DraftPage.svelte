<script>
	import Dock from './components/Dock.svelte'
	import DraftTable from './components/DraftTable.svelte'
  import { socket,table,tableSize,dock,shipSelected } from './stores/planning.js';
  import { baseAddr,state } from './stores/global.js';
  import axios from 'axios'
  import { onMount } from 'svelte';
  import io from 'socket.io-client';
  import * as lode from './lodeLib.js';


	let dif = 2

	function setDif(e) {
		 dif = e.target.value;
	}

	//Připojuje se na server
  socket.update(_ => io($baseAddr + '/plan'))

	//Event který se zavolá když je připojeno
  $socket.on('connect', data => {

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
			state.update(_ => 'game');
		}
  });

  function handleFinish(e){
		e.preventDefault();
    $socket.emit('finish',dif)
  }


</script>

<main>
	<div class="ship-storage">
    <Dock/>
  </div>
  <div class="game-table">
	<DraftTable />
  </div>



	<form on:submit={handleFinish}>
		<div>

			<input type="radio" on:change={setDif} id="r1" name="dif" class="dif-input" value="1">
			<label for="r1" class="dif-label">Lehká</label>

			<input type="radio" on:change={setDif} id="r2" name="dif" class="dif-input" value="2" checked>
			<label for="r2" class="dif-label">Střední</label>

			<input type="radio" on:change={setDif} id="r3" name="dif" class="dif-input" value="3">
			<label for="r3" class="dif-label">Těžká</label>

		</div>

		<button type="submit"
			class="game-button"
			>HOTOVO</button>

			<p>Pro pokračování je potřeba položit všechny lodě</p>

	</form>

</main>

<style>
.game-table, .ship-storage {
  margin: 20px;
  float: left;
}

form {
	float: left;
	margin-top: 25px;
	height: 400px;
	width: 200px;
}

p {
	color: white;
	text-align: center;
}

.dif-input {
	display: none;
}

.dif-label {
	display: block;
	height: 40px;
	width: 120px;
	line-height: 40px;
	text-align: center;
	background: rgba(0,0,0,0.3);
	margin: 5px auto;
	color: white;
}

.dif-input:checked + .dif-label {
	border: solid 2px var(--blue1);
	background: rgba(0,0,0,0.5);
}

.dif-label:hover {
	background-color: rgba(0,0,0,0.6);
}

.game-button {
	margin: 25px auto;
  padding: 12px;
  font-size: 1.2em;
  background: rgba(0,0,0,0.3);
  color: white;
}

.game-button:hover {
  background-color: rgba(0,0,0,0.6)
}
</style>
