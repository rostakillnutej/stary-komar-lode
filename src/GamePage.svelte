<script>
	//import Dock from './components/Dock.svelte'
  import MyGameTable from './components/MyGameTable.svelte'
  import EnemyGameTable from './components/EnemyGameTable.svelte'
  import { winner,state,baseAddr } from './stores/global.js';
  import { socket,myTable,enemyTable,myTableHoles } from './stores/game.js';
  import axios from 'axios'
  import io from 'socket.io-client';
  import * as lode from './lodeLib.js';

  let load = false

	//Připojuje se na server
  socket.update(_ => io($baseAddr + '/game'))

  $socket.on('userError', data => {
    //buď neni účet nebo neni naplánováno
  });

  $socket.on('returnTable', data => {
    const size = parseInt(data.split('#')[0]);
    myTable.update(_ => lode.parseDraftTableSaveData(data))

    enemyTable.update(_ => lode.emptyTable(10))
    myTableHoles.update(_ => lode.emptyTable(10))
    load = true
  });

  $socket.on('endGame', data => {


    state.update(_ => 'gameEnd');
    winner.update(_ => data);
  });

/*
  jak na sockety

  $socket.on('finishStatus', data => {
		if(data){
			$socket.disconnect(true)
			state.update(_ => 'game');
		}
  });

  function handleFinish(){
    $socket.emit('finish')
  }
*/

</script>

<main>
  {#if load}
    <div class="tables">
      <MyGameTable />
      <EnemyGameTable />
    </div>
  {:else}
    <div class="loading">Načítání...</div>
  {/if}
</main>

<style>

.tables {
  max-width: 1000px;
  margin: 40px auto;
}

.loading {
  width: 130px;
  height: 50px;
  line-height: 50px;
  text-align: center;
  position: absolute;
  left: 50%;
  top: 60px;
  font-size: 1.2em;
  transform: translateX(-50%);
  background: rgba(0,0,0,0.6);
  color: white;
}

</style>
