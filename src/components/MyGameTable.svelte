<script>
  import { socket,myTable,myTableHoles } from '../stores/game.js';
  import * as lode from '../lodeLib.js';


  $socket.on('myTableUpdate', data => {
    const arr = data.split('#');
    const posX = arr[0];
    const posY = arr[1];
    const val = arr[2];
    let newTable = [...$myTableHoles]

    if (val == '0') {
      newTable[posY][posX] = 1
    } else {
      newTable[posY][posX] = 2
    }

    myTableHoles.update(_ => newTable)
  });


  function getHole(x,y){
    const hole = $myTableHoles[y][x]
    if (hole) return ' hole'
    return ''
  }

</script>

<main>

<table
  class="holes"
  cellspacing="0"
  cellpadding="0">
{#if $myTableHoles}
  {#each $myTableHoles as cols, y}
    <tr>
      {#each cols as cell, x}
        <td {y}{x}{cell} ></td>
      {/each}
    </tr>
  {/each}
{/if}
</table>

<table
  class="ships"
  cellspacing="0"
  cellpadding="0">
{#if $myTable}
  {#each $myTable as cols, y}
    <tr>
      {#each cols as cell, x}
        <td {y}{x}{cell} class:visible="{cell}"
          class={lode.getBorderClass($myTable,y,x,cell) + getHole(y,x)}></td>
      {/each}
    </tr>
  {/each}
{/if}
</table>

</main>

<style>
table {

}

.holes {
  position: absolute;
  z-index: 2;
  top: 4px;
  left: 4px;
}

.holes td {
  height: 31.6px;
  width: 31.6px;
  //background: green;
}

.holes td[cell="1"]::after {
  display: block;
  content: "";
  width: 20px;
  height: 20px;
  box-sizing: border-box;
  border: solid 4px black;
  margin: 0 auto;
}

.holes td[cell="2"]::after {
  display: block;
  content: "✖";
  font-size: 1.4em;
  text-align: center;
  line-height: 20px;
  width: 20px;
  height: 20px;
  color: black;
  box-sizing: border-box;
  margin: 0 auto;
}

.ships {
  float: left;
  background: rgb(0,95,225,0.6);
  border: solid 4px #005FE1;
}

.ships td {
  position: relative;
  border: solid 1px white;
  //background-color: black;
  height: 30px;
  width: 30px;
}
/*
.ships td:nth-child(n+10){
  border-right: 0;
}
.ships td:nth-child(10n+1){
  border-left: 0;
}
.ships tr:first-child td{
  border-top: 0;
}
.ships tr:last-child td{
  border-bottom: 0;
}
*/
.ships td.visible {
  background: #FD1648;
}

.ships td[cell="h"] {
  background: rgba(255, 0, 0, 0.5);
}

.ships td.visible:not([cell="h"])::after {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  height: 26px;
  width: 26px;
  //box-sizing: border-box;
  border: solid black 2px;
}
/* Vypnutí borderu mezi částemi lodě */
.ships td.visible.nb-t::after{
  padding-bottom: 2px;
  border-top: 0;
}

.ships td.visible.nb-b::after{
  padding-top: 2px;
  border-bottom: 0;
}

.ships td.visible.nb-r::after{
  padding-left: 2px;
  border-right: 0;
}

.ships td.visible.nb-l::after{
  padding-right: 2px;
  border-left: 0;
}

</style>
