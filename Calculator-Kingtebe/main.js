/**
Create By : Kingtebe
Date : Month April 21 10:31 WIB 2011
Wkwkwk sorry style codingan nya masih culun
**/

const readline = require('readline');

const rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout,
});

var white = "\033[97m";
var green = "\033[92m";
var red = "\033[91m";
var yellow = "\033[93m";
var menu_logo = (`\n	${green}Program Calculator Sederhana\n       ${white}==============================\n        -- ${yellow}By ${white}: ${yellow}Kingtebe\n\n ${white}[${green}1${white}] Pertambahan ( ${yellow}+ ${white})\n ${white}[${green}2${white}] Pengurangan ( ${yellow}- ${white})\n ${white}[${green}3${white}] Perkalian ( ${yellow}* ${white})\n ${white}[${green}4${white}] Pembagian ( ${yellow}/ ${white})\n ${white}[${green}5${white}] ${white}Exit\n`);

function cal(){

	'use strict';
	process.stdout.write('\x1Bc');
	console.log(menu_logo);
	rl.question(' >> ', (input) => {
	if (input == '1') {
		rl.question(`\n ${white}-- Bilangan Pertama : ${yellow}`, (one) => {
		rl.question(` ${white}-- Bilangan Kedua : ${yellow}`, (two) => {
			console.log(`\n ${white}======= ${green}Hasil:${yellow}`, parseInt(one) + parseInt(two)+` ${white}=======\n`);rl.close();
	 	});
	    });
	} else if (input == '2' ) {
		rl.question(`\n ${white}-- Bilangan Pertama : ${yellow}`, (one) => {
                rl.question(` ${white}-- Bilangan Kedua : ${yellow}`, (two) => {
			console.log(`\n ${white}======= ${green}Hasil:${yellow}`, parseInt(one) - parseInt(two)+` ${white}=======\n`);rl.close();
	    });
		});
	} else if (input == '3' ) {
		rl.question(`\n ${white}-- Bilangan Pertama : ${yellow}`, (one) => {
                rl.question(` ${white}-- Bilangan Kedua : ${yellow}`, (two) => {
			console.log(`\n ${white}======= ${green}Hasil:${yellow}`, parseInt(one) * parseInt(two)+` ${white}=======\n`);rl.close();
		});
	    });
	} else if (input == '4' ) {
		rl.question(`\n ${white}-- Bilangan Pertama : ${yellow}`, (one) => {
                rl.question(` ${white}-- Bilangan Kedua : ${white}`, (two) => {
			console.log(`\n ${white}======= ${green}Hasil:${yellow}`, parseInt(one) / parseInt(two)+` ${white}=======\n`);rl.close();
	    });
		});
	} else if (input == '5' ) {
		console.log(`\n ${white}Byeee ! Semoga Bermanfaat \n`);rl.close();

		} else

	process.exit(1);
    });
 }

cal();
