<script>
  import { createEventDispatcher } from 'svelte';
  const dispatch = createEventDispatcher();
  import { dock,shipSelected } from '../stores/planning.js';
  import ShipsTable from '../objects/ShipsTable.js'
  export let st;
  export let grid;

  function putShip(elem){
    const x = parseInt(elem.getAttribute('x'));
    const y = parseInt(elem.getAttribute('y'));
    if(x + $shipSelected.width > st.size || y + $shipSelected.height > st.size)return
    if(!st.placeShip($shipSelected,x,y))return;
    console.log(st.locs)
    dispatch('update');
    shipSelected.update(_ => false);
    const exist = document.querySelector('#sticked');
    if(exist)exist.remove();
  }

  function getShip(id){
    shipSelected.update(_ => st.ships[id])
    const ship = st.ships[id].grid
    st.removeShip(id)
    dispatch('update')
    //Vytvoření tabulky která se pohybuje s myší
    const cln = document.createElement('table');
    cln.setAttribute('id', 'sticked');
    cln.setAttribute('cellspacing', '0');
    cln.setAttribute('cellpadding', '0');
    cln.classList.add('ship-grid');
    ship.forEach((row, i) => {
      const tr = document.createElement('tr');
      row.forEach((cell, j) => {
        const td = document.createElement('td');
        if(cell) td.classList.add('visible');
        tr.appendChild(td);
      });
      cln.appendChild(tr);
    });
    document.body.appendChild(cln);
    /* Tady nevím jestli se potom ty listenery mažou*/
    document.addEventListener('mousemove', e => {
    	cln.style.transform = 'translateY('+ (e.clientY + 10) + 'px)';
    	cln.style.transform += 'translateX('+ (e.clientX - 20) + 'px)';
    },false);
  }


  function handleClick(e){
    //Kliknutí na tabulku s planováním
    const elem = e.target;
    if(elem.tagName != 'TD') return;
    //Event na přidání lodě z kurzoru
    if($shipSelected){
      putShip(elem);
      return;
    }
    //Event na odebraní lodě zpátky na kurzor
    const id = parseInt(elem.getAttribute('cell'));
    if(id){
      getShip(id);
    }

  }

  function handleOver(e){
    const elem = e.target
    if(elem.tagName != 'TD' || $shipSelected == false) return;

    if(st.ships['h'])st.removeShip('h')
    const x = parseInt(elem.getAttribute('x'));
    const y = parseInt(elem.getAttribute('y'));
    if(x + $shipSelected.width > st.size || y + $shipSelected.height > st.size)return
    if(!st.placeShip($shipSelected,x,y,true))return
    dispatch('update')
  }

  function checkBorder(y,x,val,str){
    if(y > 9 || y < 0 || x > 9 || x < 0) return ''
    if(grid[y][x] == val) return str
    return ''
  }

  function getBorderClass(y,x,cell){
    if (cell == 'h' || cell == 0) return '';
    let borders = ''
    borders += checkBorder(y,x+1,cell,'nb-r ');
    borders += checkBorder(y+1,x,cell,'nb-b ');
    borders += checkBorder(y,x-1,cell,'nb-l ');
    borders += checkBorder(y-1,x,cell,'nb-t ');
    return borders;
  }


</script>
<table on:click={(e) => handleClick(e)}
  on:mousemove={(e) => handleOver(e)}
  cellspacing="0"
  cellpadding="0">
{#each grid as cols, y}
  <tr>
    {#each cols as cell, x}
      <td {y}{x}{cell} class:visible="{cell}" class={getBorderClass(y,x,cell)}></td>
    {/each}
  </tr>
{/each}
</table>


<style>
  table {
    background: rgb(0,95,225,0.6);
    border: solid 4px #005FE1;
  }

  table:hover {
  	cursor: crosshair;
  }

  td {
    position: relative;
    border: solid 1px white;
    //background-color: black;
    height: 40px;
    width: 40px;
  }

  td:nth-child(n+10){
    border-right: 0;
  }
  td:nth-child(10n+1){
    border-left: 0;
  }
  tr:first-child td{
    border-top: 0;
  }
  tr:last-child td{
    border-bottom: 0;
  }

  td.visible {
    background: #FD1648;
  }

  td[cell="h"] {
    background: rgba(255, 0, 0, 0.5);
  }

  td.visible:not([cell="h"])::after {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    height: 32px;
    width: 32px;
    //box-sizing: border-box;
    border: solid black 4px;
  }
/* Vypnutí borderu mezi částemi lodě */
  td.visible.nb-t::after{
    padding-bottom: 4px;
    border-top: 0;
  }

  td.visible.nb-b::after{
    padding-top: 4px;
    border-bottom: 0;
  }


  td.visible.nb-r::after{
    padding-left: 4px;
    border-right: 0;
  }

  td.visible.nb-l::after{
    padding-right: 4px;
    border-left: 0;
  }

/*
  nb-t
*/
</style>
