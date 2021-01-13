<script>
  import { socket,enemyTable } from '../stores/game.js';

   function handleClick(e){
     const elem = e.target;
     if(elem.tagName != 'TD') return;
     const x = parseInt(elem.getAttribute('x'));
     const y = parseInt(elem.getAttribute('y'));
     $socket.emit('hit',x+'#'+y)
   }



   $socket.on('eTableUpdate', data => {
     const arr = data.split('#');
     const posX = arr[0];
     const posY = arr[1];
     const val = arr[2];
     let newTable = [...$enemyTable]

     if (val == '0') {
       newTable[posY][posX] = 1
     } else {
       newTable[posY][posX] = 2
     }

     enemyTable.update(_ => newTable)
   });



</script>

<main>
<table on:click={(e) => handleClick(e)}
  cellspacing="0"
  cellpadding="0">
{#if $enemyTable}
  {#each $enemyTable as cols, y}
    <tr>
      {#each cols as cell, x}
        <td {y}{x}{cell}></td>
      {/each}
    </tr>
  {/each}
{/if}
</table>
</main>

<style>
table {
  border: solid 4px black;
  float: right;
}

table:hover {
  cursor: crosshair;
}

td {
  position: relative;
  border: solid 1px white;
  //background: black;
  height: 30px;
  width: 30px;
}

td[cell="1"]::after {
  display: block;
  content: "";
  width: 20px;
  height: 20px;
  box-sizing: border-box;
  border: solid 2px white;
  margin: 0 auto;
}

td[cell="2"]::after {
  display: block;
  content: "✖";
  font-size: 1.4em;
  text-align: center;
  line-height: 20px;
  width: 20px;
  height: 20px;
  color: white;
  box-sizing: border-box;
  margin: 0 auto;
}


/*
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
  height: 30px;
  width: 30px;
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
  height: 26px;
  width: 26px;
  //box-sizing: border-box;
  border: solid black 2px;
}

td.visible.nb-t::after{
  padding-bottom: 2px;
  border-top: 0;
}

td.visible.nb-b::after{
  padding-top: 2px;
  border-bottom: 0;
}

td.visible.nb-r::after{
  padding-left: 2px;
  border-right: 0;
}

td.visible.nb-l::after{
  padding-right: 2px;
  border-left: 0;
}
*/
</style>
