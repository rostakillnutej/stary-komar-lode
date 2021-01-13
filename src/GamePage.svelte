<script>
	//import Dock from './components/Dock.svelte'
  import MyGameTable from './components/MyGameTable.svelte'
  import EnemyGameTable from './components/EnemyGameTable.svelte'
  import { baseAddr } from './stores/global.js';
  import { socket,myTable,enemyTable,myTableHoles } from './stores/game.js';
  import axios from 'axios'
  import io from 'socket.io-client';
  import * as lode from './lodeLib.js';

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
  });

  $socket.on('endGame', data => {
    console.log(data)
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
  <MyGameTable />
  <EnemyGameTable />
</main>

<style>

</style>
