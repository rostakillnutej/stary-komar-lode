
class ShipsTable {
  ships = {}
  locs = {}
  grid = []
  curId = 0

  constructor(size) {
    this.size = size
    for(let i = 0; i < size; i++) {
      let fragment = [];
      for(let j = 0; j < size; j++){
        fragment.push(0);
      }
      this.grid.push(fragment)
    }
  }
  placeShip(ship,posX,posY){
    this.curId ++;
    const id = this.curId;
    this.ships[id] = ship;
    this.locs[id] = [posX,posY];
    //Validating empty space
    for(let i=0; i<ship.height; i++){
      for(let j=0; j<ship.width; j++){
        if(ship.grid[i][j]){
          if(this.grid[posY + i][posX + j]) return false;
        }
      }
    }
    //Placing ship template
    for(let i=0; i<ship.height; i++){
      for(let j=0; j<ship.width; j++){
        if(ship.grid[i][j]){
          this.grid[posY + i][posX + j] = id;
        }
      }
    }
    return id;
  }
  removeShip(id){
    const [posX,posY] = this.locs[id]
    const { width,height } = this.ships[id]
    for(let i=0;i < height; i++){
      for(let j=0;j < width; j++){
        this.grid[posY + i][posY + j] = 0
      }
    }

  }
  getGridString(){
    let largeStr = []
    this.grid.forEach( item => {
      largeStr.push(item.join(','))
    });
    return largeStr.join('\n')
  }
  /*
  getSaveData(){
    let large = []
    this.grid.forEach(i => {
      large.push(i.join(''))
    });
    return this.size + ',' + large.join('');
  }
  */
}

export default ShipsTable;
