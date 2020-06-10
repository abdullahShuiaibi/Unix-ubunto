#!/user/bin/node

const util = requir("util");
const exec =requir("child_process").exec;

console.log("Begging is fun");
dir=exec("ls","-al","/home/abdullah")
