<script>
  import ShipsTable from './objects/ShipsTable.js'
	import Dock from './components/Dock.svelte'
	import DraftTable from './components/DraftTable.svelte'

/*
	function place(ship,x,y){
    const id = st.placeShip(ship,x,y)
		gridy = st.grid
		return id
	}

	function remove(id){
		st.removeShip(id);
		gridy = st.grid
	}
*/
  //console.log(st.getGridString());


	function handlePlace(e) {

		if(selected && e.target.tagName == 'TD'){
			document.querySelector('#sticked').remove()
			const x = parseInt(e.target.getAttribute('x'));
			const y = parseInt(e.target.getAttribute('y'));
			const ship = storage[selected - 1];
			selected = false;
			if(x + ship.width > tableSize || y + ship.height > tableSize)return
/*
			console.log(ship.width)
			console.log(ship.height)
			console.log(tableSize)
			console.log(x,y)
*/
			//console.log(x,y,ship);
			place(ship,x,y);
			/*
			console.log(storage[selected - 1])
			console.log(e.target.getAttribute('x'))
			console.log(e.target.getAttribute('y'))
			console.log(e.target.tagName)
			*/
		}
	}



	function handleOver(e) {
	}


</script>

<main>
	<div class="ship-storage">
    <Dock />
  </div>
  <div class="game-table">
	<DraftTable tableSize={10} />
  </div>
</main>

<style>
.game-table, .ship-storage {
  margin: 20px;
  float: left;
}
</style>
