<script>
  import { createEventDispatcher } from 'svelte';
  const dispatch = createEventDispatcher();
  import { socket,table,tableSize,dock,shipSelected,isHover,hoverPos } from '../stores/planning.js';
  import * as lode from '../lodeLib.js'

  function handleClick(e){
    //Kliknutí na tabulku s planováním
    const elem = e.target;
    if(elem.tagName != 'TD') return;
    //Event na přidání lodě z kurzoru
    if($shipSelected){
      const x = parseInt(elem.getAttribute('x'));
      const y = parseInt(elem.getAttribute('y'));
      const index = $dock.indexOf($shipSelected);
      $socket.emit('placeShip',index,x,y)
      return;
    }
    //Event na odebraní lodě zpátky na kurzor
    const id = parseInt(elem.getAttribute('cell'));
    if(id){
      $socket.emit('removeShip',id)
    }

  }

  $socket.on('placeStatus', data => {
    const dataArr = JSON.parse(data)
    if(dataArr[0]){
      table.update(_ => {
        isHover.update(_ => false);
        let newTable = lode.removeShip($table,$shipSelected,$hoverPos[0],$hoverPos[1],'h')
        newTable = lode.placeShip(newTable,$shipSelected,dataArr[1],dataArr[2],dataArr[0])
        return newTable
      })
      const index = $dock.indexOf($shipSelected);
      const newDock = [...$dock];
      newDock.splice(index,1)
      dock.update(_ => newDock);
      shipSelected.update(_ => false);
      const exist = document.querySelector('#sticked');
      if(exist)exist.remove();
    }
  });

  $socket.on('removeStatus', data => {
    const dataArr = JSON.parse(data)
    if(dataArr[0]){
      const removed = lode.parseShipSaveData(dataArr[0])
      const newDock = [...$dock,removed];
      dock.update(_ => newDock)
      table.update(_ => {
        return lode.removeShip($table,removed,dataArr[1],dataArr[2],dataArr[3])
      })
    }
  });

  function handleOver(e){
    const elem = e.target
    if(elem.tagName != 'TD' || $shipSelected == false) return;
    const x = parseInt(elem.getAttribute('x'));
    const y = parseInt(elem.getAttribute('y'));
    //Když se pozice nezměnila
    if($isHover && $hoverPos[0] == x && $hoverPos[1] == y) return;
    //Vymaže stré nastínění
    if($isHover){
      table.update(_ => {
        return lode.removeShip($table,$shipSelected,$hoverPos[0],$hoverPos[1],'h')
      })
      isHover.update(_ => false)
    }
    //Kontroluje správnost nastínění
    if(x + $shipSelected.width > $tableSize || y + $shipSelected.height > $tableSize) return;
    const result = lode.placeShip($table,$shipSelected,x,y)
    if(result){
      table.update(_ => result)
      hoverPos.update(_ => [x,y]);
      isHover.update(_ => true);
    }
  }

  function checkBorder(y,x,val,str){
    if(y > 9 || y < 0 || x > 9 || x < 0) return ''
    if($table[y][x] == val) return str
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
{#if $table}
  {#each $table as cols, y}
    <tr>
      {#each cols as cell, x}
        <td {y}{x}{cell} class:visible="{cell}" class={getBorderClass(y,x,cell)}></td>
      {/each}
    </tr>
  {/each}
{/if}
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
