export function emptyTable(size) {
  let grid = []
  for(let i = 0; i < size; i++) {
    let fragment = [];
    for(let j = 0; j < size; j++){
      fragment.push(0);
    }
    grid.push(fragment);
  }
  return grid;
}

//Přemění kompaktnější data na data plánovací tabulky
export function parseDraftTableSaveData(str){
  const arr = str.split('#')
  let grid = []
  for(let i = 0; i < arr[0]; i++) {
    let fragment = [];
    for(let j = 0; j < arr[0]; j++){
      fragment.push(0);
    }
    grid.push(fragment);
  }
  //Parsuje lodě a pozice lodí
  const pos = JSON.parse(arr[1]);
  const ships = JSON.parse(arr[2]);
  //Přeměnuje data na lodě a podle pozic je poklada
  const ids = Object.keys(pos);
  ids.forEach(i => {
    const ship = parseShipSaveData(ships[i]);
    const x = pos[i][0];
    const y = pos[i][1];
    grid = placeShip(grid,ship,x,y,i)
  });

  return grid;
}

//Přemění kompaktnější data na data lodě
export function parseShipSaveData(str){
  const arr = str.split(',')
  let ship = {}
  ship.name = arr[0];
  ship.type = arr[1];
  ship.width = parseInt(arr[2]);
  ship.height = parseInt(arr[3]);
  ship.grid = []
  for(let i = 0; i < arr[3]; i++) {
    let fragment = [];
    for(let j = 0; j < arr[2]; j++){
      fragment.push(arr[4][i+j]);
    }
    ship.grid.push(fragment)
  }
  return ship
}

export function placeShip(grid,ship,posX,posY,id = 'h'){
  //když se jedná o nastínění položení lodě
  if(id == 'h'){
    //Kontroluje jestli nazavazí jiná loď
    for(let i=0; i<ship.height; i++){
      for(let j=0; j<ship.width; j++){
        if(ship.grid[i][j]){
          if(grid[posY + i][posX + j]) return false
        }
      }
    }
  }

  //Pokládá loď do gridu na stránce
  for(let i=0; i<ship.height; i++){
    for(let j=0; j<ship.width; j++){
      if(ship.grid[i][j]){
        grid[posY + i][posX + j] = id;
      }
    }
  }
  return grid
}

export function removeShip(grid,ship,posX,posY,id){
  for(let i=0;i < ship.height; i++){
    for(let j=0;j < ship.width; j++){
      //Prohledává tvar lodě          //Maže místa kde byla loď
      if(ship.grid[i][j]) grid[posY + i][posX + j] = 0
    }
  }
  return grid
}

//Vytváři bordery loděm
function checkBorder(table,y,x,val,str){
  if(y > 9 || y < 0 || x > 9 || x < 0) return ''
  if(table[y][x] == val) return str
  return ''
}
export function getBorderClass(table,y,x,cell){
  if (cell == 'h' || cell == 0) return '';
  let borders = ''
  borders += checkBorder(table,y,x+1,cell,'nb-r ');
  borders += checkBorder(table,y+1,x,cell,'nb-b ');
  borders += checkBorder(table,y,x-1,cell,'nb-l ');
  borders += checkBorder(table,y-1,x,cell,'nb-t ');
  return borders;
}

//Vytvoření tabulky která se pohybuje s myší
export function createSticky(grid){
  const cln = document.createElement('table');
  cln.setAttribute('id', 'sticked');
  cln.setAttribute('cellspacing', '0');
  cln.setAttribute('cellpadding', '0');
  cln.classList.add('ship-grid');
  grid.forEach((row, i) => {
    const tr = document.createElement('tr');
    row.forEach((cell, j) => {
      const td = document.createElement('td');
      if(cell) td.classList.add('visible');
      tr.appendChild(td);
    });
    cln.appendChild(tr);
  });
  document.body.appendChild(cln);
  // Tady nevím jestli se potom ty listenery mažou
  document.addEventListener('mousemove', e => {
    cln.style.transform = 'translateY('+ (e.clientY + 10) + 'px)';
    cln.style.transform += 'translateX('+ (e.clientX - 20) + 'px)';
  },false);
}
