
class ShipsTable {
  ships = {}
  locs = {}
  grid = []

  constructor(size) {
    //Vytváři prázdnou tabulku podle velikosti
    this.size = size
    for(let i = 0; i < size; i++) {
      let fragment = [];
      for(let j = 0; j < size; j++){
        fragment.push(0);
      }
      this.grid.push(fragment)
    }
  }

  newId(){
    //Vrací id kontroluje aby nevznikly velké čisla
    const keys = Object.keys(this.ships)
    for(let i=0;i<keys.length;i++){
      if(keys[i] != (i + 1)){
        return (i+1)
      }
    }
  }

  placeShip(ship,posX,posY,hover=false){
    //Zjištuje jestli se jedna o nastínění lode nebo o položení
    let id;
    if(!hover){
      if(this.ships.h)this.removeShip('h')
      id = this.newId();
    } else {
      id = 'h';
    }
    //Hledá jestli je místo na loď
    for(let i=0; i<ship.height; i++){
      for(let j=0; j<ship.width; j++){
        if(ship.grid[i][j]){
          if(this.grid[posY + i][posX + j]) return false;
        }
      }
    }
    //Přidáva loď
    for(let i=0; i<ship.height; i++){
      for(let j=0; j<ship.width; j++){
        if(ship.grid[i][j]){
          this.grid[posY + i][posX + j] = id;
        }
      }
    }
    this.ships[id] = ship;
    this.locs[id] = [posX,posY];
    return id;
  }
  removeShip(id){
    const [posX,posY] = this.locs[id]
    const { width,height } = this.ships[id]
    for(let i=0;i < height; i++){
      for(let j=0;j < width; j++){
        //Prohledává tvar lodě          //Maže místa kde byla loď
        if(this.ships[id].grid[i][j]) this.grid[posY + i][posX + j] = 0
      }
    }
    console.log(this.ships)
    delete this.ships[id]
    console.log(this.ships)
    delete this.locs[id]
  }
  /* TESTOVACÍ */
  //Vrací tabulku jako string kvůli formátování v konzoli
  getGridString(){
    let largeStr = []
    this.grid.forEach( item => {
      largeStr.push(item.join(','))
    });
    return largeStr.join('\n')
  }

  getSaveData(){
    let large = []
    this.grid.forEach(i => {
      large.push(i.join(''))
    });
    return this.size + ',' + large.join('');
  }
}

export default ShipsTable;
