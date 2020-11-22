import { readable,writable } from 'svelte/store';

export const shipSelected = writable(false);

import Ship from '../objects/Ship.js'
/*
  Přiklad používání lodí
  Vytvářet se budo automaticky
  proto je to writable
  Toto je jenom na testování
*/
let s1 = new Ship('Letadlová loď')
s1.preCreate(5,1);
s1.fill(0,0,4,0,1);
let s2 = new Ship('Bitevní loď')
s2.preCreate(4,1);
s2.fill(0,0,3,0,1);
let s3 = new Ship('Křižník')
s3.preCreate(3,1);
s3.fill(0,0,2,0,1);
let s4 = new Ship('Ponorka')
s4.preCreate(3,1);
s4.fill(0,0,2,0,1);
let s5 = new Ship('Torpédoborec')
s5.preCreate(2,1);
s5.fill(0,0,1,0,1);

//s3.rotate();

export const dock = writable([s1,s2,s3,s4,s5]);
