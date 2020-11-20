class Ship {
  width = 0;
  height = 0;
  grid = [];
  trans = false;

  constructor(name = 'default',type='none') {
    this.name = name;
    this.type = type;
  }

  preCreate(width,height){
    //Vytváří prázdnou mřížku
    this.width = width;
    this.height = height;
    for(let i = 0; i < height; i++) {
      let fragment = [];
      for(let j = 0; j < width; j++){
        fragment.push(0);
      }
      this.grid.push(fragment)
    }
  }

  rotate(){
    //Převrací tabulku lodě po směru hodin
    let newGrid = [];
    if(this.trans){
      for(let i = this.width - 1; i >= 0; i--) {
        let fragment = [];
        for(let j = this.height - 1; j >= 0; j--){
          fragment.push(this.grid[j][i]);
        }
        newGrid.push(fragment)
      }
    } else {
      for(let i = 0; i < this.width; i++) {
        let fragment = [];
        for(let j = 0; j < this.height; j++){
          fragment.push(this.grid[j][i]);
        }
        newGrid.push(fragment)
      }
    }
    //Mění výšku a šírku
    this.trans = !this.trans
    this.grid = newGrid;
    const mem = this.width
    this.width = this.height
    this.height = mem
  }

  //Funkce na vytváření části lodě
  //Vylpní čtverec podle zadaných souřadnic
  fill(fromX,fromY,toX,toY,data){
    for(let i=fromY;i<=toY;i++){
      for(let j=fromX;j<=toX;j++){
        this.grid[i][j] = data;
      }
    }

  }

  getSaveData(){
    //Vrací data tabulky v kompaktnějším formátu
    let large = []
    this.grid.forEach(i => {
      large.push(i.join(''))
    });
    return this.width + ',' + this.height + ',' + large.join('');
  }

  parseSaveData(str){
    //Přemění kompaktnější data na data lodě
    const arr = str.split(',')
    this.width = arr[0];
    this.height = arr[1];
    for(let i = 0; i < arr[1]; i++) {
      let fragment = [];
      for(let j = 0; j < arr[0]; j++){
        fragment.push(arr[2][i+j]);
      }
      this.grid.push(fragment)
    }
  }

  /* TESTOVACÍ */
  getGridString(){
    let largeStr = []
    this.grid.forEach( item => {
      largeStr.push(item.join(','))
    });
    return largeStr.join('\n')
  }


}

export default Ship;
